from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['name', "address",'phone', 'birthday', 'date_register']
    search_fields = ['name']
    ordering = ["name"]
    
   
admin.site.register(Cliente, ClienteAdmin)