from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
    path('buy/<int:item_id>/',views.buy_view)
]