# Generated by Django 2.2.7 on 2020-03-11 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_yourself', '0010_answer_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='comments',
        ),
    ]