from django.http import JsonResponse
from config.tasks import hello_django
def test_view(request):
  hello_django.delay()
  return JsonResponse({"key": "value"})
