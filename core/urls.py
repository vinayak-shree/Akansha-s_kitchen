"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from vege.views import *


# Ratna pdega
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("",home , name="home"),
    path('admin/', admin.site.urls),
    path('all_recepies/' , all_recepies , name="all_recepies"),
    path('add_recepies/', add_recepies , name="add_recepies"),
    path('aboutt/' , aboutt , name="aboutt"),
    path('contact/' , contact , name="contact"),
    path('home/', home , name="home"),
    path('category_recepie/' , category_recepie , name = "category_recepie"),
    path('recepie_ingredients/<int:id>' , recepie_ingredients , name = "recepie_ingredients"),
     path('category/<str:category>/',category_recepie,name='category_recepie'),
     path('delete_recepie/<int:id>/' , delete_recepie , name="delete_recepie"),
     path('adminUser/' , adminUser , name = 'adminUser'),
    path('admin_login/' , admin_login , name = 'admin_login'),
#  path('dashboard/', dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('update_recepies/<int:id>/' , update_recepies , name="update_recepies")
    # urls.py
# path('recipe_in/<int:id>/', views.recipe_detail, name='recipe_detail')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()