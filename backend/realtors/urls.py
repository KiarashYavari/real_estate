from django.urls import path
from realtors.views import RealtorListView, RealtorView, TopSellerView


urlpatterns = [
    path('', RealtorListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', RealtorView.as_view()),
]
