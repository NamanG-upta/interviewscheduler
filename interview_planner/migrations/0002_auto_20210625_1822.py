# Generated by Django 2.2.10 on 2021-06-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
