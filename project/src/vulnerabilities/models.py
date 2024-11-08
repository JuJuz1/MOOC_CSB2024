from django.db import models
import hashlib

class SecureData(models.Model):
    user_name = models.CharField(max_length=50)
    # FLAW: Software and data integrity failures
    # Two people can have the same data input
    # --> Duplicate primary key
    md5_hash = models.CharField(max_length=32, primary_key=True)
    # FIX:
    # Use a secure hashing algorithm to generate a unique primary key
    # See Message class's overridden method save below
    #id = models.CharField(max_length=10, primary_key=True)

class Message(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    message = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.id = hashlib.sha256(self.message.encode()).hexdigest()
        super(Message, self).save(*args, **kwargs)