# Generated by Django 3.2.2 on 2021-05-10 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='description',
            field=models.TextField(default='coolest duo rock and roll brother'),
            preserve_default=False,
        ),
    ]
