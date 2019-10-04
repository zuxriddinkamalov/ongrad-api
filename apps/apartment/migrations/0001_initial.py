# Generated by Django 2.2 on 2019-10-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('rooms', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('address', models.CharField(max_length=255)),
                ('floor', models.PositiveIntegerField()),
                ('year', models.DateField()),
                ('max_floor', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]