from django.shortcuts import render
from .models import Thing
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ThingSerializer

# Create your views here.
class ThingListView(ListCreateAPIView):

    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer