from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .task import create_random_user_accounts

class GenerateRandomUserView(FormView):
    template_name = 'generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('show_all_user')

def show_all_user(request):
    all_user = User.objects.all()
    return render(request,"users.html",{'users' : all_user})