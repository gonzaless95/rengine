# Generated by Django 3.1.6 on 2021-06-07 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0003_auto_20210606_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(default='ok', max_length=300, unique=True),
            preserve_default=False,
        ),
    ]
