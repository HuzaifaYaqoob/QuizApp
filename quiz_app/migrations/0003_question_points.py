# Generated by Django 3.1.4 on 2020-12-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_question_istaken'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=30),
        ),
    ]
