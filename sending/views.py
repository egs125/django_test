from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def users(request):
  totalUsers = User.objects.all()
  serializer = UserSerializer(totalUsers, many=True)
  return Response(serializer.data)