from django.http import JsonResponse
from config.tasks import task_register, hello_django
import random 

def test_view(request):
  task_name = "hello_django" + str(random.random()*100)
  task_register.delay(str(q.video.title)+str(datetime.now()), 'config.tasks.hello_django', args_list, month, day, hour, minute)
  return JsonResponse({"key": "value"})
