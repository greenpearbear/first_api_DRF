# Generated by Django 4.0.4 on 2022-05-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_announcement_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='is_published',
            field=models.CharField(max_length=5),
        ),
    ]
