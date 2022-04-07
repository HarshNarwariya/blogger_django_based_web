from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import CommentForm
from taggit.models import Tag
from .models import Post, Comment
from taggit.models import Tag #import at top

def post_list(request, tag_slug=None):
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])
        print(tag, posts)
    return render(request,'blog/posts_by_tag.html',{'posts':posts, 'tag':tag})



def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[post.slug]))



def index(request):
    posts = Post.objects.order_by('?')[:6]
    recent_posts_list = Post.objects.order_by('-date_posted')[:10]
    recent_posts = recent_posts_list[:3]
    most_viewed_posts = Post.objects.order_by('-views')[:10]
    tags = Tag.objects.all()[:30]
    return render(request, template_name='blog/home.html', context={
        'posts': posts,
        'recent_posts': recent_posts,
        'recent_posts_list': recent_posts_list,
        'most_viewed_posts': most_viewed_posts,
        'tags': tags,
    })

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6 


class CurrUserPostListView(ListView):
    model = Post
    template_name = 'blog/curr_user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Post.objects.filter(author=user).order_by('-date_posted')

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # stuff = get_object_or_404(Post, slug=kwargs.slug)
        context = super().get_context_data(**kwargs)
        obj = kwargs.get('object')
        likes = obj.likes
        liked = False
        if likes.filter(id=self.request.user.id):
            liked = True

        comments = obj.comments.all()[:4]
        context['comments'] = comments
        context['liked'] = liked
        return context

    def get(self, request, *args, **kwargs):
        obj = self.get_object() 
        obj.views += 1
        obj.save()
        return super().get(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'describe', 'tags', 'slug', 'thumbnail']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    # fields = ['body']
    http_method_names = ['post']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.object.post.slug})

def search_post(request):
    context = {}
    if request.method == 'POST':
        searched = request.POST['q']
        posts = Post.objects.filter(title__contains=searched)
        context['searched_for'] = searched
        context['posts'] = posts[:25]
        context
    return render(request, template_name='blog/search_post.html', context=context)