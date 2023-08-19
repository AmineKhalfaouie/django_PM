from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.
class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/project_list.html'

class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/project_create.html'
    success_url = reverse_lazy('project_list')
