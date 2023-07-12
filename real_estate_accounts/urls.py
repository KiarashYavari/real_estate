from django.urls import path
from real_estate_accounts import views

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
]
