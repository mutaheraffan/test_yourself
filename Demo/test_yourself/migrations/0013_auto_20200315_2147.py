# Generated by Django 2.2.7 on 2020-03-15 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_yourself', '0012_auto_20200315_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_yourself.Comment', verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_yourself.Question', verbose_name='Comment_For_Question'),
        ),
    ]
