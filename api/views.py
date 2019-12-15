from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from accounts.models import User
from api.serializers import MealsSerializer

class Page_list(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = MealsSerializer
