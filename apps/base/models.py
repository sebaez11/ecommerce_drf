from email.policy import default
from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    delete_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'