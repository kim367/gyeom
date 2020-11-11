from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# auth 를 import하는 이유는 아래에 auth.login을 사용하기 위함
from django.contrib import auth


# Create your views here.


def sign_up(request):
    context = {}

    # POST Method
    if request.method == 'POST':
        if (request.POST['username'] and
                request.POST['password'] and
                request.POST['password'] == request.POST['password_check']):
    # and 를 쓸때 if문을 ()로 감싸주지 않으면 동작을 안함
            new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )
    # User에 관한 class는 보안문제 때문에 .create_user라는 함수를 씀! *매우 중요!!
            auth.login(request, new_user)
            return redirect('posts:index')

        else:
            context['error'] = '아이디와 비밀번호를 다시 확인해줴요.'

    # GET Method
    return render(request, 'accounts/sign_up.html', context)


def login(request):
    context = {}

    # POST Method
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            # 사용자 인증에 관한 로직
            user = auth.authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password']
            )

            if user is not None:
                auth.login(request, user)
                return redirect('posts:index')
            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'

    # GET Method
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('posts:index')