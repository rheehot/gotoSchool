from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

# Create your models here.
# class InterestSchool(models.Model):
#     INTEREST_SCHOOL=[
#         (1, '건국대학교'),
#         (2, '서울대학교'),
#         (3, '성신여자대학교'),
#         (4, '숙명여자대학교'),
#         (5, '한국산업기술대학교')]
    
#     interestin = models.IntegerField(null=True, choices=INTEREST_SCHOOL)

#     objects = models.Manager()

#     def __str__(self):
#         choices_dict = dict(INTEREST_SCHOOL)
#         return choices_dict[self.interestin]

class Member(AbstractUser):

    SCHOOL_CHOICES = [
        (1, '건국대학교'),
        (2, '서울대학교'),
        (3, '성신여자대학교'),
        (4, '숙명여자대학교'),
        (5, '한국산업기술대학교'),
    ]
    
    INTEREST_SCHOOL=(
        (1, '건국대학교'),
        (2, '서울대학교'),
        (3, '성신여자대학교'),
        (4, '숙명여자대학교'),
        (5, '한국산업기술대학교')
    )

    school = models.IntegerField(choices=SCHOOL_CHOICES, default=SCHOOL_CHOICES[0][0])
    major = models.CharField(max_length=50, null=True, blank=True)
    schoolId = models.CharField(max_length=50)
    imgOfIdcard = models.ImageField(upload_to='user/', null=True)

    interest = MultiSelectField(choices=INTEREST_SCHOOL, max_choices=5, default=INTEREST_SCHOOL[3][0])


    def __str__(self):
        return self.username

