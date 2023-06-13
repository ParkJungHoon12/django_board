from django.urls import path
from . import views_test

urlpatterns = [
   path('', views_test.test_html_multi_data),  # 브라우저에 http://localhost:8000/ 를 입력시, views_test.py 파일의 test_html_multi_data 모듈 호출
   path('test_json', views_test.test_json_data), # 브라우저에 http://localhost:8000/test_json 를 입력시, views_test.py 파일의 test_html_multi_data 모듈 호출
   path('parameter_data', views_test.test_html_parameter_data),
   path('parameter_data2/<int:my_id>', views_test.test_html_parameter_data2),
   path('test_post_handle', views_test.test_post_handle),
]