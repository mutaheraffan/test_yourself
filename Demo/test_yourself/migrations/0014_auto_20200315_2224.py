# Generated by Django 2.2.7 on 2020-03-15 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_yourself', '0013_auto_20200315_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='comments',
        ),
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_yourself.MCQQuestion', verbose_name='Comment_of_Question'),
        ),
    ]
