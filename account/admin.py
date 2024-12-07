from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=('firstname','lastname','email','last_login','date_joined')
    list_display_links=('firstname','lastname','email','last_login','date_joined')
    filter_horizontal=()
    list_filter=()
    ordering=()
    fieldsets=()

admin.site.register(Account,AccountAdmin)
