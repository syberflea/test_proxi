from django.contrib import admin

from .models import Client, Owner, UserAccount

admin.site.register(UserAccount)
admin.site.register(Owner)
admin.site.register(Client)
