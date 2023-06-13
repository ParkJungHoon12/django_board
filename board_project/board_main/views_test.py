from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

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
        name = request.POST['my_name']
        email = request.POST['my_email']
        password = request.POST['my_password']
        
        print(name)
        print(email)
        print(password)
        
        return redirect('/') #localhost:8000/ 로 이동 
    
    else: # GET일시 화면을 rendering해주는 분기
        return render(request, 'test/test_post_form.html')