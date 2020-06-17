# 장고 라이트닝 토크 (16:30 ~ 16:50) 백경준 
## 아직도 보고서를 직접 보내시나요?(Feat.Django-celery-beat)  
***  

실습을 해보기 전에 공식 문서의 내용을 꼭 읽어보세요!  
> ## 공식 문서  
### celery
- http://docs.celeryproject.org/en/latest/  


### django-celery-beat
- https://django-celery-beat.readthedocs.io/en/latest/  


> ## 실습 환경
- python 3.8.2
- Redis server 5.0.5  


> ## requirements.txt
amqp==2.6.0  
asgiref==3.2.7  
billiard==3.6.3.0  
celery==4.4.5  
Django==3.0.7  
django-celery-beat==2.0.0  
django-timezone-field==4.0  
future==0.18.2  
kombu==4.6.10  
python-crontab==2.5.1  
pytz==2020.1  
redis==3.5.3  
sqlparse==0.3.1  
vine==1.3.0    


> ## 가상환경 생성
- $ python -m venv venv  


> ## 가상환경 활성화
 ### Linux & MAC
- $ source venv/bin/activate  
 ### Windows
- source venv\Scripts\activate.bat  


> ## packages 설치
 - (venv) $ pip install -r requirements.txt  


> ## 데이터 베이스migration 
 - (venv) $ python manage.py migrate  


> ## Django(WAS) 실행  
 - (venv) $ python manage.py runserver  


> ## Celery 실행
 - (venv) $ celery worker -A config -P --loglevel=INFO  


> ## Celery beat 실행 
 - (venv) $ celery beat -A config  --loglevel=INFO  



