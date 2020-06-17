from django.http import HttpResponse
from config.tasks import task_register
import json

# example api 
def test_view(request):

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
  name =  request.GET.get('name', 'django')
  kwargs = json.dumps({"name" : name})
  task_register.delay(task_name, task_func, kwargs, month, day, hour, minute)
  return HttpResponse("Hello "+name, status=200)
