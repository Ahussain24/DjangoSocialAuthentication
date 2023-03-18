from django.contrib import admin
from .models import Customer

# Register your models here.




class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'provider', 'uid', 'created_at', 'updated_at']
    fields = ['user', 'provider', 'uid', 'extra_data']

admin.site.register(Customer, CustomerAdmin)

