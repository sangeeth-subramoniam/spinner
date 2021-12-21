from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'threeplayers'
urlpatterns = [
    path('', views.threeplayers , name = "threeplayers"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)