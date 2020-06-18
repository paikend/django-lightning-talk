import os
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta
from celery import shared_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule, SolarSchedule
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
def clocked_task_register(task_name, task_func, kwargs):
    """수행 로직을 clocked에 등록하는 로직"""
    date = datetime.now(timezone('Asia/Seoul')) + relativedelta(minutes=1)
    schedule, _ = ClockedSchedule.objects.create(clock_time = date)
    PeriodicTask.objects.create(
    clocked = schedule,
    name = task_name + str(datetime.now(timezone('Asia/Seoul'))),
    task = task_func,
    kwargs = kwargs,
    )

@shared_task
def interval_task_register(task_name, task_func, kwargs):
    """수행 로직을 interval에 등록하는 로직"""
    schedule, _ = IntervalSchedule.objects.create(
        every = 5,
        period = "days",
        )
    PeriodicTask.objects.create(
    interval = schedule,
    name = task_name + str(datetime.now(timezone('Asia/Seoul'))),
    task = task_func,
    kwargs = kwargs,
    )

@shared_task
def solar_task_register(task_name, task_func, kwargs, event = None, latitude = None, longtitude= None ):
    """수행 로직을 solar에 등록하는 로직"""
    schedule, _ = SolarSchedule.objects.create(
        event = event,
        latitude = latitude,
        longtitude = longtitude,
        )
    PeriodicTask.objects.create(
    solar = schedule,
    name = task_name + str(datetime.now(timezone('Asia/Seoul'))),
    task = task_func,
    kwargs = kwargs,
    )
