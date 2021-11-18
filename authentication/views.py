import logging
from django.contrib.auth.models import User
from wallets.models import UserBalance
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from wallets.btcgate import gen_address
from .forms import LoginForm, SignUpForm
from django.shortcuts import render


def login_view(request):
    form = LoginForm(request.POST)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            raw_password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_wallet = str(request.user)
            address = gen_address(user_wallet)
            logging.info('Есть кошелек для юзера')
            un = UserBalance(username_id=request.user.id)
            un.user_balance = 0
            un.wallet = address
            un.save()
            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect("/home/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

# class RegisterUsers(FormView):
#     template_name = 'accounts/register.html'
#     form_class = SignUpForm
#     success_url = '/home/'

#     def get(self, request, *args, **kwargs):
#         form = SignUpForm
#         return render(request, self.template_name, {'form': form})

#     def f(self, form, request):
#         user_wallet = str(request.user)
#         address = gen_address(user_wallet)
#         logging.info('Есть кошелек для юзера')
#         UserBalance.objects.update(username_id=request.user.id, user_balance=0, wallet=address)

#         return super().form_valid(form)
