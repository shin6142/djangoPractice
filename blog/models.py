from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return self.title
