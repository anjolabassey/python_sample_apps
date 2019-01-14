from django.urls import path
from . import views

urlpatterns = [
    path('', views.tokenized, name='tokenized'), #the path for our index view
    path('card_charge/', views.card_charge, name='card_charge'),  
    path('token_charge/', views.token_charge, name='token_charge'),
    # path('cancel_sub/', views.cancel_sub, name='cancel_sub'),
    # path('activate_sub/', views.activate_sub, name='activate_sub'),

]