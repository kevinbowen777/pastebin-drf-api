# Generated by Django 4.0.3 on 2022-04-02 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ('created',)},
        ),
    ]
