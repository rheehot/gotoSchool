from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('../', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('remove_account/', views.deleteAccount, name='deleteAccount'),
    path('mypage/', views.mypage, name='mypage'),
    path('manage/password/change', views.changePassword, name='changePassword'),
    path('mypage/myposts/', views.myposts, name='myposts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)