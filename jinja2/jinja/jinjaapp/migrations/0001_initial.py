# Generated by Django 2.2.22 on 2022-11-04 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_id', models.IntegerField()),
                ('stu_name', models.CharField(max_length=30)),
                ('stu_mail', models.EmailField(max_length=60)),
                ('stu_pass', models.CharField(max_length=30)),
            ],
        ),
    ]