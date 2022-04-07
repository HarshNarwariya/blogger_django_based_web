from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    content = RichTextField()
    tags = TaggableManager()
    describe = models.TextField(max_length=500)
    thumbnail = models.ImageField(null=False, upload_to='blog_thumbnails')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    views = models.BigIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name="blog_posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.thumbnail.path)
        # print(img.height, img.width)
        # output_size = (300 * 2, 150 * 2)
        # img = img.resize(output_size)
        # print(img.height, img.width)
        width, height = img.size   # Get dimgensions
        new_width = 600
        new_height = 300
        left = (width - new_width)/2
        top = (height - new_height)/2
        right = (width + new_width)/2
        bottom = (height + new_height)/2

        # Crop the center of the imgage
        img = img.crop((left, top, right, bottom))
        img.thumbnail((new_width, new_height))
        img.save(self.thumbnail.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"slug": self.slug})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)

    
