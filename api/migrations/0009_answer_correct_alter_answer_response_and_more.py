# Generated by Django 4.0.3 on 2022-04-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='response',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(default=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
