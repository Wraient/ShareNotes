# Generated by Django 4.2.6 on 2023-10-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=150)),
                ('college_nickname', models.CharField(max_length=100)),
                ('dte_code', models.IntegerField()),
            ],
        ),
    ]
