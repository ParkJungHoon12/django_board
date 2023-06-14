from django.db import models

# Create your models here.
# model.py 클래스와 DB의 table과 sync를 맞춰 테이블(컬럼정보) 자동생성.

# 클래스명 = 테이블명
# 클래스 변수 = 컬럼명
class Test(models.Model):
    name = models.CharField(max_length=20) #CharField == VARCHAR를 의미
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)


class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    # DB설정에 default time stamp가 걸리는 것이 아닌, 장고가 현재시간을 db에 insert
    created_at = models.DateTimeField(auto_now_add=True) #만들어질때만 데이타가 입력
    updated_at = models.DateTimeField(auto_now=True) #변경사항이 나올떄만 데이타가 입력


class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #만들어질때만 데이타가 입력
    updated_at = models.DateTimeField(auto_now=True) #변경사항이 나올떄만 데이타가 입력
    # DB에는 fk를 설정한 변수명에 id를 붙게 된다.  
    # on_update = models.CASCADE, on_delete = models.CASCADE,
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null=True)

