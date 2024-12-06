# Generated by Django 4.2.6 on 2024-11-06 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer_subscription_management', '0004_alter_subscriptionmanagement_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField()),
                ('is_paid', models.BooleanField(default=False)),
                ('invoice_date', models.DateField(auto_now_add=True)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='customer_subscription_management.subscriptionmanagement')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paid', models.DateField(auto_now_add=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_and_invoice_management.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='BillingManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_period', models.CharField(choices=[('monthly', 'Monthly'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('yearly', 'Yearly')], max_length=200)),
                ('due_date', models.DateField()),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer_subscription_management.subscriptionmanagement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
