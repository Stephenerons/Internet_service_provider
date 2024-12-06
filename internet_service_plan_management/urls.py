from django.urls import path

from .views import PlanListView, PlanViews,PlanDetailView

urlpatterns = [
    path('plans/', PlanListView.as_view(), name='plan-list'), 
    path('plans/<int:id>/', PlanDetailView.as_view(), name='plan-detail'),
    path('plans/manage/', PlanViews.as_view()),  
    path('plans/manage/<int:id>/', PlanViews.as_view()),  
]
