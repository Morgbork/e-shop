# Generated by Django 2.1.7 on 2019-03-15 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objectviewed',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Object viewed', 'verbose_name_plural': 'Objects viewed'},
        ),
    ]
