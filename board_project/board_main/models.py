from django.db import models

# Create your models here.
# model.py 클래스와 DB의 table과 sync를 맞춰 테이블(컬럼정보) 자동생성.

# 클래스명 = 테이블명
# 클래스 변수 = 컬럼명
class Test(models.Model):
    name = models.CharField(max_length=20) #CharField == VARCHAR를 의미
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    