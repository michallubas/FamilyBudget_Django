# Generated by Django 3.2 on 2021-04-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_inout_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inout',
            name='category',
            field=models.CharField(max_length=16),
        ),
    ]