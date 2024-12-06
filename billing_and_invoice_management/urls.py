from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BillListView, BillDetailView, BillingView, 
    InvoiceViewSet, PaymentViewSet, 
    PayPalPaymentView, PayPalExecuteView
)

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('billing/', BillListView.as_view(), name='billing-list'),  
    path('billing/<int:id>/', BillDetailView.as_view(), name='billing-detail'), 
    path('billing/manage/', BillingView.as_view(), name='billing-manage'), 
    path('', include(router.urls)), 
    path('payment/create/', PayPalPaymentView.as_view(), name='create-payment'),  
    path('payment/execute/', PayPalExecuteView.as_view(), name='execute-payment'),  
]
