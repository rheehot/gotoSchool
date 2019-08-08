from django.contrib import admin
from .models import Member
from django.forms import CheckboxSelectMultiple
from django.db import models

# Register your models here.
# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('username', 'password', 'school', 'major', 'schoolId')
#     list_display_links = ('username', 'password')

admin.site.register(Member)

# @admin.register(InterestSchool)
# class InterestAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.ManyToManyField: {'widget': CheckboxSelectMultiple()},
#     }
    