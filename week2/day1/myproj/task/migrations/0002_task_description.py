# Generated by Django 4.2.6 on 2024-09-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
