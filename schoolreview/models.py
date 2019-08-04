from django.db import models
# Create your models here.
class SchoolReview(models.Model):
    school = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)
    date = models.DateField(null=True)
  
    def __str__(self):
        return self.school
    
    def summary(self):
        return self.content[:100]
