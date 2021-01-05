from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from . import forms
from . import models

class StudentsListView(generic.ListView):
    model = models.Student
    template_name = 'students/list.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        queryset = models.Student.objects.all()
        return queryset


class TeachersListView(generic.ListView):
    model = models.Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teacher_list'


    def get_queryset(self):
        queryset = models.Teacher.objects.all()
        return queryset

class TeacherCreateView(generic.CreateView):
    form_class = forms.TeacherCreateForm
    template_name = "teachers/create.html"
    success_url = reverse_lazy('teachers_list')

    def form_valid(self, form):
        user = form.save()
        birthdate = form.cleaned_data.get('birthdate')
        initials = form.cleaned_data.get('initials')
        profile = models.Teacher.objects.create(user=user, birthdate=birthdate, initials=initials, role='TEACHER')
        profile.save()
        return super(TeacherCreateView, self).form_valid(form)
