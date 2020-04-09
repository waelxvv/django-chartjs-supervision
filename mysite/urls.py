from django.contrib import admin
from django.urls import path

from mysite.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('supervision/', views.supervision, name='supervision'),
    path('admin/', admin.site.urls),
]
