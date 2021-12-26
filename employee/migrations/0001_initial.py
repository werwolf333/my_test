# Generated by Django 4.0 on 2021-12-26 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('surname', models.CharField(max_length=20, verbose_name='surname')),
                ('patronymic', models.CharField(max_length=20, verbose_name='patronymic')),
                ('position', models.CharField(max_length=20, verbose_name='position')),
                ('position_level', models.IntegerField()),
                ('employment_date', models.DateField(verbose_name='employment_date')),
                ('salary', models.FloatField(verbose_name='salary')),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workers', to='employee.employee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='InfoPaidSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_paid', models.DateField(verbose_name='data_paid')),
                ('paid', models.FloatField(blank=True, null=True, verbose_name='paid')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='men', to='employee.employee')),
            ],
        ),
    ]
