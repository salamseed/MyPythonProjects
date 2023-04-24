from django.urls import path

from . import views
app_name = 'ecommerceapp'
urlpatterns = [
    path('', views.AllCategories, name='AllCategories'),
    path('<slug:c_slug>/',views.AllCategories,name='product'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProductDetails,name='ProductDetails'),
]