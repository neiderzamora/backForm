from django.db import models
import uuid

class Form(models.Model):

    TYPE_DOC_CHOICES = (
        ("TI", "TI"),
        ("CC", "CC"),
        ("CE", "CE")
    )

    GENDER_CHOICES = (
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino"),
        ("Otro", "Otro")
    )

    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=200)
    email =  models.EmailField()
    phone = models.CharField(max_length=15)
    type_doc = models.CharField(max_length=30)
    doc_number = models.CharField(max_length=30)
    occupation = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    terms_conditions = models.BooleanField(default=False)
    privacity = models.BooleanField(default=False)
    select_plan = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    