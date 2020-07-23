from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

class PersonnelsInline(admin.StackedInline):
    model = Personnels
    can_delete = False
    verbose_name_plural = 'personnels'

class UserAdmin(BaseUserAdmin):
    inlines = (PersonnelsInline,)
    # provide further customisations here

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Domaine)
admin.site.register(Millesime)
admin.site.register(Organisation)
admin.site.register(Personnels)