# Generated by Django 2.2.4 on 2019-12-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_yourself', '0006_subcat_catag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ProfilePhoto',
            field=models.ImageField(upload_to='User_Profiles'),
        ),
    ]