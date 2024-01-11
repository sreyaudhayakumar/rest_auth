# Generated by Django 4.2.3 on 2023-12-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]