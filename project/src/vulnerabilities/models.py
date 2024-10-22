from django.db import models

class SecureData(models.Model):
    user_name = models.CharField(max_length=50)
    md5_hash = models.CharField(max_length=32, primary_key=True)