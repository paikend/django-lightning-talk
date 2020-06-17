import os
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta
from celery import shared_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule


@shared_task
def hello_django():
    print("hello django!")

@shared_task
def task_register(task_name, task_func, args, month, day, hour, minute):
    schedule, _ = CrontabSchedule.objects.get_or_create(
    minute=minute,
    hour=hour,
    day_of_week="*",
    day_of_month=day,
    month_of_year=month,
    )
    PeriodicTask.objects.create(
    crontab=schedule,
    name=task_name,
    task=task_dunc,
    kwargs=args,
    #1 month after discard task
    expires= datetime.now(timezone('Asia/Seoul')) + relativedelta(months=1),
    )