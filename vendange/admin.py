from django.contrib import admin
from .models import *
from .forms import *

class BenneAdmin(admin.ModelAdmin):
    form = BenneForm
admin.site.register(Benne, BenneAdmin)
admin.site.register(Marc)