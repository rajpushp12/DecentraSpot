from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from .models import *



def index(request):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':1,
    'limit':16,
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '960d1775-50a1-4b05-8e81-0ee3be509a4f',
    }

    session = Session()
    session.headers.update(headers)

    list, cur_list = [], []
    price_set, market_cap, change24h, change7d = {}, {}, {}, {}
  
    
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        for detail in data["data"]:
            cur_list.append(detail["symbol"].lower())
            list.append(detail["quote"])

        for (c, x) in zip(cur_list,list):
            price_set[c]=(round(x["USD"]["price"],2))
            change24h[c]=(round((x["USD"]["percent_change_24h"]),2))
            change7d[c]=(round(x["USD"]["percent_change_7d"],2))
            market_cap[c]=(round(x["USD"]["market_cap"]/(pow(10,9)),2))

        return render(request, 'exchange/index.html',{
            'price':price_set,
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
                "message": "Invalid username or password."
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


@login_required
def balance(request, username):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':1,
    'limit':16,
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '960d1775-50a1-4b05-8e81-0ee3be509a4f',
    }

    session = Session()
    session.headers.update(headers)

    list, cur_list = [], []
    price_set={}
  
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    for detail in data["data"]:
        cur_list.append(detail["symbol"].lower())
        list.append(detail["quote"])

    for (c, x) in zip(cur_list,list):
        price_set[c]=(round(x["USD"]["price"],2))

    if request.user.is_authenticated:
        user=User.objects.get(username=username)
        balance_fetch=Balance.objects.get(user=user.id)

        balance = {}

        value={
        'btc':(balance_fetch.btc),
        'bnb':(balance_fetch.bnb),
        'ada':(balance_fetch.ada),
        'xrp':(balance_fetch.xrp),
        'uni':(balance_fetch.uni),
        'sol':(balance_fetch.sol),
        'eth':(balance_fetch.eth),
        'dot':(balance_fetch.dot),
        'usdt':(balance_fetch.usdt)
        }

        for m in value:
            balance[m]=round((value[m]),4)

        for n in value:
            value[n]=round((value[n]*price_set[n]),4)


        total=0

        for i in value:
            total=total+value[i]
        

        total=round(total,2)
        usdt= round(balance["usdt"],2)
        spot=round((total-(balance["usdt"])),2)

        return render(request, 'exchange/balance.html',{
            'spot':spot,
            'usdt':usdt,
            'total':total,
            'value':value,
            'balance':balance
        })

    else:
        return HttpResponseRedirect(reverse('login'))





@login_required
@csrf_exempt
def add_usd(request, username):

    try:
        user=User.objects.get(username=username)
        balance=Balance.objects.get(user=user.id)

        if request.method == "PUT":

            data=json.loads(request.body)
            
            x = balance.usdt + data["amount"]
            balance.usdt = x
            balance.save()

    except User.DoesNotExist:
        return JsonResponse({"error": "Email not found."}, status=404)






@login_required
def add_transaction(request, username):

    try:
        user=User.objects.get(username=username)

        if request.method == "GET":
            return render(request, 'exchange/send.html')



        if request.method == "POST":

            asset=request.POST["asset"]
            amount=float(request.POST["amount"])
            password=request.POST["password"]
            recipient=request.POST["recipient"]

            recipient_fetch = User.objects.get(username=recipient)

            check = authenticate(request, username=username, password=password)
            if check is not None:

                sent_balance=Balance.objects.get(user=user.id)
                m=getattr(sent_balance, asset)

                if amount<=m  and recipient_fetch is not None:
                    m= m - amount
                    setattr(sent_balance, asset, m)
                    sent_balance.save()

                    received_balance=Balance.objects.get(user=recipient_fetch.id)
                    n=getattr(received_balance, asset)
                    n= n + amount

                    setattr(received_balance, asset, n)
                    received_balance.save()

                    detail=Transactions()
                    detail.user=username
                    detail.asset=asset
                    detail.amount=amount
                    detail.recipient=recipient
                    detail.save()

                    return redirect('transaction', username)

                else:
                    return render(request, 'exchange/send.html', {
                        'message': 'Insufficient Balance'
                    })
 
            else:
                return render(request, 'exchange/send.html', {
                        'message': 'Invalid Password'
                    })


    except User.DoesNotExist:
        return render(request, 'exchange/send.html', {
                'message': 'User Does not Exist'
            })




@login_required
def trade(request, asset):

    
    try:
        user=User.objects.get(username=request.user.username)

        if request.method == "GET":
            return render(request, 'exchange/trade.html', {
                'asset': asset
            })


        if request.method == "POST":

            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
            parameters = {
            'start':1,
            'limit':16,
            'convert':'USD'
            }
            headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '960d1775-50a1-4b05-8e81-0ee3be509a4f',
            }

            session = Session()
            session.headers.update(headers)

            list, cur_list = [], []
            price_set={}
  
    
            response = session.get(url, params=parameters)
            data = json.loads(response.text)

            for detail in data["data"]:
                cur_list.append(detail["symbol"].lower())
                list.append(detail["quote"])

            for (c, x) in zip(cur_list,list):
                price_set[c]=(round(x["USD"]["price"],2))



            if 'buy' in request.POST:
                amount=float(request.POST["amount"])

                balance=Balance.objects.get(user=user.id)
                m=getattr(balance, asset)
                n=balance.usdt

                if amount<=balance.usdt:

                    m= m + (amount/price_set[asset])
                    setattr(balance, asset, m)
                    balance.save()

                    n= n - amount
                    balance.usdt=n
                    balance.save()

                    order=Orders()
                    order.user=request.user.username
                    order.asset_amount=amount/price_set[asset]
                    order.status="buy"
                    order.asset=asset
                    order.busd_amount=amount
                    order.save()
                    return redirect('balance', request.user.username)
 
                else:
                    return render(request, 'exchange/trade.html', {
                    'message': 'Insufficient Balance',
                    'asset': asset
                    })



            if 'sell' in request.POST:

                amount=float(request.POST["amount"])

                balance=Balance.objects.get(user=user.id)
                a=getattr(balance, asset)
                b=balance.usdt

                if (a*price_set[asset])>=amount:

                    a= a - (amount/price_set[asset])
                    setattr(balance, asset, a)
                    balance.save()

                    b= b + amount
                    balance.usdt=b
                    balance.save()

                    order=Orders()
                    order.user=request.user.username
                    order.asset_amount=amount/price_set[asset]
                    order.status="sell"
                    order.asset=asset
                    order.busd_amount=amount
                    order.save()

                    return redirect('balance', request.user.username)
 
                else:
                    return render(request, 'exchange/trade.html', {
                    'message': f'Insufficient {asset}',
                    'asset': asset
                    })

    except User.DoesNotExist:
        return HttpResponse("Error: User doesn't exist")



@login_required
def transaction(request, username):

    if request.method == 'GET':

        try:
            sent_list=Transactions.objects.filter(user=username).order_by('-time')
            received_list=Transactions.objects.filter(recipient=username).order_by('-time')


            return render(request, 'exchange/transactions.html', {
                'sent_list':sent_list,
                'received_list':received_list
            })


        except Transactions.DoesNotExist:
            return HttpResponse("Error: User doesn't exist")



@login_required
def order(request, username):

    if request.method == 'GET':

        try:
            buy_orders=Orders.objects.filter(user=username, status='buy').order_by('-time')
            sell_orders=Orders.objects.filter(user=username, status='sell').order_by('-time')


            return render(request, 'exchange/orders.html', {
                'buy_orders':buy_orders,
                'sell_orders':sell_orders
            })


        except Orders.DoesNotExist:
            return HttpResponse("Error: Order doesn't exist")



