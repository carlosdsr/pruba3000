# Generated by Django 2.2.1 on 2019-06-14 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20190608_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
