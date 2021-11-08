from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

CHOICE_DATE = [
    ('JAN', 'СІЧ/JAN'),
    ('JUL', 'ЛИП/JUL'),
    ('FEB', 'ЛЮТ/FEB'),
    ('AUG', 'СЕР/AUG'),
    ('MAR', 'БЕР/MAR'),
    ('SEP', 'ВЕР/SEP'),
    ('APR', 'КВІ/APR'),
    ('OCT', 'ЖОВ/OCT'),
    ('MAY', 'ТРА/MAY'),
    ('NOV', 'ЛИС/NOV'),
    ('JUN', 'ЧЕР/JUN'),
    ('DEC', 'ГРУ/DEC'),
]

GENDER_CHOICE = [
    ('M', 'Ч/M'),
    ('F', 'Ж/F')
]

class DocUkraineInternational(models.Model):
    typedoc = models.CharField(
        verbose_name='Тип/Туре', default='P', max_length=2)
    country = models.CharField(
        verbose_name='Код Страны/Соde of stаte', default='UKR', max_length=3)
    surname = models.CharField(
        verbose_name='Фамилия/Surname', default='ТКАЧЕНКО', max_length=32)
    given_name = models.CharField(
        verbose_name='Имя/name', default="МАР'ЯНА", max_length=32)
    passport_number = models.CharField(
        verbose_name='Номер паспорта', default='PO894599', max_length=8)
    genre = models.CharField(
        verbose_name='Пол', choices=GENDER_CHOICE, default='F', max_length=4)
    nationality = models.CharField(
        verbose_name='Национальность', default='UKRAINE', max_length=32)
    birth_date = models.CharField(
        verbose_name='Дата рождения YYYYMMDD', default='20001220', max_length=8)
    personal_number = models.CharField(
        verbose_name='Персональний N/ Personal No.', default='EH № 13251', max_length=10)
    locations = models.CharField(
        verbose_name='Место рождения', default='Київ/UKR', max_length=26)
    data_start = models.CharField(
        verbose_name='Дата выдачи/Date of issue YYMMDD', default='111111', max_length=20)
    exp_date = models.CharField(
        verbose_name='Дата окончания YYMMDD', default='290722', max_length=20)
    issuing = models.CharField(
        verbose_name='Орган Выдачи YYMMDD', default='9099', max_length=20)
    photo_doc = models.ImageField(
        'Фото в паспорт', upload_to='media/cfg/input/')
    get_exif_info = models.ImageField(
        verbose_name='Загрузить фото для копирования EXIF', upload_to='media/cfg/exif_tool/', null=True)
    # background = models.BooleanField('Включить фон', default=False)
    background_image = models.ImageField(
        verbose_name='Загрузить фон', upload_to='media/cfg/background_image/', null=True)
    remove_bg = models.BooleanField(
        verbose_name='Удаление фона с фото [ТЕСТОВО]', default=False)

    class Meta:
        verbose_name = 'Пасспорт'
        verbose_name_plural = 'Пасспорт'


class StateCardUsa(models.Model):
    passport_card_number = models.CharField(
        verbose_name="Passpord Card Num", default="C000091", max_length=9)
    nationality = models.CharField(
        verbose_name="Nationalyti", max_length=15, default="USA")
    surname = models.CharField(
        verbose_name="Surname", max_length=24, default="Johnson")
    given_names = models.CharField(
        verbose_name="Given Names", max_length=24, default="John")
    sex = models.CharField(verbose_name="Sex", max_length=3, default="M")
    date_of_birdth = models.CharField(
        verbose_name="Date of Birth", max_length=20, default="01 JAN 1986")
    place_of_birth = models.CharField(
        verbose_name="Place of Birth", max_length=50, default="NEW YORK USA")
    issues_on = models.CharField(
        verbose_name="Issued On", max_length=15, default="16 MAY 08")
    expiries_on = models.CharField(
        verbose_name="Expires On", max_length=15, default="16 MAY 18")
    documment_id = models.CharField(
        verbose_name="Document ID", max_length=7, default="A123456")
    photo_document = models.ImageField(
        verbose_name="Photo iD", upload_to="media/cfg/usa/photo_id/", null=True)
    remove_bg = models.BooleanField(
        verbose_name='Remove background [BETA]', default=False)
    get_exif_info = models.ImageField(
        verbose_name='Загрузить фото для копирования EXIF', upload_to='media/cfg/exif_tool/', null=True)
    background_image = models.ImageField(
        verbose_name='Загрузить фон', upload_to='media/cfg/background_image/', null=True)

    class Meta:
        verbose_name = 'State Usa iD generator'
        verbose_name_plural = 'State Usa iD generator'


class UsaVisa(models.Model):
    EN_GENRE = [
    ('M', 'M'),
    ('F', 'F')
    ]
    doc_type = models.CharField(verbose_name='Document type', max_length=3, default='VN')
    doc_country = models.CharField(verbose_name='Document country', max_length=3, default='USA')
    surname = models.CharField(verbose_name='Surname(s)', max_length=25, default='MUSTAINE')
    givenname = models.CharField(verbose_name='Given name(s)', max_length=25, default='JOHN')
    doc_number = models.CharField(verbose_name='Document number', max_length=9,default='123456789')
    nationality = models.CharField(verbose_name='Nationality', max_length=4, default='CAN')
    birthdate = models.CharField(verbose_name='Birth date', max_length=6, default='991220')
    genre = models.CharField(verbose_name='Genre', choices=EN_GENRE, max_length=1, default='F')
    doc_exp_date = models.CharField(verbose_name='Expiry date', max_length=6, default='991220')
    optional_data = models.CharField(verbose_name='Optional data', max_length=16, default='B3XLC000FD142955', blank=True)
    photo_document = models.ImageField(verbose_name="Photo iD", upload_to="media/cfg/usa/usavisa/", blank=True)
    remove_bg = models.BooleanField(verbose_name='Remove background [BETA]', default=False)
    get_exif_info = models.ImageField(verbose_name='Load image  EXIF', upload_to='media/cfg/usa/exif_tool/', blank=True)
    background_image = models.ImageField(verbose_name='Загрузить фон', upload_to='media/cfg/usa/background_image/', blank=True)
    


    class Meta:
        verbose_name = _("Usa Visa")
        verbose_name_plural = _("Usa Visas")

    # def __str__(self):
    #     return self.givenname

    # def get_absolute_url(self):
    #     return reverse("UsaVisa_detail", kwargs={"pk": self.pk})
