from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=100)
    description = models.TextField()
    github = models.URLField()
    priority = models.IntegerField(default=0)

    image = models.ImageField(upload_to="projects/")

    def __str__(self):
        return self.project_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
