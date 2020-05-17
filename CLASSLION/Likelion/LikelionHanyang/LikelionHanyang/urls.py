from django.contrib import admin
from django.urls import path
import introduce.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', introduce.views.home, name="home"),
]
