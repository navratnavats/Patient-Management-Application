# Generated by Django 3.2 on 2021-04-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0004_alter_userinfo_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
