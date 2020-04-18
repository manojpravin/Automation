from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(activeusers)
admin.site.register(loggedinusers)