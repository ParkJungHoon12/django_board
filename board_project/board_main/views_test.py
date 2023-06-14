from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Test
# Create your views here.

# html 파일의 기본 경로는 templates/ (생략가능), 파일의 경로가 변경되면 경로를 지정해야함

# GET 요청시 html 파일을 그대로 return
def test_html(request):
    return render(request, 'test/test.html')

# GET 요청시 html + data return
def test_html_data(request):
    my_name = "hongindong"
    return render(request, 'test/test.html', {'name' : my_name})

# GET 요청시 html + multidata return
def test_html_multi_data(request):
     data = {
        'name': 'hongildong',
        'age': 20
    }  
     return render(request, 'test/test.html', {'data' : data })

# GET 요청시 data만 return
def test_json_data(request):
    data = {
        'name': 'hongildong',
        'age': 20
    }
    # render라는 의미는 web 개발에서 일반적으로 화면을 return 해줄때 사용되는 용어
    # Python의 dict와 유사한 json형태로 변환해서 return
    return JsonResponse(data)

# 사용자가 GET요청으로 데이터를 넣어올때
#         < 사용자가 GET요청으로 데이터를 넣어오는 방식 >
#  1) 쿼리파라미터 방식              
#     URL : http://localhost:8000/parameter_data?name=hong&email=hong@naver.com&password=1234
def test_html_parameter_data(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    password = request.GET.get('password')

    data  = {
        "name" : name,
        "email" : email,
        "password" : password 
        }
      
    return render(request, 'test/test.html', {'data' : data })

#  2) path variable 방식 (좀 더 현대적인 방식) 
#     URL : http://localhost:8000/parameter_data2/3
def test_html_parameter_data2(request, my_id):
    print(my_id)
      
    return render(request, 'test/test.html', {})


# FORM 태그를 이용한 POST(사용자로부터 값을 받는) 방식
#  GET요청 : 화면응답(HTML + 상태코드)
#  POST요청 : 응답코드
def test_post_handle(request):
    if request.method == 'POST':  # test_post_form.html에서 사용자 데이터 값을 받아서 처리해주는 method    
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        
        # DB에 insert -> save함수를 사용
        # DB의 테이블과 sync가 맞는 test클래스에서 객체를 만들어 save

        t1 = Test() # board_main/models.py에 사용자가 지정한 DB 클래스 Test의 객체 생성
        t1.name = my_name # 객체 변수에 POST로 받은 값을 저장
        t1.email = my_email
        t1.password = my_password
        t1.save() # 마지막에 save로 종료 
        return redirect('/') # localhost:8000/ 로 이동 
    
    else: # GET일시 화면을 rendering해주는 분기
        return render(request, 'test/test_post_form.html')
    

# DB값 1개만 조회 
# URL : http://localhost:8000/test_select_one/1
def test_select_one(request, my_id):
    # 단건만을 조회할때는 get함수를 사용
    t1 = Test.objects.get(id = my_id)
    return render( request, 'test/test_select_one.html', {'data' : t1 } )


# DB값 모두 조회 
# URL : http://localhost:8000/test_select_all/
def test_select_all(request):
    # 모든 data 조회시 select * from xxxx; all() 함수 사용
    tests = Test.objects.all()
    return render(request, 'test/test_select_all.html', {'datas': tests })


# where 조건으로 다건을 조회할 떄는 filter()함수 사용
# 쿼리파라미터 방식
# URL : http://localhost:8000/test_select_filter?name=park (select * from board_main_test where name = "park")
def test_select_filter(request):
    # 모든 data 조회시 select * from xxxx; all() 함수 사용
    my_name = request.GET.get('name')
    tests = Test.objects.filter(name = my_name)
    
    return render(request, 'test/test_select_filter.html', {'datas': tests })


# UPDATE를 하기 위해서는 해당건을 사전에 조회하기 위한 ID 값이 필요
# 메서드는 등록과 동일하게 save()함수 사용
def test_update(request):
    if request.method == 'POST':     

        my_id = request.POST['my_id']
        t1 = Test.objects.get(id = my_id)

        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']

        t1.name = my_name # 기존 DB 값을 사용자가 입력한 값으로 대체
        t1.email = my_email
        t1.password = my_password
        t1.save()  # save 함수는 신규 객체를 save하면 insert, 기존 객체를 save하면 update
        # 삭제는 delete() 함수 사용 : update와 마찬가지로 기존객체 조회후 delete()
        # t1.delete() 하면 삭제
        return redirect('/') 
    
    else: 
        return render(request, 'test/test_update.html')


