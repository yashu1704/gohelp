from django.contrib import admin
from .models import Client, ServiceProvider, ServiceHistory
admin.site.register(Client)
admin.site.register(ServiceProvider)
admin.site.register(ServiceHistory)
