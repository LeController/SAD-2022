# Generated by Django 4.0.1 on 2022-02-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammate',
            name='title',
            field=models.CharField(default='Mr.', max_length=10),
            preserve_default=False,
        ),
    ]
