from django.http import HttpResponse
from config.tasks import task_register
import json

def test_view(request):
  name =  request.GET.get('name', 'django')
  task_name = "hello"
  task_func = 'config.tasks.hello_django'
  kwargs = json.dumps({"name" : name})
  month = "*"
  day = "*"
  hour = "*"
  minute = "*"
  task_register.delay(task_name, task_func, kwargs, month, day, hour, minute)
  return HttpResponse("Hello "+name, status=200)
