# Generated by Django 4.2.6 on 2023-11-04 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0002_remove_member_name_remove_member_surname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=10)),
                ('car_name', models.CharField(max_length=20)),
                ('max_speed', models.IntegerField(default=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='Users.member')),
            ],
        ),
    ]
