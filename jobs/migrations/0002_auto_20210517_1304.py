# Generated by Django 3.2.2 on 2021-05-17 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='job_close_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='job_publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
