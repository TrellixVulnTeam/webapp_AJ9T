# Generated by Django 3.0.2 on 2020-02-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20200210_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=40)),
                ('qty', models.CharField(max_length=40, null=True)),
                ('unit', models.CharField(max_length=40, null=True)),
                ('ext', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]
