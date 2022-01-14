from django.db import models


class Documents(models.Model):
    document_number = models.CharField(verbose_name='passport_card_number ', max_length=25)
    document_number = models.CharField(verbose_name='passport_number ', max_length=25)
    nationality = models.CharField(verbose_name='nationality ', max_length=25)
    surname = models.CharField(verbose_name='surname ', max_length=25)
    given_names = models.CharField(verbose_name='given_names ', max_length=25)
    sex = models.CharField(verbose_name='sex ', max_length=25)
    date_of_birdth = models.CharField(verbose_name='date_of_birdth ', max_length=25)
    place_of_birth = models.CharField(verbose_name='place_of_birth ', max_length=25)
    issues_on = models.CharField(verbose_name='issues_on ', max_length=25)
    expiries_on = models.CharField(verbose_name='expiries_on ', max_length=25)
    documment_id = models.CharField(verbose_name='documment_id ', max_length=25)
    photo_document = models.CharField(verbose_name='photo_document ', max_length=25)


class ConfigureHomePage(models.Model):
    name = models.CharField('Name', max_length=200)
    folder = models.CharField('Path folder', max_length=128)


class DocumentsFields(models.Model):
    document_type = models.CharField(verbose_name='document_type', max_length=25, default='document_type')
    country_code = models.CharField(verbose_name='country_code', max_length=25, default='country_code')
    surname = models.CharField(verbose_name='surname', max_length=25, default='surname')
    given_names = models.CharField(verbose_name='given_names', max_length=25, default='given_names')
    document_number = models.CharField(verbose_name='document_number', max_length=25, default='document_number')
    nationality = models.CharField(verbose_name='nationality', max_length=25, default='nationality')
    birth_date = models.CharField(verbose_name='birth_date', max_length=25, default='birth_date')
    sex = models.CharField(verbose_name='sex', max_length=25, default='sex')
    expiry_date = models.CharField(verbose_name='expiry_date', max_length=25, default='expiry_date')
    issue_date = models.CharField(verbose_name='issue_date', max_length=25, default='issue_date')
    optional_data = models.CharField(verbose_name='optional_data', max_length=25, default='optional_data', blank=True)
    photo_document = models.ImageField(verbose_name="Photo iD", upload_to="media/cfg/usa/usavisa/", blank=True)
    remove_bg = models.BooleanField(verbose_name='Remove background [BETA]', default=False)
    get_exif_info = models.ImageField(verbose_name='Load image  EXIF', upload_to='exif_tool/', blank=True)
    background_image = models.ImageField(verbose_name='Загрузить фон',
                                         upload_to='media/cfg/usa/background_image/', blank=True)

    class Meta:
        verbose_name = 'Document config field'
        verbose_name_plural = 'Documents config fields'
