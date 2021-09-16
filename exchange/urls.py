from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('trade/<str:asset>', views.trade, name='trade'),
    path('balance/<str:username>', views.balance, name='balance'),
    path('add_transaction/<str:username>', views.add_transaction, name='add_transaction'),
    

    #api routes
    path('add_usd/<str:username>', views.add_usd, name='add_usd'),
    path('add_request/<str:username>', views.add_request, name='add_request')

]