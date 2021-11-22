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


class Country(models.Model):
    country = coun


class ConfigureHomePage(models.Model):
    name = models.CharField('Name', max_length=200)
    folder = models.CharField('Path folder', max_length=128)
