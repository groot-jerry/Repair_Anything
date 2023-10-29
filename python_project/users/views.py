# Create your views here.

'''class UserRegistrationView(View):
    template_name = 'users/registration.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = user.userprofile
            user_profile.role = 'user'
            user_profile.save()
            login(request, user)
            return redirect('product_selection')
        return render(request, self.template_name, {'form': form})
'''

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views import View


class UserLoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_selection')
        return render(request, self.template_name, {'error_message': 'Invalid login credentials'})


from django.http import HttpResponse
from django.shortcuts import render
from . import forms


def UserRegistrationView(request):
    if request.method == 'GET':
        form = forms.UserCreationForm(request.GET)

        if form.is_valid():
            form.save()

            return HttpResponse("User Created Successfully")

    else:
        form = forms.UserCreationForm()

    return render(request, 'users/registration.html', {
        'form': form
    })
