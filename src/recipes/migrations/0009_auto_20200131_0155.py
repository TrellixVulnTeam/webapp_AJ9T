# Generated by Django 3.0.2 on 2020-01-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20200131_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
