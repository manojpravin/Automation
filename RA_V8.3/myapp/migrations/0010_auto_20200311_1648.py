# Generated by Django 3.0.4 on 2020-03-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200226_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='braking',
            fields=[
                ('id', models.IntegerField(default=False, primary_key=True, serialize=False)),
                ('OrganizationName', models.CharField(max_length=45)),
                ('FullName', models.CharField(max_length=200)),
                ('EmailAddress', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=60)),
                ('PostalAddress', models.CharField(max_length=150)),
                ('UserCreationDate', models.CharField(max_length=50)),
                ('LastLoginDate', models.CharField(max_length=50)),
                ('LoginStatus', models.CharField(max_length=50)),
                ('PreferredFileServer', models.CharField(max_length=30)),
                ('AuditGroup', models.CharField(max_length=30)),
                ('GenericGroup', models.CharField(max_length=15)),
                ('UserLastModificationDate', models.CharField(max_length=30)),
                ('ReportWeek', models.IntegerField()),
                ('ReportYear', models.IntegerField()),
            ],
            options={
                'db_table': 'braking',
                'unique_together': {('id', 'Name', 'ReportWeek', 'ReportYear', 'UserCreationDate')},
            },
        ),
        migrations.CreateModel(
            name='css',
            fields=[
                ('id', models.IntegerField(default=False, primary_key=True, serialize=False)),
                ('OrganizationName', models.CharField(max_length=45)),
                ('FullName', models.CharField(max_length=200)),
                ('EmailAddress', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=60)),
                ('PostalAddress', models.CharField(max_length=150)),
                ('UserCreationDate', models.CharField(max_length=50)),
                ('LastLoginDate', models.CharField(max_length=50)),
                ('LoginStatus', models.CharField(max_length=50)),
                ('PreferredFileServer', models.CharField(max_length=30)),
                ('AuditGroup', models.CharField(max_length=30)),
                ('GenericGroup', models.CharField(max_length=15)),
                ('UserLastModificationDate', models.CharField(max_length=30)),
                ('ReportWeek', models.IntegerField()),
                ('ReportYear', models.IntegerField()),
            ],
            options={
                'db_table': 'css',
                'unique_together': {('id', 'Name', 'ReportWeek', 'ReportYear', 'UserCreationDate')},
            },
        ),
        migrations.CreateModel(
            name='elec',
            fields=[
                ('id', models.IntegerField(default=False, primary_key=True, serialize=False)),
                ('OrganizationName', models.CharField(max_length=45)),
                ('FullName', models.CharField(max_length=200)),
                ('EmailAddress', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=60)),
                ('PostalAddress', models.CharField(max_length=150)),
                ('UserCreationDate', models.CharField(max_length=50)),
                ('LastLoginDate', models.CharField(max_length=50)),
                ('LoginStatus', models.CharField(max_length=50)),
                ('PreferredFileServer', models.CharField(max_length=30)),
                ('AuditGroup', models.CharField(max_length=30)),
                ('GenericGroup', models.CharField(max_length=15)),
                ('UserLastModificationDate', models.CharField(max_length=30)),
                ('ReportWeek', models.IntegerField()),
                ('ReportYear', models.IntegerField()),
            ],
            options={
                'db_table': 'elec',
                'unique_together': {('id', 'Name', 'ReportWeek', 'ReportYear', 'UserCreationDate')},
            },
        ),
        migrations.CreateModel(
            name='lvs',
            fields=[
                ('id', models.IntegerField(default=False, primary_key=True, serialize=False)),
                ('OrganizationName', models.CharField(max_length=45)),
                ('FullName', models.CharField(max_length=200)),
                ('EmailAddress', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=60)),
                ('PostalAddress', models.CharField(max_length=150)),
                ('UserCreationDate', models.CharField(max_length=50)),
                ('LastLoginDate', models.CharField(max_length=50)),
                ('LoginStatus', models.CharField(max_length=50)),
                ('PreferredFileServer', models.CharField(max_length=30)),
                ('AuditGroup', models.CharField(max_length=30)),
                ('GenericGroup', models.CharField(max_length=15)),
                ('UserLastModificationDate', models.CharField(max_length=30)),
                ('ReportWeek', models.IntegerField()),
                ('ReportYear', models.IntegerField()),
            ],
            options={
                'db_table': 'lvs',
                'unique_together': {('id', 'Name', 'ReportWeek', 'ReportYear', 'UserCreationDate')},
            },
        ),
        migrations.CreateModel(
            name='oss',
            fields=[
                ('id', models.IntegerField(default=False, primary_key=True, serialize=False)),
                ('OrganizationName', models.CharField(max_length=45)),
                ('FullName', models.CharField(max_length=200)),
                ('EmailAddress', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=60)),
                ('PostalAddress', models.CharField(max_length=150)),
                ('UserCreationDate', models.CharField(max_length=50)),
                ('LastLoginDate', models.CharField(max_length=50)),
                ('LoginStatus', models.CharField(max_length=50)),
                ('PreferredFileServer', models.CharField(max_length=30)),
                ('AuditGroup', models.CharField(max_length=30)),
                ('GenericGroup', models.CharField(max_length=15)),
                ('UserLastModificationDate', models.CharField(max_length=30)),
                ('ReportWeek', models.IntegerField()),
                ('ReportYear', models.IntegerField()),
            ],
            options={
                'db_table': 'oss',
                'unique_together': {('id', 'Name', 'ReportWeek', 'ReportYear', 'UserCreationDate')},
            },
        ),
        migrations.DeleteModel(
            name='exceldata',
        ),
        migrations.AlterField(
            model_name='activeusers',
            name='AuditGroup',
            field=models.CharField(max_length=30),
        ),
    ]
