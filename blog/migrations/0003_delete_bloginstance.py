# Generated by Django 4.1.5 on 2023-01-30 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_bloginstance_uid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogInstance',
        ),
    ]