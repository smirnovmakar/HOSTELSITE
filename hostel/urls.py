from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavn),
    path("reg", views.reg),
    path("vhod", views.vhod),
    path("bron", views.bron),
    path("room/<int:roomid>", views.rooms),
    path("nomera", views.nomera)
]
