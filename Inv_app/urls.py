from django.urls import path,include
from .views import HomeView, ItemView,DeleteItemView,UpdateItemView,CreateItemView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('inventario/', ItemView.as_view(), name='inventario'),
    path('delete_item/<int:pk>/', DeleteItemView.as_view(), name='delete_item'),
    path('update_item/<int:pk>/', UpdateItemView.as_view(), name='update_item'),
    path('create_item/', CreateItemView.as_view(), name='create_item'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]