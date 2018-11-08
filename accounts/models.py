from importlib import import_module
from django.conf import settings
from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.mail import send_mail


SessionStore=import_module(settings.SESSION_ENGINE).SessionStore

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


def on_send_mail(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)

        send_mail(
            '가입 인사',
            '가입을 환영합니다.',
            'purum01@naver.com',
            [user.email],
            fail_silently=False,
        )

post_save.connect(on_send_mail, sender=settings.AUTH_USER_MODEL)

class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    session_key = models.CharField(max_length=40, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

def block_duplicate_logins(sender, request, user, **kwargs):
    for user_session in UserSession.objects.filter(user=user):
        session_key = user_session.session_key
        session = SessionStore(session_key)
        # session.delete()
        session['blocked'] = True
        session.save()

    session_key = request.session.session_key
    UserSession.objects.create(user=user, session_key=session_key)

user_logged_in.connect(block_duplicate_logins)