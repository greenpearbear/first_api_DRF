# Generated by Django 4.0.4 on 2022-05-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]