from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from test_yourself.models import UserProfile
from friendship.models import Friend, Follow, Block


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('/accounts/login/')
    else:
        return render(request, 'accounts/login.html' )

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        profile_photo = request.FILES.get('profile_picture')

        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,"Username is already taken")
               return redirect('/accounts/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken")
                return redirect('/accounts/register/')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                Profile = User.objects.get(username=username)
                Extended_User = UserProfile.objects.create(user=Profile, ProfilePhoto=profile_photo)
                Extended_User.save();
                return redirect('/accounts/login/')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('/accounts/register/')

        return redirect('/')

    else:
        return render(request,'accounts/register.html',)


def logout(request):
    auth.logout(request)
    return redirect('/')


def user_profile(request):
    friend_list = Friend.objects.friends(request.user)
    all_users = User.objects.all().exclude(is_superuser = True)
    total_friends = len(friend_list)
    params = {
        'friends':friend_list,
        'total_friends':total_friends,
        'all_users':all_users,
    }
    return render(request, 'accounts/profile2.html',params)