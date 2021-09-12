from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=("id", "username", "email", "wallet_address", "last_login")

class BalanceAdmin(admin.ModelAdmin):
    list_display=("user", "usd", "btc", "eth", "ada", "sol", "xrp", "dot")

class TransfersAdmin(admin.ModelAdmin):
    list_display=("sender", "receiver", "asset", "amount", "time")

class RequestsAdmin(admin.ModelAdmin):
    list_display=("user", "amount", "asset", "status", "request_time")



admin.site.register(User, UserAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(Requests, RequestsAdmin)
admin.site.register(Transfers, TransfersAdmin)