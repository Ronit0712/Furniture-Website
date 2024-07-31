"""
URL configuration for FurnitureProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from userApp import views

urlpatterns = [
    path('admin/', include('adminApp.admin_urls')),
    path('',views.home),
    path('living/',views.living),
    path('kitchen/',views.kitchen),
    path('bedroom/',views.bedroom),
    path('outdoor/',views.outdoor),
    path('cafe/',views.cafe),
    path('office/',views.office),
    path('others/',views.others),
    path('about_us/',views.about_us),
    path('blogs/',views.blogs),
    path('contact_us/',views.contact_us),
    path('save_contact/',views.save_contact)

]
