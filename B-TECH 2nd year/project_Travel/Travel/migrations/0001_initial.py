# Generated by Django 5.0.6 on 2024-07-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Duration', models.TextField()),
                ('Season', models.TextField()),
                ('activate', models.TextField()),
            ],
        ),
    ]
