import os
from datetime import datetime
from celery import shared_task

@shared_task
def hello_django():
    print("hello django!")


