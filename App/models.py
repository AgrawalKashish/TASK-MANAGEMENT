from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#title
#description
#deadline
#status
#date
#updation
#user
#user_email

class TODO(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    status_choices= {
        ('c', 'COMPLETED'),
        ('p', 'PENDING'),
    }
    status = models.CharField(max_length=2, choices = status_choices )
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(max_length =6)
    updation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)