# Generated by Django 3.0.7 on 2020-07-09 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200707_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publised_date',
            new_name='published_date',
        ),
    ]
