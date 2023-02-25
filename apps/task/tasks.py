from django.conf import settings
from django.core.mail import send_mail

from classroom.celery import app


@app.task
def send_comment(email,username,text,to_user):

    send_mail(
    f'Hello! {to_user}',
    f'FROM:{username}:\n\n{text}',
    # settings.EMAIL_HOST_USER,
    'zarinakudajberdikyzy@gmail.com',
    [email],
    fail_silently=False,
    
)