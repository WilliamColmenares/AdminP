# Generated by Django 2.1.2 on 2018-10-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0004_auto_20181014_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='victimario',
            name='direccion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='victimario',
            name='ocupacion',
            field=models.CharField(max_length=140, null=True),
        ),
    ]