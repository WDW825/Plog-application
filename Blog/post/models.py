from django.db import models

class Post(models.Model):
    post_text = models.TextField()
    author = models.CharField(max_length=100)
    post_name = models.CharField(max_length=300, default='')
    post_date = models.DateField()
    theme_id = models.ForeignKey('theme.Theme', on_delete=models.CASCADE, default='')


#TODO: make function to generate proper post name for url
