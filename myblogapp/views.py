from django.shortcuts import render
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


class PostDetailView(generic.DetailView):
	model = Post
	template_name = 'myblogapp/post_detail.html'

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		context['tags'] = Tag.objects.all()
		return context
