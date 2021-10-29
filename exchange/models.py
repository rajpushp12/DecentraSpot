from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)



class Balance(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    usdt=models.FloatField(default=0)
    btc=models.FloatField(default=0)
    eth=models.FloatField(default=0)
    ada=models.FloatField(default=0)
    bnb=models.FloatField(default=0)
    sol=models.FloatField(default=0)
    xrp=models.FloatField(default=0)
    dot=models.FloatField(default=0)
    uni=models.FloatField(default=0)
    


    def __str__(self):
        return f"user: {self.user}"


class Transactions(models.Model):

    user=models.CharField(max_length=32)
    recipient=models.CharField(max_length=32)
    asset=models.CharField(max_length=4)
    amount=models.FloatField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.user}, To: {self.recipient}, amount: {self.amount} {self.asset}"

    def serialize(self):

        return{
            "user":self.user,
            "asset":self.asset,
            "amount":self.amount,
            "time":self.time
        }



class Orders(models.Model):

    user=models.CharField(max_length=32)
    status=models.CharField(max_length=4)
    asset=models.CharField(max_length=4)
    asset_amount=models.CharField(max_length=4)
    busd_amount=models.FloatField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user}, amount: {self.asset_amount} {self.asset}"

    def serialize(self):

        return{
            "user":self.user,
            "asset":self.asset,
            "amount":self.asset_amount,
            "status":self.status,
            "time":self.time
        }