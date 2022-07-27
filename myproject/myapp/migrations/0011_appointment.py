# Generated by Django 4.0.5 on 2022-07-05 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_doctor_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_date', models.DateField(max_length=20)),
                ('a_time', models.CharField(max_length=30)),
                ('reason', models.TextField()),
                ('status', models.CharField(default='PENDING', max_length=30)),
                ('doc_note', models.TextField(blank=True)),
                ('case_status', models.CharField(max_length=30)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.doctor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
    ]