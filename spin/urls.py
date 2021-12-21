from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'spin'
urlpatterns = [
    path('', views.spin , name = "spin"),
    path('getnames/<int:pk>', views.getnames , name = "getnames"),
    path('2/<ls>', views.twoplayers , name = "twoplayers"),
    path('3/<ls>', views.threeplayers , name = "threeplayers"),
    path('4/<ls>', views.fourplayers , name = "fourplayers"),
    path('5/<ls>', views.fiveplayers , name = "fiveplayers"),
    path('6/<ls>', views.sixplayers , name = "sixplayers"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)