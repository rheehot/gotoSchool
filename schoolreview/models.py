from django.db import models
from django.conf import settings

# Create your models here.
class SchoolReview(models.Model):
    UNIVS = [(univ, univ) for univ in ('숙명여자대학교','성신여자대학교','서울대학교','한국산업기술대학교','건국대학교')]
    YEARS = [(year, year) for year in (2018,2019)]
    SEMESTERS = [(semester, semester) for semester in ('1학기','여름학기','2학기','겨울학기')]
    
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)
    school = models.TextField(choices=UNIVS, default='숙명여자대학교')
    schoolyear = models.IntegerField(choices=YEARS, default='2019') #수강학기(년도)
    schoolsemester = models.TextField(choices=SEMESTERS, default='1학기') #수강학기(학기)
    content = models.TextField(null=True, blank=True)
    #date = models.DateField(null=True)
  
    def __str__(self):
        return self.school
    
    def summary(self):
        return self.content[:50]
