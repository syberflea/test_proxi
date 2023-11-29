from django.contrib import admin
from .models import UserAccount, Owner, Client

admin.site.register(UserAccount)
admin.site.register(Owner)
admin.site.register(Client)
