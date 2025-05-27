from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe

class Course(models.Model):
    COURSE_STATUS = (
        ('draft', 'Draft'), 
        ('published', 'Published')
    )
    title = models.CharField(max_length=120)
    description = models.TextField()
    publish_date = models.DateTimeField()
    price = models.IntegerField()
    author = models.CharField(max_length=200)
    status = models.CharField(default = 'published', help_text='Enter field documentation',max_length = 15, choices = COURSE_STATUS)
    def __str__(self):
        return self.title
    
    @admin.display(description="New Column")
    def captital_title(self):
        return self.title.upper()
    # @property
    # def lessons(self):
    #     return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    
    def image_privew(self):
        return mark_safe(f'<img src="{self.image.url}" alt = "" width = "300"/>')    
    def admin_image_privew(self):
        return mark_safe(f'<img src="{self.image.url}" alt = "" width = "100" style="border: 1px solid #000;border-radius:50%;"/>')    
    admin_image_privew.short_description = "Image"
    # admin_image_privew.allow_tags = True
    
    def __str__(self):
        return self.name