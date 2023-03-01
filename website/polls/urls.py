"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [

    path('', views.loginPage, name='login'),
    path('user/', views.ViewUsers, name='user'),
    path('logout/', views.logoutUser, name='logout'),

    path('user/add-product', views.add_product, name='add_product'),
    path('user/add-store', views.add_store, name='add_store'),
    path('user/add-sales', views.add_sales, name='add_sales'),
    path('user/view-sales', views.view_sales, name='view_sales'),

    path('user/delete/<str:productid>', views.delete_product, name='delete'),
    path('user/update/<str:productid>', views.update_product, name='update'),

    path('user/delete-s/<str:storeid>', views.delete_store, name='delete-s'),
    path('user/update-s/<str:storeid>', views.update_store, name='update-s'),
    
    path('user/download', views.export_csv, name='download'),
]