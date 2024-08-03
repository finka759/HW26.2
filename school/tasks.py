from datetime import datetime, timezone, timedelta

import pytz
from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from school.models import Subscription, Course
from users.models import User


@shared_task
def privet(pk):
    course = Course.objects.get(pk=pk)
    subscriptions = Subscription.objects.filter(course=pk, )
    email_list = []
    if subscriptions:
        for sub in subscriptions:
            email_list.append(sub.user.email)
        if len(email_list) > 0:
            send_mail(
                subject=f"Курс '{course.name}' был обновлен.",
                message=f"В программе курса '{course.name}' произошли изменения.",
                from_email=EMAIL_HOST_USER,
                recipient_list=email_list,
            )


@shared_task
def check_how_long_ago_logined_user():
    active_users = User.objects.filter(is_active=True)
    now = datetime.now(timezone.utc)
    for user in active_users:
        if user.last_login:
            if now - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
                print(f"Пользователь {user} заблокирован по истечении 30 дней")
