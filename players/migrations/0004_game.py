# Generated by Django 3.0.8 on 2021-11-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20211107_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_team', models.CharField(max_length=100)),
                ('home_team', models.CharField(max_length=100)),
                ('visit_win', models.FloatField()),
                ('home_win', models.FloatField()),
                ('pred_model', models.CharField(max_length=100)),
            ],
        ),
    ]
