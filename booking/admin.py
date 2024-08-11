from django.contrib import admin
from .models import DestinationBook,ServiceBook
# Register your models here.
admin.site.register([DestinationBook,ServiceBook])