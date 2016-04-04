from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import generic

from .models import Post
from .models import Tag


class IndexView(generic.ListView):
    template_name = 'myblogapp/index.html'
    context_object_name = 'latest_post_list'
    current_page = 0
    POSTS_PER_PAGE = 3

    def get_queryset(self, **kwargs):
        "Return the last five posts."
        self.current_page = self.kwargs.get('page')
        if self.current_page is not None:
            self.current_page = int(self.current_page)
        else:
            self.current_page = 0
        return Post.objects.order_by('-pub_date')[
               self.current_page * self.POSTS_PER_PAGE: (self.current_page + 1) * self.POSTS_PER_PAGE]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['more_posts'] = len(Post.objects.all()) > self.POSTS_PER_PAGE
        context['next_page_exists'] = (self.current_page + 1) * self.POSTS_PER_PAGE < len(Post.objects.all())
        if context['next_page_exists']:
            context['next_page'] = self.current_page + 1
        context['previous_page_exists'] = self.current_page - 1 >= 0
        if context['previous_page_exists']:
            context['previous_page'] = self.current_page - 1
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
