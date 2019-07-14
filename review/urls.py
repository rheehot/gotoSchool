from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('show/<int:review_id>', views.show, name='show'),
    path('edit', views.edit, name='edit'),
    path('update/<int:review_id>', views.update, name='update'),
    path('delete/<int:review_id>', views.delete, name='delete'),
]