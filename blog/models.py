from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200,
                             default="WithoutTitle")
    text = models.TextField()
    author = models.ForeignKey(User,
                               on_delete=SET_NULL,
                               related_name='all_posts',
                               blank=True,
                               null=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title