# Generated by Django 4.2 on 2024-03-01 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_portfolio_project_alter_student_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
        ),
        migrations.AddField(
            model_name='student',
            name='portfolio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
        ),
    ]