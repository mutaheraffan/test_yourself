# Generated by Django 2.2.4 on 2019-10-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mcqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=50, unique=True)),
                ('choice1', models.CharField(max_length=50, unique=True)),
                ('choice2', models.CharField(max_length=50, unique=True)),
                ('choice3', models.CharField(max_length=50, unique=True)),
                ('choice4', models.CharField(max_length=50, unique=True)),
                ('correct_answer', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
