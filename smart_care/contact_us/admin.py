from django.contrib import admin
from . models import Contact_us
# Register your models here.




class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'problem']
   
  
admin.site.register(Contact_us,ContactModelAdmin)