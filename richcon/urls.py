from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from richcon import settings
from core import views
from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
