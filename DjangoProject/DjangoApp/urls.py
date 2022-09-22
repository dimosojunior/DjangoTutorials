
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.about, name="about"),
    path('view_product/<int:id>/', views.view_product, name="view_product"),
    path('delete_product/<int:id>/', views.delete_product, name="delete_product"),
    path('add_product/', views.add_product, name="add_product"),
    path('update_product/<int:id>/', views.update_product, name="update_product"),
    
]