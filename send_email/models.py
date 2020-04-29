from django.db import models
from tinymce import models as tinymce_models
# Create your models here.
class Email(models.Model):
    subject = models.CharField(max_length=120)
    body = tinymce_models.HTMLField()
    to = models.EmailField()