# Generated by Django 4.0.5 on 2022-06-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_author_first_name_alter_author_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
