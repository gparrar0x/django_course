from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request) -> HttpResponse:
    text_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'MyApp/index.html', context=text_dict)

def help(request) -> HttpResponse:
    my_dict = {'help_insert': "HELP PAGE"}
    return render(request, 'MyApp/help.html', context=my_dict)

def register(request):
    registered = False
    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileInfoForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'MyApp/registration.html', {'user_form': user_form, 
                                                        'profile_form': profile_form, 
                                                        'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not active")
        else:
            print("Someone tried to login and failed!")
            print("Username: %s and password %s" % (username, password))
            return HttpResponse("Invalid credentials")
    else:
        return render(request, 'MyApp/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")



# def users(request) -> HttpResponse:
#     users_list = User.objects.order_by('last_name')
#     users_dict = {'users': users_list}
#     return render(request, 'MyApp/users.html', context=users_dict)


# def sign_up(request):
#     form = forms.SignUp()

#     if request.method == 'POST':
#         form = forms.SignUp(request.POST)

#         if form.is_valid():
#             print("Validation Success!!")
#             print(
#                 "NAME: "+form.cleaned_data['first_name']+" "+form.cleaned_data['last_name'])
#             print("EMAIL: "+form.cleaned_data['email'])
#             new_user = form.save(commit=True)
#             return index(request)
#         else:
#             print('Failed form validation')

#     return render(request, 'MyApp/users.html', context={'form': form})


# def relative(request):
#     return render(request, 'MyApp/relative_url_template.html')
