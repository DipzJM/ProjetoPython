from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class MagicLinkToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def is_valid(self):
        # Define uma validade de, por exemplo, 10 minutos
        from django.utils import timezone
        from datetime import timedelta
        return not self.used and self.created_at >= timezone.now() - timedelta(minutes=10)