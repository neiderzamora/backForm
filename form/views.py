from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from .models import Form
from .email import *
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

            full_name = serializer.validated_data['full_name']
            phone = serializer.validated_data['phone']
            email = serializer.validated_data['email']
            type_doc = serializer.validated_data['type_doc']
            doc_number = serializer.validated_data['doc_number']
            occupation = serializer.validated_data['occupation']
            gender = serializer.validated_data['gender']
            select_plan = serializer.validated_data['select_plan']
            
            send_confirmation_email(full_name, phone, email, type_doc, doc_number, occupation, gender, select_plan)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
