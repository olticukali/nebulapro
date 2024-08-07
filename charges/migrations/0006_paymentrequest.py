# Generated by Django 5.0.6 on 2024-07-07 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charges', '0005_bill_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('sent', 'Sent'), ('paid', 'Paid')], default='back_log', max_length=225)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charges.bill')),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charges.cost')),
            ],
        ),
    ]
