from django.contrib import admin
from .models import Carosel

# Register your models here.

class CaroselAdmin(admin.ModelAdmin):
    list_display = ('id','title','added_date')

admin.site.register(Carosel,CaroselAdmin)