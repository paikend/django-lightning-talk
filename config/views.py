from django.http import HttpResponse
from config.tasks import \
  crontab_task_register, clocked_task_register, \
  solar_task_register, interval_task_register
import json
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta
# example api 
def hello_crontab_view(request):  
  """
  crontab task view
  """
  # 스케줄링할 시간 입력 (*은 모든 값에 적용)
  month = request.GET.get('month', '*')
  day = request.GET.get('day', '*')
  hour =request.GET.get('hour', '*')
  minute = request.GET.get('minute', '*')
  # task의  short description 
  task_name = request.GET.get('task_name', 'hello')
  # celery에 등록한 task
  task_func = request.GET.get('task_func', 'config.tasks.hello_django')
  # def hello_django(name)의 파라미터
  name =  request.GET.get('name', 'crontab_django')
  kwargs = json.dumps({"name" : name})
  crontab_task_register.delay(task_name, task_func, kwargs, month, day, hour, minute)
  return HttpResponse("Hello "+name, status=200)

def hello_clocked_view(request):
  """
  clocked task view
  """
  task_name = request.GET.get('task_name', 'hello')
  task_func = request.GET.get('task_func', 'config.tasks.hello_django')
  name =  request.GET.get('name', 'clocked_django')
  kwargs = json.dumps({"name" : name})
  date = datetime.now(timezone('Asia/Seoul')) + relativedelta(minutes=1)

  clocked_task_register.delay(task_name, task_func, kwargs, date)
  return HttpResponse("Hello "+name, status=200)

def hello_interval_view(request):
  """
  interval task view
  """
  task_name = request.GET.get('task_name', 'hello')
  task_func = request.GET.get('task_func', 'config.tasks.hello_django')
  name =  request.GET.get('name', 'interval_django')
  kwargs = json.dumps({"name" : name})
  interval_task_register.delay(task_name, task_func, kwargs, every = 3, period = "days")
  return HttpResponse("Hello "+name, status=200 )

def hello_solar_view(request):
  """
  solar task view
  서울특별시 강남구 역삼동 테헤란로16길 13 동원빌딩(강남일등파티룸스터디룸)
  37.498837, 127.034077
  """
  task_name = request.GET.get('task_name', 'hello')
  task_func = request.GET.get('task_func', 'config.tasks.hello_django')
  name =  request.GET.get('name', 'solar_django')
  kwargs = json.dumps({"name" : name})
  solar_task_register.delay(task_name, task_func, kwargs, event = "sunset", latitude=37.498837, longitude=127.034077 )
  return HttpResponse("Hello "+name, status=200)