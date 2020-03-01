# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavetype', models.CharField(choices=[('casual', 'Casual Leave'), ('vacation', 'Vacation Leave'), ('commuted', 'Commuted Leave'), ('special_casual', 'Special Casual Leave'), ('restricted', 'Restricted Holiday'), ('earned', 'Earned Leave')], default='casual', max_length=20)),
                ('station_leave', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('station_start_date', models.DateField(blank=True)),
                ('station_end_date', models.DateField(blank=True)),
                ('no_of_days', models.IntegerField(default=0)),
                ('purpose', models.CharField(max_length=500)),
                ('leave_address', models.CharField(blank=True, max_length=100)),
                ('processing_status', models.CharField(choices=[('rep user', 'Replacing User'), ('HOD', 'Head Of Department'), ('Director', 'Director')], default='rep user', max_length=20)),
                ('application_status', models.CharField(choices=[('accepted', 'Accepted'), ('rejected', 'Rejected'), ('processing', 'Being Processed')], default='processing', max_length=20)),
                ('admin_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_for', to=settings.AUTH_USER_MODEL)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_for', to=settings.AUTH_USER_MODEL)),
                ('replacing_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replaced_for', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RemainingLeaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casual', models.IntegerField(default=8)),
                ('vacation', models.IntegerField(blank=True, default=60)),
                ('commuted', models.IntegerField(default=20)),
                ('special_casual', models.IntegerField(default=15)),
                ('restricted', models.IntegerField(default=2)),
                ('earned', models.IntegerField(blank=True, default=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remaining_leaves', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='designation',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
