from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProjectStatus(models.IntegerChoices):
    PENDING = 1, _('Pending')
    COMPLETED = 2, _('Completed')
    POSTPONED = 3, _('Postponed')
    CANCELED = 4, _('Canceled')

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(choices=ProjectStatus.choices, default=ProjectStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True)
    #PROTECT:idha fasa5t category mattfasa5ch lmachari3 eli 3andha 3ale9a bil category hadhika
    #CASCADE:idha fasa5t l user yetfasa5 lmachari3 mte3o lkol

    def __str__(self):
        return self.title

class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    class Meta:
        ordering = ["is_completed"]
    def __str__(self):
        return self.description
