# Generated by Django 3.2.7 on 2021-09-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interestrate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_date', models.DateField()),
                ('rate_value', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
    ]
