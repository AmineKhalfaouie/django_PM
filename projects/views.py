from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
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

class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/project_update.html'
    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])

class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('project_list')

class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project','description']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
    #self.object.project.id t5alina n3od lsaf7et idarat al machro3

class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])

class TaskDeleteView(DeleteView):
    model = models.Task
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
