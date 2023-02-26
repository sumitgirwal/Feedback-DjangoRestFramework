from django.shortcuts import render
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework import generics

# Create your views here.
def index(request):
	template_name = 'index.html'
	context = {}
	return render(request, template_name, context)

class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackCreate(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

