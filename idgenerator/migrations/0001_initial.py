# Generated by Django 3.2.9 on 2021-11-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocUkraineInternational',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typedoc', models.CharField(default='P', max_length=2, verbose_name='Тип/Туре')),
                ('country', models.CharField(default='UKR', max_length=3, verbose_name='Код Страны/Соde of stаte')),
                ('surname', models.CharField(default='ТКАЧЕНКО', max_length=32, verbose_name='Фамилия/Surname')),
                ('given_name', models.CharField(default="МАР'ЯНА", max_length=32, verbose_name='Имя/name')),
                ('passport_number', models.CharField(default='PO894599', max_length=8, verbose_name='Номер паспорта')),
                ('genre', models.CharField(choices=[('M', 'Ч/M'), ('F', 'Ж/F')], default='F', max_length=4, verbose_name='Пол')),
                ('nationality', models.CharField(default='UKRAINE', max_length=32, verbose_name='Национальность')),
                ('birth_date', models.CharField(default='20001220', max_length=8, verbose_name='Дата рождения YYYYMMDD')),
                ('personal_number', models.CharField(default='EH № 13251', max_length=10, verbose_name='Персональний N/ Personal No.')),
                ('locations', models.CharField(default='Київ/UKR', max_length=26, verbose_name='Место рождения')),
                ('data_start', models.CharField(default='111111', max_length=20, verbose_name='Дата выдачи/Date of issue YYMMDD')),
                ('exp_date', models.CharField(default='290722', max_length=20, verbose_name='Дата окончания YYMMDD')),
                ('issuing', models.CharField(default='9099', max_length=20, verbose_name='Орган Выдачи YYMMDD')),
                ('photo_doc', models.ImageField(upload_to='cfg/input/', verbose_name='Фото в паспорт')),
                ('get_exif_info', models.ImageField(null=True, upload_to='cfg/exif_tool/', verbose_name='Загрузить фото для копирования EXIF')),
                ('background', models.BooleanField(default=False, verbose_name='Включить фон')),
                ('background_image', models.ImageField(null=True, upload_to='cfg/background_image/', verbose_name='Загрузить фон')),
                ('remove_bg', models.BooleanField(default=False, verbose_name='Удаление фона с фото [ТЕСТОВО]')),
            ],
            options={
                'verbose_name': 'Пасспорт',
                'verbose_name_plural': 'Пасспорт',
            },
        ),
        migrations.CreateModel(
            name='StateCardUsa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_card_number', models.CharField(default='C000097141', max_length=9, verbose_name='Passpord Card Num')),
                ('nationality', models.CharField(default='USA', max_length=15, verbose_name='Nationalyti')),
                ('surname', models.CharField(default='Johnson', max_length=24, verbose_name='Surname')),
                ('given_names', models.CharField(default='John', max_length=24, verbose_name='Given Names')),
                ('sex', models.CharField(default='M', max_length=3, verbose_name='Sex')),
                ('date_of_birdth', models.CharField(default='01 JAN 1986', max_length=20, verbose_name='Date of Birth')),
                ('place_of_birth', models.CharField(default='NEW YORK USA', max_length=50, verbose_name='Place of Birth')),
                ('issues_on', models.CharField(default='16 MAY 08', max_length=15, verbose_name='Issued On')),
                ('expiries_on', models.CharField(default='16 MAY 18', max_length=15, verbose_name='Expires On')),
                ('documment_id', models.CharField(default='A123456', max_length=7, verbose_name='Document ID')),
                ('photo_document', models.ImageField(null=True, upload_to='media/cfg/usa/photo_id/', verbose_name='Photo iD')),
                ('remove_bg', models.BooleanField(default=False, verbose_name='Remove background [BETA]')),
                ('get_exif_info', models.ImageField(null=True, upload_to='media/cfg/exif_tool/', verbose_name='Загрузить фото для копирования EXIF')),
                ('background_image', models.ImageField(null=True, upload_to='media/cfg/background_image/', verbose_name='Загрузить фон')),
            ],
            options={
                'verbose_name': 'State Usa iD generator',
                'verbose_name_plural': 'State Usa iD generator',
            },
        ),
    ]
