from django.urls import path

from .views import PerformanceDetailView, PerformanceListView, PerformanceView

urlpatterns = [
    path('performance/', PerformanceListView.as_view(), name='plan-list'), 
    path('performance/<int:id>/', PerformanceDetailView.as_view(), name='plan-detail'),
    path('performance/manage/', PerformanceView.as_view()),  
    path('performance/manage/<int:id>/', PerformanceView.as_view()),  
]
