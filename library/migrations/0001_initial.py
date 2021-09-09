# Generated by Django 3.2.7 on 2021-09-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('code', models.IntegerField()),
                ('description', models.TextField()),
                ('date_enrolled', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
