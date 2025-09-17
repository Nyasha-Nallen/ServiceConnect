from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('provider_dashboard/', views.provider_dashboard, name="provider_dashboard"),
    path('customer_dashboard/', views.customer_dashboard, name="customer_dashboard"),

    #CATEGORY URLS (ADMIN ONLY)
    path('category/list/', views.list_category, name='list_category'),
    path('category/create/', views.create_category, name='create_category'),
    path('category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete_category'),

]