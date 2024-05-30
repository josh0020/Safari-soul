from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView # LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Redirect to the login page after successful registration
        return response

class CustomLoginView(LoginView):
    template_name = 'accounts/login_logout.html'
    authentication_form = AuthenticationForm
    
    def get_success_url(self):
        # Redirect to the index URL after successful login
        return reverse_lazy('index')

