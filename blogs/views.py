from django.shortcuts import render,redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import blog,likes,user_profile,notification
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.models import User
from .forms import PostForm,detailForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.paginator import Paginator
def homepage(request):
    if request.user.is_authenticated:
        l=likes.objects.all()
        b=blog.objects.all()
        bb=blog.objects.order_by("-pub_date")
        noti = notification.objects.filter(user=request.user)
        count=noti.count()
        k={}
        user = {}
        id=[0,]
        for i in b:
            n=i.id
            n=str(n)
            n=int(n)
            k[n] = int(0)
            id.append(n)
            list=[]
            for j in l:
                m=j.blog_id
                m=str(m)
                m=int(m)
                name=str(j.user)
            
                if m == n:
                    k[m] = k[m] + int(1)
                    list.append(name)
            user[n]=list
            
        return render(request,
                    template_name='blogs/home.html',
                    context = {"blogs":bb,"likes":k,"ids":id,"users":user,"notification":noti,"count":count}
                    )
    else:
        return render(request,template_name='blogs/home.html')
def register(request):
    if request.user.is_authenticated:
        return redirect('blogs:homepage')
    else:
        if request.method == "POST":
        
            form = NewUserForm(request.POST)
            if form.is_valid():
            
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"New acoount created successfully: {username}")
                login(request, user)
                return redirect("blogs:homepage")

            else:
                for msg in form.error_messages:
                    messages.error(request,f"{msg}: {form.error_messages[msg]}")

                return render(request = request,
                            template_name = "blogs/register.html",
                            context={"form":form})

        form =  NewUserForm
        return render(request = request,
                    template_name = "blogs/register.html",
                    context={"form":form})
def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect('blogs:homepage')
    else:
        return redirect('blogs:homepage')
    
def login_request(request):
    if request.user.is_authenticated:
        return redirect('blogs:homepage')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('/')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        return render(request = request,
                    template_name = "blogs/login.html",
                    context={"form":form})
def add_request(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST)
        if request.method == 'POST':
        
            if form.is_valid():
            
            
            
                post_item = form.save(commit=False)
                post_item.user = request.user
                post_item.save()
                
                return redirect("blogs:homepage")

                

            else:
                
                messages.error(request,f"some error occured")
                return render(request,
                            template_name = 'blogs/insert.html',
                            context={'form': form})
        return render(request,
                    template_name = 'blogs/insert.html',
                    context={'form': form})
    else:
        return redirect("blogs:login")

def users(request,user_name):
    return render(request,
                  template_name = "blogs/account.html",
                  context ={'users': User.objects.filter(username=request.user)}
                  )
def user(request,user_name):
    return render(request,
                  template_name = "blogs/profile.html",
                  context ={'users': User.objects.filter(username=user_name),'details': user_profile.objects.filter(user__in=User.objects.filter(username=user_name))}
                  )
def delete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            blog.objects.filter(id__in=request.POST.getlist('item')).delete()
            messages.info(request, "Blog deleted successfully!")
            return redirect("blogs:homepage")
        return render(request,
                    template_name = "blogs/delete.html",
                    context = {"blogs":blog.objects.filter(user=request.user).order_by("-pub_date")}
                    )
    else:
        return redirect("blogs:login")
def deletes(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            blog.objects.filter(id=pk).delete()
            messages.info(request, "Blog deleted successfully!")
            return redirect("blogs:homepage")
        return render(request,
                    template_name = "blogs/confirmdel.html"
                    )
    else:
        return redirect("blogs:login")
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = blog
    fields = ['title', 'content','back']
    template_name = 'blogs/updateblog.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == blog.user:
            return True
        return False
    def get_success_url(self):
        return "/"
def like(request,pk):
    if request.user.is_authenticated:
        titles = blog.objects.filter(id=pk).values('title')
        titles = titles[0]
        user =  blog.objects.filter(id=pk).values('user')
        user = user[0]['user']
        user =User.objects.filter(id=user)
        print(user)
        noti = notification.objects.get_or_create(user=user[0],notify=request.user.username+" has liked your blog "+titles['title'])
        lik = likes.objects.get_or_create(blog_id=blog.objects.get(id=pk),user=request.user)
        #lik.save()
        return redirect('blogs:homepage')
    else:
        return redirect('blogs:homepage')
def dislike(request,pk):
    if request.user.is_authenticated:
        likes.objects.filter(blog_id=blog.objects.get(id=pk),user=request.user).delete()
        return redirect('blogs:homepage')
    else:
        return redirect('blogs:homepage')
def likess(request,pk):
    if request.user.is_authenticated:
        bb=likes.objects.filter(blog_id=pk)
        users=user_profile.objects.all()
        return render(request,
                  template_name='blogs/likes.html',
                  context = {"blogs":bb,"uu":users}
                 )
    else:
        return redirect('blogs:homepage')

def update(request,user_name):
    if request.user.is_authenticated:
        instance = get_object_or_404(user_profile,user= request.user)
        print(request.FILES)

        form = detailForm(request.POST or None,request.FILES or None,instance=instance)
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()             
                return redirect("blogs:homepage")
            else:
                
                messages.error(request,f"some error occured")
                return render(request,
                            template_name = 'blogs/updatedetails.html',
                            context={'form': form,'title': instance.title,'instance':instance})
        return render(request,
                    template_name = 'blogs/updatedetails.html',
                    context={'form': form})
    else:
        return redirect("blogs:login")
def notify(request,pk):
    if request.user.is_authenticated:
          notification.objects.filter(id=pk).delete()
          return redirect("blogs:login")
    else:
        return redirect("blogs:login")


    
    