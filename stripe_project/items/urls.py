from django.urls import path

from . import views


urlpatterns = [
    path('buy/<int:item_id>/', views.create_checkout_session, name='create-checkout-session'),
    path('item/<int:item_id>/', views.item_detail, name='item-detail'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]
