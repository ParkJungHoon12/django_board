from django.shortcuts import render, redirect
from .models import Author, Post
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
    return render(request, 'home.html')


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {'authors': authors})


def author_detail(request, my_id):
    author = Author.objects.get(id = my_id)
    return render(request, 'author/author_detail.html', {'author': author})


def author_update(request, my_id):
    author = Author.objects.get(id = my_id)
    if request.method == 'POST':     
        
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']

        author.name = my_name 
        author.email = my_email
        author.password = my_password
        author.save() 
       
        return redirect('/') 
    
    else: 
        return render(request, 'author/author_update.html', {'author': author})


def author_new(request):
     
     if request.method == 'POST':  
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']

        a1 = Author() 
        a1.name = my_name
        a1.email = my_email
        a1.password = my_password
        a1.save()

        return redirect('/') 
     
     else: 
        return render(request, 'author/author_new.html')


def post_list(request):
    # filter주고 값을 안주면 all과 일치
    # order_by 하고 -컬럼명 이렇게 주면 내림차순정렬
    posts = Post.objects.filter().order_by('-created_at')
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, my_id):
    post = Post.objects.get(id = my_id)
    return render(request, 'post/post_detail.html', {'post': post})


def post_update(request, my_id):
    post = Post.objects.get(id = my_id)
    if request.method == 'POST':         
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']

        post.title = my_title 
        post.contents = my_contents
        post.save() 
       
        return redirect('/') 
    
    else: 
        return render(request, 'post/post_update.html', {'post': post})
    

def post_new(request):    
     if request.method == 'POST':  
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']
        my_email = request.POST['my_email'] # 이메일 추가

        p1 = Post() 
        if my_email:
           try:
               p1.author  = Author.objects.get(email = my_email) 
           # {id:1. name"hong, email"aaa@aa ....} email = my_email인 db 행 1개의 전체값을 객체(p1.author)에 저장
           # 장고에서는 id값만 빼서 post db에 알아서 자동 저장함
    
           except Author.DoesNotExist:
               # HttpResponse : 200 정상
               # HttpResponseNotFound : 404 에러(사용자 오류)
               return HttpResponseNotFound("존재하지 않는 이메일입니다.")
          
        p1.title = my_title
        p1.contents = my_contents
        p1.save()

        return redirect('/') 
     
     else: 
        return render(request, 'post/post_new.html')