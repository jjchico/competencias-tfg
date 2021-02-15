from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import activate, get_language
from django.views import generic


from . import forms
from . import models
from . import services

COMPETENCE_LIST = 'competences/list.html'
COMPETENCE_CREATE = "competences/create.html"

# Generic
class HomeView(generic.TemplateView):
    template_name = 'home.html'

# Competences
@method_decorator(login_required, name='dispatch')
class CompetenceCreateChildView(generic.CreateView):
    form_class = forms.CompetenceCreateForm
    template_name = COMPETENCE_CREATE
    
    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(CompetenceCreateChildView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')
    
    def get_context_data(self, **kwargs):
        context = super(CompetenceCreateChildView, self).get_context_data(**kwargs)
        competence_pk = self.kwargs.get('pk')
        context['competence_pk'] = competence_pk
        context['competence_parent'] = True
        return context

    def form_valid(self, form):
        competence_pk = self.kwargs.get('pk')
        competence = models.Competence.objects.get(pk=competence_pk)
        competence_new = form.save(commit=False)
        competence_new.parent = competence
        if competence.level == 3:
            competence_new.level = 2
        elif competence.level == 2:
            competence_new.level = 1
        else:
            return redirect('/')
            
        competence_new.save()

        return redirect('competences_relation', pk=competence_pk)

@method_decorator(login_required, name='dispatch')
class CompetenceCreateLevel3View(generic.CreateView):
    form_class = forms.CompetenceCreateForm
    template_name = COMPETENCE_CREATE
    success_url = reverse_lazy('competences_list3')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(CompetenceCreateLevel3View, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')
    
    def get_context_data(self, **kwargs):
        context = super(CompetenceCreateLevel3View, self).get_context_data(**kwargs)
        context['create_level3'] = True
        return context
    
    def form_valid(self, form):
        competence_new = form.save(commit=False)
        competence_new.level = 3
        competence_new.save()

        return redirect('competences_list3')

@method_decorator(login_required, name='dispatch')
class CompetencesDeleteView(generic.DeleteView):
    template_name = 'competences/delete.html'
    model = models.Competence

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(CompetencesDeleteView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        competence_pk = self.kwargs.get('pk')
        competence = models.Competence.objects.get(pk=competence_pk)
        context = super(CompetencesDeleteView, self).get_context_data(**kwargs)
        context['list_level3'] = False
        context['list_level2'] = False
        context['list_level1'] = False
        if competence.level == 3:
            context['list_level3'] = True
            
        elif competence.level == 2:
            context['list_level2'] = True
        else:
            context['list_level1'] = True

        return context

    def post(self, request, *args, **kwargs):
        competence_pk = self.kwargs.get('pk')
        competence = models.Competence.objects.get(pk=competence_pk)
        competence.delete()
        
        if competence.level == 3:
            return redirect('competences_list3')
            
        elif competence.level == 2:
            return redirect('competences_list2')
        else:
            return redirect('competences_list1')

class CompetencesListChildView(generic.ListView):
    model = models.Competence
    template_name = COMPETENCE_LIST
    context_object_name = 'competence_list'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(CompetencesListChildView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')
    
    def get_context_data(self, **kwargs):
        context = super(CompetencesListChildView, self).get_context_data(**kwargs)
        competence_pk = self.kwargs.get('pk')
        competence = models.Competence.objects.get(pk=competence_pk)
        context['competence_pk'] = competence_pk
        context['listall_level3'] = False
        context['listall_level2'] = False
        context['list_level2'] = False
        context['list_level1'] = False

        if competence.level == 3:
            context['list_level2'] = True
        elif competence.level == 2:
            context['list_level1'] = True

        return context

    def get_queryset(self):
        level3_pk = self.kwargs.get('pk')
        level3 = models.Competence.objects.get(pk=level3_pk)
        queryset = models.Competence.objects.filter(parent=level3)
        return queryset

class CompetenceListLevel1View(generic.ListView):
    model = models.Competence
    template_name = COMPETENCE_LIST
    context_object_name = 'competence_list'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(CompetenceListLevel1View, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(CompetenceListLevel1View, self).get_context_data(**kwargs)
        context['listall_level3'] = False
        context['listall_level2'] = False
        context['list_level2'] = False

        return context

    def get_queryset(self):
        queryset = models.Competence.objects.filter(level="1")
        return queryset

class CompetenceListLevel2View(generic.ListView):
    model = models.Competence
    template_name = COMPETENCE_LIST
    context_object_name = 'competence_list'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(CompetenceListLevel2View, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(CompetenceListLevel2View, self).get_context_data(**kwargs)
        context['listall_level3'] = False
        context['listall_level2'] = True
        context['list_level2'] = False

        return context

    def get_queryset(self):
        queryset = models.Competence.objects.filter(level="2")
        return queryset

class CompetenceListLevel3View(generic.ListView):
    model = models.Competence
    template_name = COMPETENCE_LIST
    context_object_name = 'competence_list'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(CompetenceListLevel3View, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(CompetenceListLevel3View, self).get_context_data(**kwargs)
        context['listall_level3'] = True
        context['listall_level2'] = False
        context['list_level3'] = False
        context['list_level2'] = False

        return context

    def get_queryset(self):
        queryset = models.Competence.objects.filter(level="3")
        return queryset

@method_decorator(login_required, name='dispatch')
class CompetenceUpdateView(generic.UpdateView):
    model = models.Competence
    form_class = forms.CompetenceCreateForm
    template_name = COMPETENCE_CREATE

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(CompetenceUpdateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(CompetenceUpdateView, self).get_context_data(**kwargs)
        context['is_update'] = True
        return context

    def form_valid(self, form):
        competence = form.save()

        if competence.level == 3:
            return redirect('competences_list3')
        elif competence.level == 2:
            return redirect('competences_list2')
        else:
            return redirect('competences_list1')

@method_decorator(login_required, name='dispatch')
class StudentCreateView(generic.CreateView):
    form_class = forms.StudentCreateForm
    template_name = "students/create.html"
    success_url = reverse_lazy('students_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(StudentCreateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')
class StudentDeleteView(generic.DeleteView):
    template_name = 'students/delete.html'
    model = models.Student
    success_url = reverse_lazy('students_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(StudentDeleteView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')
class StudentsListView(generic.ListView):
    model = models.Student
    template_name = 'students/list.html'
    context_object_name = 'student_list'
    paginate_by = 5


    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(StudentsListView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_queryset(self):
        queryset = models.Student.objects.all().order_by('surname')
        return queryset

@method_decorator(login_required, name='dispatch')
class StudentUpdateView(generic.UpdateView):
    model = models.Student
    form_class = forms.StudentCreateForm
    template_name = "students/create.html"
    success_url = reverse_lazy('students_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(StudentUpdateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')
class TeacherCreateView(generic.CreateView):
    form_class = forms.TeacherCreateForm
    template_name = "teachers/create.html"
    success_url = reverse_lazy('teachers_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(TeacherCreateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def form_valid(self, form):
        user = form.save()
        birthdate = form.cleaned_data.get('birthdate')
        initials = form.cleaned_data.get('initials')
        profile = models.Teacher.objects.create(user=user, birthdate=birthdate, initials=initials, role='TEACHER')
        profile.save()
        return super(TeacherCreateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class TeacherDeleteView(generic.DeleteView):
    model = models.Teacher
    template_name = 'teachers/confirm_delete.html'

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(TeacherDeleteView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def post(self, request, *args, **kwargs):
        teacher_pk = self.kwargs.get('pk')
        teacher = models.Teacher.objects.get(pk=teacher_pk)
        teacher.user.delete()
        teacher.delete()

        return redirect('teachers_list')

@method_decorator(login_required, name='dispatch')
class TeachersListView(generic.ListView):
    model = models.Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teacher_list'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(TeachersListView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_queryset(self):
        queryset = models.Teacher.objects.all().order_by('user__last_name')
        return queryset

@method_decorator(login_required, name='dispatch')        
class TeacherUpdateView(generic.UpdateView):
    model = models.User
    form_class = forms.UserUpdateForm
    teacher_form_class = forms.TeacherUpdateForm
    template_name = "teachers/create.html"
    success_url = reverse_lazy('teachers_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(TeacherUpdateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(TeacherUpdateView, self).get_context_data(**kwargs)
        context['teacher_form'] = self.teacher_form_class(instance=self.object.profile)
        return context

    def get_object(self):
        teacher_pk = self.kwargs.get('pk')
        teacher = models.Teacher.objects.get(pk=teacher_pk)
        teacher_user = teacher.user
        return teacher_user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        teacher_form = self.teacher_form_class(
            request.POST, instance=self.object.profile)
        if form.is_valid() and teacher_form.is_valid():
            user = form.save()
            teacher_form.save(user)
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form, profile_form=teacher_form))

@method_decorator(login_required, name='dispatch')
class SetsListView(generic.ListView):
    model = models.Set
    template_name = 'sets/list.html'
    context_object_name = 'set_list'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(SetsListView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_queryset(self):
        queryset = models.Set.objects.all().order_by('name')
        return queryset

@method_decorator(login_required, name='dispatch')
class SetDeleteView(generic.DeleteView):
    template_name = 'sets/delete.html'
    model = models.Set
    success_url = reverse_lazy('sets_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(SetDeleteView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')
class SetCreateView(generic.CreateView):
    form_class = forms.SetCreateForm
    template_name = "sets/create.html"
    success_url = reverse_lazy('sets_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(SetCreateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')
class SetUpdateView(generic.UpdateView):
    model = models.Set
    form_class = forms.SetCreateForm
    template_name = "sets/create.html"
    success_url = reverse_lazy('sets_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(SetUpdateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')


class not_impl(generic.TemplateView):
    template_name = "not_impl.html"

@method_decorator(login_required, name='dispatch')
class EvaluationsListView(generic.ListView):
    model = models.Evaluation
    template_name = 'evaluations/list.html'
    context_object_name = 'evaluations_list'
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(EvaluationsListView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')
            
    def get_queryset(self):
        queryset = models.Evaluation.objects.all().order_by('name','subject', 'parent', 'start_date')
        return queryset

@method_decorator(login_required, name='dispatch')
class EvaluationDeleteView(generic.DeleteView):
    template_name = 'evaluations/delete.html'
    model = models.Evaluation
    success_url = reverse_lazy('evaluations_list')

    def get(self, request, *args, **kwargs):
        evaluation_pk = self.kwargs.get('pk')
        parent = models.Evaluation.objects.get(pk=evaluation_pk)
        if services.UserService().is_admin(request.user) and parent.is_final:
            return super(EvaluationDeleteView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')
    
    def delete(self, request, *args, **kwargs):
        evaluation_pk = self.kwargs.get('pk')
        parent = models.Evaluation.objects.get(pk=evaluation_pk)
        if parent.is_final:
            models.Evaluation.objects.filter(parent=parent).delete()
            parent.delete()
            return redirect('evaluations_list')
        else:
            return redirect('/')


@method_decorator(login_required, name='dispatch')
class EvaluationCreateView(generic.CreateView):
    form_class = forms.EvaluationCreateForm
    template_name = "evaluations/update.html"
    success_url = reverse_lazy('evaluations_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(EvaluationCreateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        start_date = form.cleaned_data.get('start_date')
        end_date_1 = form.cleaned_data.get('end_date_1')
        start_date_2 = form.cleaned_data.get('start_date_2')
        end_date_2 = form.cleaned_data.get('end_date_2')
        start_date_3 = form.cleaned_data.get('start_date_3')
        end_date = form.cleaned_data.get('end_date')
        subject = form.cleaned_data.get('subject')

        evaluation = form.save(commit=False) 
        evaluation.is_final=True
        evaluation.period = "Final"
        evaluation.save()
        evaluation1 = models.Evaluation.objects.create(name=name, start_date=start_date, end_date=end_date_1,
            is_final=False, period="1st", subject=subject, parent=evaluation)
        evaluation1.save()
        evaluation2 = models.Evaluation.objects.create(name=name, start_date=start_date_2, end_date=end_date_2,
            is_final=False, period="2nd", subject=subject, parent=evaluation)
        evaluation2.save()
        evaluation3 = models.Evaluation.objects.create(name=name, start_date=start_date_3, end_date=end_date,
            is_final=False, period="3rd", subject=subject, parent=evaluation)
        evaluation3.save()

        return redirect('evaluations_list')
    
@method_decorator(login_required, name='dispatch')
class EvaluationUpdateView(generic.UpdateView):
    model = models.Evaluation
    form_class = forms.EvaluationUpdateForm
    template_name = "evaluations/update.html"
    success_url = reverse_lazy('evaluations_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(EvaluationUpdateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

class SubjectsListView(generic.ListView):
    model = models.Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subject_list'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(SubjectsListView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_queryset(self):
        queryset = models.Subject.objects.all().order_by('name')
        return queryset

class SubjectsDeleteView(generic.DeleteView):
    template_name = 'subjects/delete.html'
    model = models.Subject
    success_url = reverse_lazy('subjects_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(SubjectsDeleteView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')
class SubjectCreateView(generic.CreateView):
    form_class = forms.SubjectCreateForm
    template_name = "subjects/create.html"
    success_url = reverse_lazy('subjects_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(SubjectCreateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')        
class SubjectsUpdateView(generic.UpdateView):
    model = models.Subject
    form_class = forms.SubjectCreateForm
    template_name = "subjects/create.html"
    success_url = reverse_lazy('subjects_list')

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(SubjectsUpdateView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')        
class SetAssignStudentListView(generic.ListView, generic.list.MultipleObjectMixin):
    model = models.Set
    template_name = 'students/list_assign_student.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(SetAssignStudentListView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        set_object_pk = self.kwargs.get('pk')
        set_object = models.Set.objects.get(pk=set_object_pk)
        object_list = set_object.students.all().order_by('surname')
        context = super(SetAssignStudentListView, self).get_context_data(
            object_list=object_list, **kwargs)
        context['other_students'] = models.Student.objects.all().exclude(id__in=object_list).order_by('surname')
        context['set_object_pk'] = set_object_pk

        return context

class SetAssignStudentView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            student_pk = self.kwargs.get('pk')
            student = models.Student.objects.get(pk=student_pk)
            set_pk = self.kwargs.get('id')
            set_object = models.Set.objects.get(pk=set_pk)

            set_object.students.add(student)
            set_object.save()
            return redirect('sets_assign_student_list', pk=set_pk)
        else:
            return redirect('/')

class SetUnassignStudentView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            student_pk = self.kwargs.get('pk')
            student = models.Student.objects.get(pk=student_pk)
            set_pk = self.kwargs.get('id')
            set_object = models.Set.objects.get(pk=set_pk)

            set_object.students.remove(student)
            set_object.save()
            return redirect('sets_assign_student_list', pk=set_pk)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')        
class TeacherAssignSubjectListView(generic.ListView, generic.list.MultipleObjectMixin):
    model = models.Teacher
    template_name = 'subjects/list_assign_subject.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            return super(TeacherAssignSubjectListView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        teacher_object_pk = self.kwargs.get('pk')
        teacher_object = models.Teacher.objects.get(pk=teacher_object_pk)
        object_list = teacher_object.subjects.all().order_by('name')
        context = super(TeacherAssignSubjectListView, self).get_context_data(
            object_list=object_list, **kwargs)
        context['other_subjects'] = models.Subject.objects.all().exclude(id__in=object_list).order_by('name')
        context['teacher_object_pk'] = teacher_object_pk

        return context

class TeacherAssignSubjectView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            subject_pk = self.kwargs.get('pk')
            subject = models.Subject.objects.get(pk=subject_pk)
            teacher_pk = self.kwargs.get('id')
            teacher_object = models.Teacher.objects.get(pk=teacher_pk)

            teacher_object.subjects.add(subject)
            teacher_object.save()
            return redirect('teachers_assign_subject_list', pk=teacher_pk)
        else:
            return redirect('/')

class TeacherUnassignSubjectView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        if services.UserService().is_admin(request.user):
            subject_pk = self.kwargs.get('pk')
            subject = models.Subject.objects.get(pk=subject_pk)
            teacher_pk = self.kwargs.get('id')
            teacher_object = models.Teacher.objects.get(pk=teacher_pk)

            teacher_object.subjects.remove(subject)
            teacher_object.save()
            return redirect('teachers_assign_subject_list', pk=teacher_pk)
        else:
            return redirect('/')

@method_decorator(login_required, name='dispatch')
class SubjectsOwnerListView(generic.ListView):
    model = models.Student
    template_name = 'subjects/list.html'
    context_object_name = 'subject_list'
    paginate_by = 5


    def get(self, request, *args, **kwargs):
        if services.UserService().is_teacher(request.user):
            return super(SubjectsOwnerListView, self).get(self, request, *args, **kwargs)
        else:
            return redirect('/')

    def get_queryset(self):
        user = self.request.user
        teacher = models.Teacher.objects.get(user=user)
        subjects = teacher.subjects.all()
        return subjects     
