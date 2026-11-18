from django.urls import path
from hello import views

urlpatterns = [
    path("discriminant/", views.disc_page),
    path("calc_discriminant/", views.calc_discriminant),
]