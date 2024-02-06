from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from .models import Form
from .serializers import FormSerializer
from datetime import datetime, time, timedelta

from django.http import HttpResponse

class FormList(APIView):
    def get(self, request):
        form = Form.objects.all()
        serializer = FormSerializer(form, many=True)
        return Response(serializer.data)

class FormCreate(APIView):
    def post(self, request):
        serializer =  FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
