from __future__ import absolute_import

# 장고에 shared_task 경로 등록
from .celery import app as celery_app
__all__ = ['celery_app']
