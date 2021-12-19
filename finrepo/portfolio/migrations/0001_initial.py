# Generated by Django 3.2.10 on 2021-12-18 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_currency', djmoney.models.fields.CurrencyField(choices=[('COP', 'Peso colombiano'), ('USD', 'US Dollar')], default='COP', editable=False, max_length=3)),
                ('balance', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='COP', max_digits=16)),
                ('added_currency', djmoney.models.fields.CurrencyField(choices=[('COP', 'Peso colombiano'), ('USD', 'US Dollar')], default='COP', editable=False, max_length=3)),
                ('added', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='COP', max_digits=16)),
                ('date_added', models.DateTimeField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio')),
            ],
        ),
    ]
