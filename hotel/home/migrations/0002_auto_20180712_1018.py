# Generated by Django 2.0.5 on 2018-07-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dates',
            name='city',
        ),
        migrations.AlterField(
            model_name='hotels',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]