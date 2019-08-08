from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator 
from .models import Blog
from django.db.models import Q
<<<<<<< HEAD
from .form import NewBlog
from django.contrib import admin
=======

>>>>>>> ef4964117f88841f51b978ea61574413e983e81f
# Create your views here.
def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request,'home.html',{'blogs':blogs,'posts':posts})

def new(request):
    return render(request, 'new.html')

def detail(request, blog_id):
    details= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})
   
def create(request):
<<<<<<< HEAD
        if request.method == 'POST':
                form = NewBlog(request.POST)
                if form.is_valid:
                        post = form.save(commit=False)
                        post.pub_date = timezone.now()
                        post.save()
                        return redirect('home')
                         
 
        else:
                form = NewBlog()
                return render(request, 'new.html', {'form':form})
        #print(request)blog= Blog() blog.title = request.POST.get('title','') blog.body = request.POST.get('body','')blog.pub_date = timezone.datetime.now()blog.save()return redirect('/blog/' + str(blog_id))    
=======
        print(request)
        blog= Blog()
        blog.title = request.POST.get('title','')
        blog.body = request.POST.get('body','')
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog_id))    
>>>>>>> ef4964117f88841f51b978ea61574413e983e81f

def mypage(request):
    return render(request, 'mypage.html')

def mypage2(request):
    return render(request, 'mypage2.html')

def nono(request):
    return render(request, 'nono.html')
 
def index(request):
    return render(request, 'index.html')

def search(request):
        schWord= '%s' % request.POST['search_word']
        post_list= Blog.objects.filter(Q(title__icontains=schWord) |
                Q(body__icontains=schWord)).distinct()

        context={}
        context['search_term']=schWord
        context['object_list']=post_list

        return render(request, 'post_search.html', context)

def inform(request):
    return render(request, 'inform.html')

<<<<<<< HEAD
def delete(request,pk):
        blog = get_object_or_404(Blog, pk= pk)
        blog.delete()
        return redirect('home')

def update(request,pk):
        #블로그 객체 가져오기
        blog = get_object_or_404(Blog, pk=pk)
        #해당하는 블로그 객체 pk 에 맞는 입력공간
        form = NewBlog(request.POST, instance= blog)

        if form.is_valid():
                form.save()
                return redirect('home')

        return render(request,'new.html', {'form':form})
    
=======
def edit(request):
        return render(request, 'edit_blog.html')
    #post = get_object_or_404(Post, pk=blog_id)
    #post.delete()
    #return redirect('edit_blog.html')

def remove(request):
        return render(request, 'remove_blog.html')
    #post = get_object_or_404(Post, pk=blog_id)
>>>>>>> ef4964117f88841f51b978ea61574413e983e81f
    #post.delete()
    #return redirect('remove_blog.html')