#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
