# Generated by Django 4.0.3 on 2022-04-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_answer_answered_alter_answer_favorited_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='response',
            field=models.CharField(default=True, max_length=10000),
        ),
    ]
