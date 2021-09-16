from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)



class Balance(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    busd=models.FloatField(default=0)
    btc=models.FloatField(default=0)
    eth=models.FloatField(default=0)
    ada=models.FloatField(default=0)
    bnb=models.FloatField(default=0)
    sol=models.FloatField(default=0)
    xrp=models.FloatField(default=0)
    dot=models.FloatField(default=0)
    uni=models.FloatField(default=0)
    ltc=models.FloatField(default=0)
    


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
            "amount":self.amount,
            "time":self.time
        }