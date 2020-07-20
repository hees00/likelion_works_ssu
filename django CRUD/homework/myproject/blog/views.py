from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog,Food
from django.utils import timezone
from .forms import BlogUpdate
from django.core.paginator import Paginator
from faker import Faker

def fake(request):
    for i in range(10):
        blog=Blog()
        myfake = Faker()
        blog.title=myfake.name()
        blog.body=myfake.sentence()
        blog.pub_date=timezone.datetime.now()
        blog.save()
    return redirect('/')


def food(request):
    foods= Food.objects
    return render(request, 'food.html',{'foods':foods})

def blog(request):
    blogs= Blog.objects

    blog_list = Blog.objects.all()  
    paginator = Paginator(blog_list,10)  
    page= request.GET.get('page')
    articles= paginator.get_page(page)  
    return render(request, 'blog.html',{'blogs':blogs,'articles':articles})

def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def new(request):
    return render(request,'new.html')


def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+ str(blog.id))


def delete(request,blog_id):
    Blog.objects.get(id=blog_id).delete()
    return redirect('/')

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)
 
        return render(request,'update.html', {'form':form})



# Create your views here.
