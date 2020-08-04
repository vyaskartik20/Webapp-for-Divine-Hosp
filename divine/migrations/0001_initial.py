# Generated by Django 3.0.8 on 2020-08-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Email', models.EmailField(max_length=254)),
                ('Date', models.DateField()),
                ('PhoneNo', models.IntegerField()),
                ('Message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]