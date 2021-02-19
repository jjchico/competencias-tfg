from django.contrib.auth.hashers import make_password
from django.core import management
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from faker import Faker

from corrigeapp.models import Student, Teacher, Administrator, Competence, Subject, Evaluation, Set

import random
import json

DATE_FORMAT = '%Y-%m-%d %H:%M:%S%z'
FAKE = Faker('es_ES')
POPULATE = []
USER_PKS = range(2, 10)
STUDENT_PKS = range(1, 30)


def run():
    management.call_command('flush', interactive=False)

    seed_users()
    seed_profiles()
    seed_admins()
    seed_students()
    seed_competences()
    seed_subjects()
    seed_evaluations()
    seed_sets()

    sets = Set.objects.all()
    sets.delete()

    students = Student.objects.all()
    students.delete()

    teachers = Teacher.objects.all()
    teachers.delete()

    admins = Administrator.objects.all()
    admins.delete()

    competences = Competence.objects.all()
    competences.delete()

    subjects = Subject.objects.all()
    subjects.delete()

    evaluations = Evaluation.objects.all()
    evaluations.delete()

    with open('initial_data/initial_data.json', 'w') as file:
        file.write(json.dumps(POPULATE, indent=4))

    management.call_command('loaddata', 'initial_data/initial_data')

def seed_users():
    for pk in USER_PKS:
        profile = FAKE.profile()
        names = profile['name'].split(' ')
        first_name = names[0]
        last_name = names[1]

        fields = {
            'password': make_password(profile['username']),
            'is_superuser': False,
            'username': profile['username'],
            'first_name': first_name,
            'last_name': last_name,
            'email': profile['mail'],
            'is_staff': False,
            'date_joined': now().strftime(DATE_FORMAT),
        }
        user = {
            'pk': pk,
            'model': 'auth.User',
            'fields': fields
        }

        POPULATE.append(user)

def seed_profiles():
    for user_pk in USER_PKS:
        
        teacher = {
            'pk': user_pk,
            'model': 'corrigeapp.TEACHER',
            'fields': {
                'profile_ptr_id': user_pk,
            }
        }
        POPULATE.append(teacher)

        profile = {
            'pk': user_pk,
            'model': 'corrigeapp.PROFILE',
            'fields': {
                'birthdate': '1980-01-01',
                'initials': get_random_string(length=3).upper(),
                'role': 'TEACHER',
                'user': user_pk,
            }
        }
        POPULATE.append(profile)

def seed_admins():
    profile = FAKE.profile()
    names = profile['name'].split(' ')
    first_name = names[0]
    last_name = names[1]

    fields = {
        'password': make_password('administrator'),
        'is_superuser': False,
        'username': 'administrator',
        'first_name': first_name,
        'last_name': last_name,
        'email': profile['mail'],
        'is_staff': False,
        'date_joined': now().strftime(DATE_FORMAT),
    }

    user = {
        'pk': 1,
        'model': 'auth.User',
        'fields': fields
    }

    POPULATE.append(user)
    admin = {
        'pk': 1,
        'model': 'corrigeapp.ADMINISTRATOR',
        'fields': {
            'profile_ptr_id': 1,
        }
    }
    POPULATE.append(admin)

    profile = {
        'pk': 1,
        'model': 'corrigeapp.PROFILE',
        'fields': {
            'birthdate': '1980-01-01',
            'initials': get_random_string(length=3).upper(),
            'role': 'ADMINISTRATOR',
            'user': 1,
        }
    }
    POPULATE.append(profile)           
        

def seed_students():
    for pk in STUDENT_PKS:
        profile = FAKE.profile()
        names = profile['name'].split(' ')
        name = names[0]
        surname = names[1]

        student = {
            'pk': pk,
            'model': 'corrigeapp.Student',
            'fields': {
                'name': name,
                'surname': surname,
                'birthdate': '1980-01-01',
                'initials': get_random_string(length=3).upper(),
            }
        }
        POPULATE.append(student)

def seed_competences():
    competence_pk = 1

    ## 3º ESO Level 3
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC1',
                'name': 'Comunicación lingüística',
                'description': '3º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC1_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC2',
                'name': 'Competencia matemática y competencias básicas en ciencia y tecnología',
                'description': '3º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC2_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC3',
                'name': 'Competencia digital',
                'description': '3º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC3_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC4',
                'name': 'Aprender a aprender',
                'description': '3º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC4_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC5',
                'name': 'Competencias sociales y cívicas',
                'description': '3º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC5_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC6',
                'name': 'Sentido de la iniciativa y espíritu emprendedor',
                'description': '3º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC6_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC7',
                'name': 'Conciencia y expresiones culturales',
                'description': '3º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC7_pk = competence_pk
    competence_pk += 1

    ## 4º ESO Level 3
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC1',
                'name': 'Comunicación lingüística',
                'description': '4º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC1_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC2',
                'name': 'Competencia matemática y competencias básicas en ciencia y tecnología',
                'description': '4º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC2_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC3',
                'name': 'Competencia digital',
                'description': '4º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC3_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC4',
                'name': 'Aprender a aprender',
                'description': '4º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC4_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC5',
                'name': 'Competencias sociales y cívicas',
                'description': '4º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC5_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC6',
                'name': 'Sentido de la iniciativa y espíritu emprendedor',
                'description': '4º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC6_pk = competence_pk
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'CC7',
                'name': 'Conciencia y expresiones culturales',
                'description': '4º ESO',
                'level': 3,
            }
    }
    POPULATE.append(competence)
    competence_3ESO_CC7_pk = competence_pk
    competence_pk += 1
    
    ## FQ 3º ESO
    ## Level 2
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.1',
                'name': 'Reconocer e identificar las características del método científico.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 2,
                'parent': [competence_3ESO_CC2_pk],
        }
    }
    POPULATE.append(competence)
    competence_level2_pk = competence_pk
    competence_pk += 1
    ## FQ3 1.1 Level 1
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.1.1',
                'name': 'Formula hipótesis para explicar fenómenos cotidianos utilizando teorías y modelos científicos.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.1.2',
                'name': 'Registra observaciones, datos y resultados de manera organizada y rigurosa, y los comunica de forma oral y escrita utilizando esquemas, gráficos, tablas y expresiones matemáticas.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1
    ## Level 2
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.2',
                'name': 'Valorar la investigación científica y su impacto en la industria y en el desarrollo de la sociedad.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 2,
                'parent': [competence_3ESO_CC1_pk, competence_3ESO_CC5_pk],
        }
    }
    POPULATE.append(competence)
    competence_level2_pk = competence_pk
    competence_pk += 1
    ## FQ3 1.2 Level 1
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.2.1',
                'name': 'Relaciona la investigación científica con las aplicaciones tecnológicas en la vida cotidiana.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1
    ## Level 2
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.3',
                'name': 'Conocer los procedimientos científicos para determinar magnitudes.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 2,
                'parent': [competence_3ESO_CC2_pk],
        }
    }
    POPULATE.append(competence)
    competence_level2_pk = competence_pk
    competence_pk += 1
    ## FQ3 1.3 Level 1
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.3.1',
                'name': 'Establece relaciones entre magnitudes y unidades utilizando, preferentemente, el Sistema Internacional de Unidades y la notación científica para expresar los resultados.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1
    ## Level 2
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.4',
                'name': 'Reconocer los materiales, e instrumentos básicos presentes en los laboratorios de Física y Química; conocer y respetar las normas de seguridad y de eliminación de residuos para la protección del medio ambiente.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 2,
                'parent': [competence_3ESO_CC2_pk],
        }
    }
    POPULATE.append(competence)
    competence_level2_pk = competence_pk
    competence_pk += 1
    ## FQ3 1.4 Level 1
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.4.1',
                'name': 'Reconoce e identifica los símbolos más frecuentes utilizados en el etiquetado de productos químicos e instalaciones, interpretando su significado.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.4.2',
                'name': 'Identifica material e instrumentos básicos de laboratorio y conoce su forma de utilización para la realización de experiencias respetando las normas de seguridad e identificando actitudes y medidas de actuación preventivas.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1
    ## Level 2
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.5',
                'name': 'Interpretar la información sobre temas científicos de carácter divulgativo que aparece en publicaciones y medios de comunicación.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 2,
                'parent': [competence_3ESO_CC1_pk, competence_3ESO_CC5_pk],
        }
    }
    POPULATE.append(competence)
    competence_level2_pk = competence_pk
    competence_pk += 1
    ## FQ3 1.5 Level 1
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.5.1',
                'name': 'Selecciona, comprende e interpreta información relevante en un texto de divulgación científica y transmite las conclusiones obtenidas utilizando el lenguaje oral y escrito con propiedad.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.5.2',
                'name': 'Identifica las principales características ligadas a la fiabilidad y objetividad del flujo de información existente en internet y otros medios digitales.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1

    ## Level 2
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.6',
                'name': 'Desarrollar y defender pequeños trabajos de investigación en los que se ponga en práctica la aplicación del método científico y la utilización de las TIC.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 2,
                'parent': [competence_3ESO_CC2_pk],
        }
    }
    POPULATE.append(competence)
    competence_level2_pk = competence_pk
    competence_pk += 1
    ## FQ3 1.6 Level 1
    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.6.1',
                'name': 'Realiza pequeños trabajos de investigación sobre algún tema objeto de estudio aplicando el método científico, y utilizando las TIC para la búsqueda y selección de información y presentación de conclusiones.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1

    competence = {
        'pk': competence_pk,
        'model': 'corrigeapp.Competence',
        'fields': {
                'code': 'FQ3 1.6.2',
                'name': 'Participa, valora, gestiona y respeta el trabajo individual y en equipo.',
                'description': 'FQ 3º ESO',
                'weight': 0.15,
                'level': 1,
                'parent': [competence_level2_pk],
        }
    }
    POPULATE.append(competence)
    competence_pk += 1

def seed_subjects():
    subject_pk = 1
    competencels = []

    competencels = [2,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    subject = {
        'pk': subject_pk,
        'model': 'corrigeapp.Subject',
        'fields': {
                'name': 'Física y Química',
                'level': '3º',
                'grade': 'ESO',
                'description': 'Física y Química',
                'competences': competencels, 
            }
    }
    POPULATE.append(subject)
    subject_pk += 1
    competencels = []
    subject = {
        'pk': subject_pk,
        'model': 'corrigeapp.Subject',
        'fields': {
                'name': 'Física y Química',
                'level': '4º',
                'grade': 'ESO',
                'description': 'Física y Química',
                'competences': competencels, 
            }
    }
    POPULATE.append(subject)
    subject_pk += 1
    competencels = []
    subject = {
        'pk': subject_pk,
        'model': 'corrigeapp.Subject',
        'fields': {
                'name': 'Matemáticas',
                'level': '3º',
                'grade': 'ESO',
                'description': 'Matemáticas',
                'competences': competencels, 
            }
    }
    POPULATE.append(subject)
    subject_pk += 1
    competencels = []
    subject = {
        'pk': subject_pk,
        'model': 'corrigeapp.Subject',
        'fields': {
                'name': 'Matemáticas',
                'level': '4º',
                'grade': 'ESO',
                'description': 'Matemáticas',
                'competences': competencels, 
            }
    }
    POPULATE.append(subject)
    subject_pk += 1

def seed_evaluations():
    evaluation = {
        'pk': 1,
        'model': 'corrigeapp.Evaluation',
        'fields': {
                'name': 'Matemáticas 5º Primaria Final',
                'start_date': '1980-01-01',
                'end_date': '1980-01-01',
                'is_final': True,
                'period': 'Final',
                'subject': 3,
            }
    }
    POPULATE.append(evaluation)

def seed_sets():
    students = []

    for n in STUDENT_PKS:
        students.append(n)

    set_obj = {
        'pk': 1,
        'model': 'corrigeapp.Set',
        'fields': {
                'name': 'Matemáticas 5ºA Primaria',
                'level': '5º',
                'grade': 'Primaria',
                'line': 'A',
                'teacher': 2,
                'subject': 3,
                'evaluation': 1,
                'students': students,
            }
    }
    POPULATE.append(set_obj)