from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


#from allauth.socialaccount.models import SocialApp
#from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import SignupForm

def signup(request):
    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup_form.html',{'form':form})
   

def profile(request):
    return render(request, 'accounts/profile.html')


class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')
    template_name = 'accounts/password_change_form.html'
    
    def form_valid(self, form):
        messages.info(self.request, '암호 변경을 완료했습니다.')
        return super().form_valid(form)
    

class MyPasswordResetView(PasswordResetView):
    pass

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    pass


# def login(request):
#     providers = []
#     for provider in get_providers():
#         try:
#             provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
#             print(provider.social_app)
#         except SocialApp.DoesNotExist:
#             provider.social_app = None
#         providers.append(provider)

#     return LoginView.as_view(template_name='accounts/login_form.html', extra_context={'providers':providers})(request)