from django.urls import path
from . import views

urlpatterns = [

    path('schoolupdate/<int:s_review_id>', views.schoolupdate, name='schupdate'),
    path('schooldelete/<int:s_review_id>', views.schooldelete, name='schdelete'),
    path('reviewList', views.reviewlist, name='reviewList'),
    path('schoolnew', views.schoolnew, name='schnew'),
    path('schoolcreate', views.schoolcreate, name='schcreate'),
    path('schoolshow/<int:s_review_id>', views.schoolshow, name='schshow'),
    path('schooledit', views.schooledit, name='schedit'),

]