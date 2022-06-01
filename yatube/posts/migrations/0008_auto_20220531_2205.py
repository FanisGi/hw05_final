# Generated by Django 2.2.16 on 2022-05-31 19:05

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20220531_1336'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, author=django.db.models.expressions.F('user')), name='author_not_user'),
        ),
    ]
