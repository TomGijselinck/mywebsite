from django.test import TestCase
from myblogapp.models import Post, Tag
from django.core.urlresolvers import reverse

class PostTestCase(TestCase):
    # models test
    def setUp(self):
        Post.objects.create(title="R. Feynman and QED", body="It's just revolutionary")

    def get_post(self, title="R. Feynman and QED"):
        return Post.objects.get(title=title)

    def test_post_creation(self):
        post = self.get_post()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), "R. Feynman and QED")

class PostViewTests(TestCase):
    def create_post(title, body, slug):
        return Post.objects.create(title=title, body=body, slug=slug)

    def test_index_view(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Blog Home")

    def test_detail_view(self):
        post = self.create_post(body="not so fancy body text", slug="fancy-title")
        response = self.client.get(reverse('blog:post_detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.body)

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(title="physics")

    def get_tag(self):
        return Tag.objects.get(title="physics")

    def test_tag_creation(self):
        tag = self.get_tag()
        self.assertTrue(isinstance(tag, Tag))
        self.assertEquals(tag.__str__(), "physics")

class TagViewTests(TestCase):
    def create_tag_without_posts(self):
        return Tag.objects.create(title="testing", slug="testing")
    
    def create_tag_with_posts(self):
        tag = Tag.objects.create(title="testing", slug="testing")
	post = Post.objects.create(title="A test title", slug="test-title")
	post.tags.add(tag)
	return tag

    def test_detail_view_tag_without_posts(self):
        tag = self.create_tag_without_posts()
	response = self.client.get(reverse('blog:tag_detail', args=(tag.slug,)))
	self.assertEqual(response.status_code, 404)

    def test_detail_view_tag_with_posts(self):
        tag = self.create_tag_with_posts()
	response = self.client.get(reverse('blog:tag_detail', args=(tag.slug,)))
	self.assertEqual(response.status_code, 200)
	self.assertContains(response, tag.title)

    def test_detail_view_tag_not_existing(self):
        response = self.client.get(reverse('blog:tag_detail', args=("not-existing-tag",)))
	self.assertEqual(response.status_code, 404)
