from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from .models import *



def index(request):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':1,
    'limit':9,
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '960d1775-50a1-4b05-8e81-0ee3be509a4f',
    }

    session = Session()
    session.headers.update(headers)

    list=[]
    price_set, market_cap, change24h, change7d = [], [], [], []
    
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        for detail in data["data"]:
            list.append(detail["quote"])

        for x in list:
            price_set.append(x["USD"]["price"])
            change24h.append(x["USD"]["percent_change_24h"])
            change7d.append(x["USD"]["percent_change_7d"])
            market_cap.append(x["USD"]["market_cap"]/(pow(10,9)))

        price={
            'btc':round(price_set[0],2),
            'eth':round(price_set[1],2),
            'ada':round(price_set[2],2),
            'bnb':round(price_set[3],2),
            'sol':round(price_set[5],2),
            'xrp':round(price_set[6],2),
            'dot':round(price_set[8],2)
            }

        market_cap={
            'btc':round(market_cap[0],2),
            'eth':round(market_cap[1],2),
            'ada':round(market_cap[2],2),
            'bnb':round(market_cap[3],2),
            'sol':round(market_cap[5],2),
            'xrp':round(market_cap[6],2),
            'dot':round(market_cap[8],2)
            }

        change24h={
            'btc':round(change24h[0],2),
            'eth':round(change24h[1],2),
            'ada':round(change24h[2],2),
            'bnb':round(change24h[3],2),
            'sol':round(change24h[5],2),
            'xrp':round(change24h[6],2),
            'dot':round(change24h[8],2)
            }

        change7d={
            'btc':round(change7d[0],2),
            'eth':round(change7d[1],2),
            'ada':round(change7d[2],2),
            'bnb':round(change7d[3],2),
            'sol':round(change7d[5],2),
            'xrp':round(change7d[6],2),
            'dot':round(change7d[8],2)
            }


        return render(request, 'exchange/index.html',{
            'price':price,
            'market_cap':market_cap,
            'change24h':change24h,
            'change7d':change7d
        })

    except (ConnectionError, Timeout, TooManyRedirects) as message:
        return HttpResponse(message)
    



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "exchange/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "exchange/login.html")




def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))




def register(request):
    if request.method == "POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]

        username = request.POST["username"]
        email = request.POST["email"]
        wallet_address= username + '@spot'
        
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "exchange/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name=firstname
            user.last_name=lastname
            user.wallet_address=wallet_address
            user.save()

            balance=Balance()
            balance.user=user
            balance.save()

        except IntegrityError:
            return render(request, "exchange/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))


    else:
        return render(request, "exchange/register.html")