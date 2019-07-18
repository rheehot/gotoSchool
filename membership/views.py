from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, DeleteAccountForm
from .models import Member
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)

        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['passwordCheck']:
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")

                newUser = Member.objects.create_user(username=username, email=None, password=password)
                
                newUser.school = form.cleaned_data.get("school")
                newUser.major = form.cleaned_data.get("major")
                newUser.schoolId = form.cleaned_data.get("schoolId")
                newUser.imgOfIdcard = form.cleaned_data.get("imgOfIdcard")
                newUser.save()

                login(request, newUser)
                return redirect('home')
            else:
                return render(request, 'signup.html', {'form': form, 'error': '비밀번호를 다시 확인해주십시오.'})
        
        else:
            return HttpResponse('이미 존재하는 아이디입니다. 다시 입력해주세요.')
    
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
            return HttpResponse("로그인 실패. 다시 시도해주세요.")
    
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
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
                    return redirect('home')
                else:
                    HttpResponse("회원 탈퇴 실패. 다시 시도해주세요.")

        except user.DoesNotExist:
            messages.error(request, "User does not exist")
            return render(request, 'home.html')

        except Exception as e:
            return render(request, 'home.html', {'err': print(e)})
    else:
        form = DeleteAccountForm()
        return render(request, 'deleteAccount.html', {'form': form})