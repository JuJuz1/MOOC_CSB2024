from django.db import models
import uuid
import hashlib

class SecureData(models.Model):
    user_name = models.CharField(max_length=50)
    # FLAW: Software and data integrity failures
    # Two people can have the same data input
    # --> Duplicate primary key
    md5_hash = models.CharField(max_length=32, primary_key=True)
    # FIX:
    # Use a UUID as the primary key to ensure uniqueness
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Message(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    message = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.id = hashlib.sha256(self.message.encode()).hexdigest()
        super(Message, self).save(*args, **kwargs)