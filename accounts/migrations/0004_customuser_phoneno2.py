# Generated by Django 3.1.3 on 2020-12-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201201_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phoneno2',
            field=models.CharField(default=1, max_length=12, unique=True, verbose_name='contact number'),
            preserve_default=False,
        ),
    ]
