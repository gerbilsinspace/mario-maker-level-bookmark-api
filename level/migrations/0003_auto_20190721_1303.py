# Generated by Django 2.2.3 on 2019-07-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0002_auto_20190721_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level_code',
            field=models.CharField(blank=True, default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
