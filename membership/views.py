from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, DeleteAccountForm, ChangePasswordForm
from .models import Member
from review.models import Review
from schoolreview.models import SchoolReview
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.template import RequestContext


# Create your views here.
def home(request):
    return render(request,  '../index.html')


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)

        if form.is_valid():
            
            if form.cleaned_data['password'] == form.cleaned_data['passwordCheck']:
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                
                newUser = form.save(commit=False)
                newUser = Member.objects.create_user(username=username, email=None, password=password)
                
                newUser.school = form.cleaned_data.get("school")
                newUser.major = form.cleaned_data.get("major")
                newUser.schoolId = form.cleaned_data.get("schoolId")
                newUser.imgOfIdcard = form.cleaned_data.get("imgOfIdcard")
                newUser.interest = form.cleaned_data.get("interest")
                    
                newUser.save()
                form.save_m2m()

                login(request, newUser)
                messages.info(request, '회원이 되어주셔서 감사합니다. WelCome ~ :)')
                return redirect('mypage')
            else:
                return render(request, 'signup.html', {'form': form, 'error': '비밀번호를 다시 확인해주십시오.'}, context_instance=RequestContext(request))
        
        else:
            messages.error(request, '이미 존재하는 아이디이거나 회원가입에 실패했습니다. 다시 입력해주세요 :)')
            return redirect('signup')
    
    else:
        form = CreateUserForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else: 
            return render_to_response('login.html', {'message': '로그인에 실패했습니다. 다시 시도해주세요 :(', 'form': form})
    
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('')
    return render(request, 'signup.html')


@csrf_exempt
@login_required(login_url='http://127.0.0.1:8000/membership/login/')
def deleteAccount(request):
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)

        try:
            if form.is_valid():
                user = Member.objects.get(username=form.cleaned_data['username'])

                if user is not None:
                    user.delete()
                    return redirect('signin')

        except Exception as e:
            messages.error(request, '아이디를 잘못 입력하셨습니다. 회원 탈퇴에 실패했습니다.')
            return redirect('deleteAccount')
    else:
        form = DeleteAccountForm()
        return render(request, 'deleteAccount.html', {'form': form})


def mypage(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    information = Member.objects.filter(username=request.user)

    return render(request, 'mypage.html', {'information': information})


def myposts(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    myschoolreview = SchoolReview.objects.filter(writer=request.user)
    myreview = Review.objects.filter(writer=request.user)

    return render(request, 'myposts.html', {'myschoolreview': myschoolreview, 'myreview': myreview})


def changePassword(request):

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid() :
            user = request.user
            currentPassword = request.POST['currentPassword']

            if check_password(currentPassword, user.password):
                newPassword = request.POST['newPassword']
                passwordCheck = request.POST['newPasswordCheck']

                if newPassword == passwordCheck:
                    user.set_password(newPassword)
                    user.save()
                    auth.login(request, user)
                    return redirect('mypage')
                else:
                    messages.error(request, '새로운 비밀번호가 서로 일치하지 않습니다. ')
                    return redirect('changePassword')
            
            else:
                messages.error(request, '현재 비밀번호가 일치하지 않습니다.')
                return redirect('changePassword')

    else:
        form = ChangePasswordForm()
        return render(request, 'changePassword.html', {'form': form})
    