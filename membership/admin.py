from django.contrib import admin
from .models import Member

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'school', 'major', 'schoolId')
    list_display_links = ('username', 'password')

    