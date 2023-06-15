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
    email = models.CharField(max_length=50, unique = True)
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

    # DB의 author_id는 파이썬(장고)에서는 author객체와 같은 것이다.
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null=True, related_name = 'posts')
    # Post는 객체 생성시 Author객체를 자동 생성하기 때문에 코드에서 값을 참조 가능하지만
    # Author는 객체 생성시 Post값을 참조하기 어렵다.(예로 작가 1명당 몇개의 글을 썼는지)
    # 이럴떄는 위 문구처럼 author의 파라미터로 이름을 지정 related_name = 'posts'해서 외부에서 참조 가능함
    # (장고에서 지원하는 기능임으로 이해하면 됨)