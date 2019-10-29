from django.contrib import admin
from django.urls import path
import eventex.core.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', eventex.core.views.home),
    path('admin/', admin.site.urls),
]

urlpatterns += [] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
