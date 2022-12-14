# Generated by Django 4.1.3 on 2022-12-04 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_ip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('year', models.IntegerField(verbose_name='Год постуления')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000, verbose_name='Полное название')),
                ('short_name', models.CharField(max_length=20, verbose_name='Краткое название')),
                ('date', models.DateField(verbose_name='Дата создания')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='student',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ip.university', verbose_name='Место учебы'),
        ),
    ]
