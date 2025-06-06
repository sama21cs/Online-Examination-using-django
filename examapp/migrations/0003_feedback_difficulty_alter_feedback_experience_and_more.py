# Generated by Django 5.2.2 on 2025-06-05 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='difficulty',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='quality',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='suggestions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
