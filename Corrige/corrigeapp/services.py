from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import get_language

from . import models

User = get_user_model()

class ActivityService():

    def is_owner(self, user: User, activity_object: models.Activity) -> bool:
        res = False

        if activity_object.created_by == user:
            res = True
        
        return res

class BlockService():

    def is_owner(self, user: User, block: models.Evaluation) -> bool:
        res = False

        if block.teacher.user == user:
            res = True
        
        return res

class FormService():

    def raise_error(self, en_message: str, es_message: str):
        
        if get_language() == 'en':
            raise ValidationError(
                en_message)
        else:
            raise ValidationError(
                es_message)

class MarkService():

    def calculate_competence_evaluation(self, exercise_object: models.Exercise, student_object: models.Student) -> None:

        competence_mark_distinct_list = models.Competence_mark.objects.filter(competence__competence_exercise_competence__exercise = exercise_object, student=student_object).distinct('competence')

        for c_m in competence_mark_distinct_list:
            competence_mark_list = models.Competence_mark.objects.filter(competence=c_m.competence ,student=student_object)

            if not models.Competence_evaluation.filter(competence=c_m.competence ,student=student_object).exists():
                c_e = models.Competence_evaluation.create(competence=c_m.competence ,student=student_object)
                c_e.save()
            
            intensity_sum = 0.0
            marks_sum = 0.0
            c_e_saved = models.Competence_evaluation.filter(competence=c_m.competence, student=student_object)

            for c_m_c in competence_mark_list:
                e_c = models.Exercise_competence(exercise_activity__set_activity__students = student_object,  competece = c_m.competence)
                intensity_sum = intensity_sum + e_c.intensity
                marks_sum = marks_sum + c_m_c.mark
            
            mark = marks_sum/intensity_sum
            c_e_saved.mark = mark


    def calculate_competence_mark(self, mark: float, competence_mark: models.Competence_mark) -> None:

        competence_mark.mark = mark
        competence_mark.save()
    
    

class SetService():

    def is_owner(self, user: User, set_object: models.Set) -> bool:
        res = False

        if set_object.teacher.user == user:
            res = True
        
        return res

class UserService():

    def is_admin(self, user: User) -> bool:
        res = False

        if user.profile.role == 'ADMINISTRATOR':
            res = True

        return res
    
    def is_teacher(self, user: User) -> bool:
        res = False

        if user.profile.role == 'TEACHER':
            res = True

        return res
