# Generated by Django 3.0.8 on 2020-07-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.CharField(default='neupytech', max_length=250),
            preserve_default=False,
        ),
    ]