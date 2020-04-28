from django.shortcuts import render
from .models import Posts
from .forms import PostForm, PostSearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, Page
from django.views import View
from django.utils.decorators import method_decorator


class PostsView(View):
    template_name = 'pages/posts.html'
    search_form = PostSearchForm

    def get(self, request):
        name = request.GET.get('name', '')
        posts = Posts.objects.all().filter(name__contains=name)
        current_page = Paginator(posts, 10)
        page = request.GET.get('page')
        search_form = self.search_form(request.GET)
        try:
            posts_list = current_page.page(page)
        except PageNotAnInteger:
            posts_list = current_page.page(1)
        except EmptyPage:
            posts_list = current_page.page(current_page.num_pages)

        return render(request, self.template_name, {'page': page, 'posts': posts_list, 'form': search_form})


class UserPostsView(View):
    template_name = 'pages/user_posts.html'
    search_form = PostSearchForm

    @method_decorator(login_required)
    def get(self, request):
        print(request.user.id)
        posts = Posts.objects.all().filter(user=request.user.id)
        current_page = Paginator(posts, 10)
        page = request.GET.get('page')
        try:
            posts_list = current_page.page(page)
        except PageNotAnInteger:
            posts_list = current_page.page(1)
        except EmptyPage:
            posts_list = current_page.page(current_page.num_pages)

        return render(request, self.template_name, {'page': page, 'posts': posts_list})


def single_post(request, id):
    post = Posts.objects.get(pk=id)
    return render(request, 'pages/single_post.html', {'post': post})


@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Your post saved')
            
    else:
        post_form = PostForm()
    return render(request, 'pages/create_post.html', {
        'form': post_form,
    })


@login_required
def edit_post(request, id):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Your post saved')
    else:
        post = Posts.objects.get(pk=id)
        post_form = PostForm({'name': post.name, 'post': post.post})
    return render(request, 'pages/edit_post.html', {
        'form': post_form,
    })
