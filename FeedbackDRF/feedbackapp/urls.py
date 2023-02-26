from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/feedbacks/', views.FeedbackList.as_view(), name='feedback_list'),
    path('api/feedbacks/create', views.FeedbackCreate.as_view(), name='feedback_create'),
]
