from django.test import TestCase
from .models import User, Post

# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        self.new = User(username = 'new', name = 'test1', category = "women's casual apparel")

    def test_instance(self):
        self.assertTrue(isinstance(self.new,User))

    def test_save_profile(self):
        User.save(self)
        all_users = User.objects.all()
        self.assertTrue(len(all_users),1)

    def test_delete_user(self):
        self.dee.delete()
        all_users = User.objects.all()
        self.assertEqual(len(all_users),0)


class PostTestCase(TestCase):
    def setUp(self):
        self.new_post = Post(account='1', name='Mike', contact=555-012-987, category= "Men's official shoes")


    def test_save_project(self):
        self.new_post.save()
        posts = Post.objects.all()
        self.assertEqual(len(posts),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        posts = Post.objects.all()
        self.assertEqual(len(posts),0) 