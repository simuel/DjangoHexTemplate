import uuid
from django.db import models

class {{app_name.capitalize}}Model(models.Model):
    # Modelo para la entidad Customer
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)