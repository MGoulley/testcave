# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),  # add this
    path("administration/", include("administration.urls")),
    path("entrants/", include("entrants.urls")),
    path("vendange/", include("vendange.urls")),
    path("cave/", include("cave.urls")),
]