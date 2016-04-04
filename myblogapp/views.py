from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import generic

from .models import Post
from .models import Tag


class IndexView(generic.ListView):
    template_name = 'myblogapp/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        "Return the last five posts."
        return Post.objects.order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class PostListView(generic.ListView):
    template_name = 'myblogapp/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        "Return all posts."
        return Post.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'myblogapp/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


def tag_detail(request, slug):
    posts_with_tag = get_list_or_404(Post.objects.order_by('-pub_date'), tags__slug=slug)
    tag = get_object_or_404(Tag, slug=slug)
    context = {
        'tags': Tag.objects.all(),
        'tag': tag,
        'posts_with_tag': posts_with_tag
    }
    return render(request, 'myblogapp/tag_detail.html', context)
