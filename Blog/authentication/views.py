from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import UserAuthenticationForm


def auth(request: HttpRequest):
    return HttpResponse("you are in the /auth route")


class AuthenticationView(FormView):
    template_name = "login.html"
    form_class = UserAuthenticationForm
    success_url = "/admin2"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if not form.is_valid():
            form.add_error(None, "Invalid username/password")
            return self.form_invalid(form)

        else:
            username = self.request.POST['username']
            password = self.request.POST['password']

            user = authenticate(username=username, password=password)
            print(f'{user=}')

            if not user:
                form.add_error(None, "Account doesn't exist")
                return self.form_invalid(form)

            login(self.request, user)

        return super().form_valid(form)


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("auth")
