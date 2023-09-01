import uuid

from django.db import models



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class CodeBased(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract=True
