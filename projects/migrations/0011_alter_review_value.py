# Generated by Django 3.2.7 on 2021-09-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_review_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('down', 'down vote'), ('up', 'up vote')], max_length=200),
        ),
    ]