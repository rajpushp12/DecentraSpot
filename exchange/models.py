from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    wallet_address=models.CharField(max_length=20)



class Balance(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    usd=models.FloatField(default=0)
    btc=models.FloatField(default=0)
    eth=models.FloatField(default=0)
    ada=models.FloatField(default=0)
    sol=models.FloatField(default=0)
    xrp=models.FloatField(default=0)
    dot=models.FloatField(default=0)
    uni=models.FloatField(default=0)
    ltc=models.FloatField(default=0)
    


    def __str__(self):
        return f"user: {self.user}"


class Transfers(models.Model):
    sender=models.CharField(max_length=32, default=None)
    receiver=models.CharField(max_length=32, default=None)
    asset=models.CharField(max_length=4)
    amount=models.FloatField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.sender}, To: {self.receiver}, amount: {self.amount} {self.asset}"

class Requests(models.Model):
    user=models.CharField(max_length=32, default=None)
    asset=models.CharField(max_length=4)
    amount=models.FloatField()
    request_time=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10, default='Pending')
    financer=models.CharField(max_length=32, default=None)
    complete_time=models.DateTimeField(default=None)

    def __str__(self):
        return f"User: {self.user}, amount: {self.amount} {self.asset}"