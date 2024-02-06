from .models import Form
from rest_framework import serializers

class FormSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%e %H:%M', read_only=True)

    class Meta:
        model = Form
        fields = '__all__'
        read_only_field = ['id', 'created_at']