from django.urls import path

from .views import CustomerView,SubscriptionListView,SubscriptionDetailView

urlpatterns = [
    path('subscribe/', SubscriptionListView.as_view(), name='customer-list'), 
    path('subscribe/<int:id>/',  SubscriptionDetailView.as_view(), name='customer-detail'),
    path('subscribe/manage/',  CustomerView.as_view()),  
    path('subscribe/manage/<int:id>/',  CustomerView.as_view()),  
]
