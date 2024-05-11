from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_products, name="product_list"),
    path('', views.home, name="home"),
    path('add_produit/', views.add_product, name="add_product"),
    path('delete_product/<int:product_id>/',
         views.delete_product, name="delete_product"),
    path('update_product/<int:product_id>/',
         views.update_product, name='update_product'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login')
]
