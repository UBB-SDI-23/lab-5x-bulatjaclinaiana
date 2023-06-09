# Generated by Django 4.1.7 on 2023-03-17 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_worker_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plantParent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='api.botanicalgarden'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='workerParent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='api.botanicalgarden'),
        ),
        migrations.CreateModel(
            name='Watching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watchingTime', models.DateTimeField()),
                ('watchingReward', models.IntegerField()),
                ('plant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='api.plant')),
                ('worker_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='api.worker')),
            ],
        ),
    ]
