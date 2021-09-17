from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('trade/<str:asset>', views.trade, name='trade'),
    path('balance/<str:username>', views.balance, name='balance'),
    path('transaction/<str:username>', views.transaction, name='transaction'),
    path('order/<str:username>', views.order, name='order'),
    path('add_transaction/<str:username>', views.add_transaction, name='add_transaction'),
    

    #api routes
    path('add_usd/<str:username>', views.add_usd, name='add_usd')

]