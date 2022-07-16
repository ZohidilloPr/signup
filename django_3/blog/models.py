from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300) # input
    blog = models.TextField() #textarea
    add_time = models.DateTimeField(auto_now_add=True)       
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("OB", kwargs={"pk": self.pk})
    