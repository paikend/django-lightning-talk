import os
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta
from celery import shared_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule, SolarSchedule, ClockedSchedule
# 업무 로직
@shared_task
def hello_django(name):
    print("hello " + name)

@shared_task
def crontab_task_register(task_name, task_func, kwargs, month, day, hour, minute):
    """수행 로직을 crontab에 등록하는 로직"""
    schedule, _ = CrontabSchedule.objects.get_or_create(
    minute = minute,
    hour = hour,
    day_of_week = "*",
    day_of_month = day,
    month_of_year = month,
    timezone = 'Asia/Seoul'
    )
    PeriodicTask.objects.create(
    crontab = schedule,
    name = task_name + str(datetime.now(timezone('Asia/Seoul'))),
    task = task_func,
    kwargs = kwargs,
    expires = datetime.now(timezone('Asia/Seoul')) + relativedelta(months=1),
    )

@shared_task
def clocked_task_register(task_name, task_func, kwargs, date):
    """수행 로직을 clocked에 등록하는 로직"""
    schedule, _ = ClockedSchedule.objects.get_or_create(clocked_time = date)
    PeriodicTask.objects.create(
    clocked = schedule,
    name = task_name + str(datetime.now(timezone('Asia/Seoul'))),
    one_off=True,
    task = task_func,
    kwargs = kwargs,
    )

@shared_task
def interval_task_register(task_name, task_func, kwargs, every, period):
    """수행 로직을 interval에 등록하는 로직"""
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every = every,
        period = period,
        )
    PeriodicTask.objects.create(
    interval = schedule,
    name = task_name + str(datetime.now(timezone('Asia/Seoul'))),
    task = task_func,
    kwargs = kwargs,
    )

@shared_task
def solar_task_register(task_name, task_func, kwargs, event, latitude, longitude):
    """수행 로직을 solar에 등록하는 로직"""
    schedule, _ = SolarSchedule.objects.get_or_create(
        event = event,
        latitude = latitude,
        longitude = longitude,
        )
    PeriodicTask.objects.create(
    solar = schedule,
    name = task_name + str(datetime.now(timezone('Asia/Seoul'))),
    task = task_func,
    kwargs = kwargs,
    )
