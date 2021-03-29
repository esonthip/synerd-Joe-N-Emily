# Generated by Django 3.1.7 on 2021-03-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officecode', models.IntegerField()),
                ('officename', models.CharField(max_length=50)),
                ('attribution', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizationcode', models.IntegerField()),
                ('description', models.TextField()),
                ('datejoined', models.DateField()),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.IntegerField()),
                ('phonenumber', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicecode', models.IntegerField()),
                ('servicename', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('premium', models.CharField(max_length=3)),
                ('allocation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriptiontypecode', models.IntegerField()),
                ('subscriptiontypename', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.IntegerField()),
                ('employername', models.CharField(max_length=50)),
            ],
        ),
    ]