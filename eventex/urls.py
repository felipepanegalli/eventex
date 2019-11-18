from django.contrib import admin
from django.urls import path

import eventex.core.views

urlpatterns = [
    path('', eventex.core.views.home),
    path('admin/', admin.site.urls),
]
