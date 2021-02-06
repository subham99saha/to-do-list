# Generated by Django 3.1.6 on 2021-02-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=300)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'todo',
            },
        ),
    ]