# Generated by Django 3.2.12 on 2024-12-07 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strain_name', models.CharField(blank=True, max_length=100, null=True)),
                ('strain_type', models.CharField(choices=[('indica', 'Indica'), ('sativa', 'Sativa'), ('hybrid', 'Hybrid')], max_length=50)),
                ('rating', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
