# Generated by Django 4.2.2 on 2024-06-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_payments_payment_link_payments_session_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Время последнего посещения"
            ),
        ),
    ]
