# Generated by Django 4.2.2 on 2024-06-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0005_alter_subscription_course_alter_subscription_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="sign_of_subscription",
            field=models.BooleanField(default=False, verbose_name="Признак подписки"),
        ),
    ]