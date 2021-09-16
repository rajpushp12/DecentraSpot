from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=("id", "username", "email", "last_login")

class BalanceAdmin(admin.ModelAdmin):
    list_display=("user", "busd", "btc", "eth", "ada", "sol", "xrp", "dot", "uni", "ltc")

class TransactionsAdmin(admin.ModelAdmin):
    list_display=("user", "recipient", "asset", "amount", "time")



admin.site.register(User, UserAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(Transactions, TransactionsAdmin)