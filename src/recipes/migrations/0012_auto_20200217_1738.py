# Generated by Django 3.0.2 on 2020-02-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='username',
        ),
        migrations.AddField(
            model_name='rating',
            name='user_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
