# Generated by Django 4.0.3 on 2022-04-09 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20220409_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodCamp',
            fields=[
                ('camp_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('description', models.CharField(default='N/A', max_length=400)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
