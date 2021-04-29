# Generated by Django 3.1.6 on 2021-04-29 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('date', models.DateField(verbose_name='date')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='weight')),
                ('is_recovery', models.BooleanField(verbose_name='is_recovery')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_activity_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('code', models.CharField(max_length=50, verbose_name='code')),
                ('name', models.CharField(max_length=300, verbose_name='name')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='weight')),
                ('subject_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='subject_weight')),
                ('level', models.PositiveIntegerField(verbose_name='level')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_competence_created', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ManyToManyField(blank=True, related_name='competence_parent', to='corrigeapp.Competence', verbose_name='competences_parent')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_competence_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Competence',
                'verbose_name_plural': 'Competences',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('start_date', models.DateField(verbose_name='start_date')),
                ('end_date', models.DateField(verbose_name='end_date')),
                ('is_final', models.BooleanField(verbose_name='is_final')),
                ('period', models.CharField(max_length=50, verbose_name='period')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='weight')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_evaluation_created', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_parent', to='corrigeapp.evaluation')),
            ],
            options={
                'verbose_name': 'Evaluation',
                'verbose_name_plural': 'Evaluations',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='weight')),
                ('statement', models.CharField(max_length=300, verbose_name='statement')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_exercise', to='corrigeapp.activity')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_exercise_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_exercise_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Exercise',
                'verbose_name_plural': 'Exercises',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(verbose_name='birthdate')),
                ('initials', models.CharField(max_length=9, verbose_name='initials')),
                ('role', models.CharField(max_length=50, verbose_name='role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='corrigeapp.profile')),
            ],
            options={
                'verbose_name': 'Admistrator',
                'verbose_name_plural': 'Admistrators',
            },
            bases=('corrigeapp.profile',),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('level', models.CharField(max_length=50, verbose_name='level')),
                ('grade', models.CharField(max_length=50, verbose_name='grade')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('competences', models.ManyToManyField(related_name='competences', to='corrigeapp.Competence', verbose_name='competences_subject')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_subject_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_subject_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('surname', models.CharField(max_length=100, verbose_name='surname')),
                ('birthdate', models.DateField(verbose_name='birthdate')),
                ('initials', models.CharField(max_length=10, verbose_name='initials')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_student_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_student_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('level', models.CharField(max_length=50, verbose_name='level')),
                ('grade', models.CharField(max_length=50, verbose_name='grade')),
                ('line', models.CharField(max_length=50, verbose_name='line')),
                ('evaluation_type_final', models.CharField(blank=True, max_length=100, null=True, verbose_name='evaluation_type_final')),
                ('evaluation_type_partial', models.CharField(blank=True, max_length=100, null=True, verbose_name='evaluation_type_partial')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_set_created', to=settings.AUTH_USER_MODEL)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_set', to='corrigeapp.evaluation')),
                ('students', models.ManyToManyField(blank=True, related_name='student', to='corrigeapp.Student', verbose_name='students_set')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_set', to='corrigeapp.subject')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_set_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Set',
                'verbose_name_plural': 'Sets',
            },
        ),
        migrations.CreateModel(
            name='Exercise_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('mark', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='mark')),
                ('manual_mark', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='manual_mark')),
                ('evaluation_type', models.CharField(max_length=50, verbose_name='evaluation_type')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_exercise_mark_created', to=settings.AUTH_USER_MODEL)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_exercise_mark', to='corrigeapp.exercise')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_exercise_mark', to='corrigeapp.student')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_exercise_mark_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Exercise_mark',
                'verbose_name_plural': 'Exercise_marks',
            },
        ),
        migrations.CreateModel(
            name='Exercise_competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('intensity', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='intensity')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='weight')),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competence_exercise_competence', to='corrigeapp.competence')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_exercise_competence_created', to=settings.AUTH_USER_MODEL)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_exercise_competence', to='corrigeapp.exercise')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_exercise_competence_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Exercise_competence',
                'verbose_name_plural': 'Exercise_competences',
            },
        ),
        migrations.CreateModel(
            name='Evaluation_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('mark', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='mark')),
                ('manual_mark', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='manual_mark')),
                ('evaluation_type', models.CharField(max_length=50, verbose_name='evaluation_type')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_evaluation_mark_created', to=settings.AUTH_USER_MODEL)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_evaluation_mark', to='corrigeapp.evaluation')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_evaluation_mark', to='corrigeapp.student')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_evaluation_mark_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Evaluation_mark',
                'verbose_name_plural': 'Evaluation_marks',
            },
        ),
        migrations.AddField(
            model_name='evaluation',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_evaluation', to='corrigeapp.subject'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_evaluation_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Competence_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('mark', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='mark')),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competence_competence_mark', to='corrigeapp.competence')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_competence_mark_created', to=settings.AUTH_USER_MODEL)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_competence_mark', to='corrigeapp.exercise')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_competence_mark', to='corrigeapp.student')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_competence_mark_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Competence_mark',
                'verbose_name_plural': 'Competence_marks',
            },
        ),
        migrations.CreateModel(
            name='Competence_evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('mark', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='mark')),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competence_competence_evaluation', to='corrigeapp.competence')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_competence_evaluation_created', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_competence_evaluation', to='corrigeapp.student')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_competence_evaluation_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Competence_evaluation',
                'verbose_name_plural': 'Competence_evaluations',
            },
        ),
        migrations.CreateModel(
            name='Activity_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('mark', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='mark')),
                ('manual_mark', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='manual_mark')),
                ('evaluation_type', models.CharField(max_length=50, verbose_name='evaluation_type')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_activity_mark', to='corrigeapp.activity')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_activity_mark_created', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_activity_mark', to='corrigeapp.student')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_activity_mark_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity_mark',
                'verbose_name_plural': 'Activity_marks',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='evaluation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_activity', to='corrigeapp.evaluation'),
        ),
        migrations.AddField(
            model_name='activity',
            name='set_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_activity', to='corrigeapp.set'),
        ),
        migrations.AddField(
            model_name='activity',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_activity', to='corrigeapp.subject'),
        ),
        migrations.AddField(
            model_name='activity',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corrigeapp_activity_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='corrigeapp.profile')),
                ('subjects', models.ManyToManyField(related_name='subjects', to='corrigeapp.Subject', verbose_name='subjects_teacher')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
            bases=('corrigeapp.profile',),
        ),
        migrations.AddField(
            model_name='set',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_set', to='corrigeapp.teacher'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_evaluation', to='corrigeapp.teacher'),
        ),
    ]
