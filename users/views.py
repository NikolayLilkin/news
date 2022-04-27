from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomerCreationForm
# Create your views here.
class SignUpView(CreateView):
    form_class = CustomerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'