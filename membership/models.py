from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Member(AbstractUser):
    school = models.CharField(max_length=50)
    major = models.CharField(max_length=50, null=True, blank=True)
    schoolId = models.CharField(max_length=50)
    imgOfIdcard = models.ImageField(upload_to='user/', null=True)
    #interest = models.(choices=INTEREST_SCHOOL)

    def __str__(self):
        return self.username

