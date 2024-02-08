from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'type_doc', 'doc_number', 'occupation', 'gender', 'terms_conditions', 'privacity', 'created_at')
    list_filter = ('terms_conditions', 'full_name')
    search_fields = ('full_name', 'email', 'phone')

admin.site.register(Form,  FormAdmin)