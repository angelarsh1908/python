# Generated by Django 4.0.5 on 2022-06-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_doctor_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='pic',
            field=models.FileField(default='media/ddd.png', upload_to='media/images'),
        ),
    ]