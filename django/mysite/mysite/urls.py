"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
from django.urls import path
from hello import views

urlpatterns = [
    path("discriminant/", views.disc_page),
    path("calc_discriminant/", views.calc_discriminant),
]
"""
from django.urls import path
from hello import views

urlpatterns = [
    path("sum/", views.sum_page),
    path("calc_sum/", views.calc_sum),
]