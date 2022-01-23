import random
from mrz import *
from pathlib import Path
from datetime import datetime
from babel.dates import format_date
from PIL import Image, ImageDraw, ImageFont
from mrz.generator.mrva import MRVACodeGenerator, dictionary


class Imager:

    main_font = ImageFont.truetype('media/cfg/font/italy_main.ttf', 34)
    font_vertical_id = ImageFont.truetype('media/cfg/font/SNEgCheck1MP.ttf', 120)
    mrz_font = ImageFont.truetype('media/cfg/font/cour.ttf', 47)  # Шрифт для MRZ
    doc_template_path = 'media/template_document/italy/template.png'
    font_color = 40, 40, 40  # Цвет основного шрифта
    document_type = 480, 1145  # Тип документа
    country_code = 620, 1140  # Код страны
    surname = 480, 1225  # Фамилия
    given_names = 480, 1295  # Имя
    document_number = 1120, 1140  # Номер документа
    nationality = 480, 1370  # Национальность
    birth_date = 480, 1445  # День рождения
    sex = 480, 1520  # Пол
    expiry_date = 480, 1690  # Дата выдачи
    issue_date = 480, 1595  # Дата окончания
    optional_data = 480, 12  # Опциональная информация
    coord_photo = 45, 1190  # Положение фотограции
    size_second_photo = 120, 120
    coord_second_photo = 1120, 1190
    mrz_coords = 120, 1900
    coord_sing_img = 12, 12
    country_document = 'it'  # ISO format
    second_photo = True  # Определяет присутствие дополнительного фото
    need_mrz = True
    config_path = None
    vertical_id_number = True

    def __init__(self, face, bac, exif, trim=False):
        self.face = face
        self.bac = bac
        self.trim = trim
        self.exif = exif

    def remove_background(self, face):
        img = Image.open(face).convert("RGBA")
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        image_no_bg_path = f'media/{self.user}/without_bg-{random.randint(1000,9999)}.png'
        img.save(image_no_bg_path)
        return img

    def paste_photo(self, pasport_tmp):
        # Открываем изображение куда вешать фото
        photo_id = Image.open(self.face).convert('RGBA')  # Открывает изображение лица
        if self.trim:
            photo_id = self.remove_background(self.face)
        template = Image.open(pasport_tmp)
        # Назначаем на переменные высоту и ширину фото в паспорт
        width, height = photo_id.size
        new_height = 498  # Устанавливаем нормальную высоту относительно шаблона
        # Расчитываем размер для обрезания :)
        new_width = new_height * width // height
        photo_id = photo_id.resize(
            (new_width, new_height), Image.ANTIALIAS)  # Обрезаем
        """ Тут я наверное зелаю костыльно но бл.. """
        if self.second_photo:
            new_height_sec = 300
            new_width_sec = new_height_sec * width // height
            sec_photo = photo_id.resize(
                (new_width_sec, new_height_sec), Image.ANTIALIAS)

            template.paste(sec_photo, self.coord_second_photo, sec_photo)

        template.paste(photo_id, self.coord_photo, photo_id)
        filename = f'media/{self.user}/{random.randint(11111, 99999999)}.png'
        template.save(filename)
        return filename

    def paste_background(self, tmp):
        t = Image.open(self.paste_photo(tmp))
        background = Image.open(self.bac)
        w, h = t.size
        nh = int(background.size[1] / 1.3)  # Высота
        nw = int(nh * w / h)

        # template = t.resize(
        #     (background.size[0] // 3, background.size[1] // 3), Image.ANTIALIAS)
        template = t.resize((nw, nh), Image.ANTIALIAS)
        background.paste(
            template, ((int(background.size[0] / 100 * 10)), int(background.size[1] / 100 * 10)), template)
        filename = f'media/{self.user}/done-{datetime.now()}.png'
        background.save(filename, exif=self.exif_paster())
        print(f'Фото создано {filename}')
        return filename

    def info_paste(self, user, mrz, *args, **kwargs):
        tmp = Image.open(self.doc_template_path)
        p1, p2 = tmp.size
        blank = Image.new('RGBA', (p1, p2))
        image = ImageDraw.Draw(blank)
        image.text((self.document_type),
                   kwargs['document_type'], self.font_color, self.main_font)
        image.text((self.country_code),
                   kwargs['country_code'], self.font_color, self.main_font)
        image.text((self.surname), kwargs['surname'],
                   self.font_color, self.main_font)
        image.text((self.given_names), kwargs['given_names'],
                   self.font_color, self.main_font)
        image.text((self.document_number), kwargs['document_number'],
                   self.font_color, self.main_font)
        image.text((self.nationality), kwargs['nationality'],
                   self.font_color, self.main_font)
        image.text((self.birth_date), self.date_country(kwargs['birth_date']),
                   self.font_color, self.main_font)
        image.text((self.sex), kwargs['sex'],
                   self.font_color, self.main_font)
        image.text((self.expiry_date), self.date_country(kwargs['expiry_date']),
                   self.font_color, self.main_font)
        image.text((self.issue_date), self.date_country(kwargs['issue_date']),
                   self.font_color, self.main_font)
        image.text((self.optional_data), kwargs['optional_data'],
                   self.font_color, self.main_font)
        image.text((self.mrz_coords), mrz, self.font_color, self.mrz_font)

        tmp.paste(blank, (0, 0), blank)
        nums = self.paste_vertical_pasport_number(kwargs['document_number'])
        tmp.paste(nums, (30, 170), nums)
        sing = Image.open('media/cfg/sing_png/27.jpg.png').resize((2, 2), Image.ANTIALIAS)
        tmp.paste(sing, (self.coord_sing_img), sing)
        p = Path(f'media/{user}')
        p.mkdir(exist_ok=True)
        print(p)
        self.user = user
        filename = f'media/{user}/{random.randint(11111, 99999999)}.png'

        tmp.save(filename)
        return filename

    def exif_paster(self):
        return Image.open(self.exif).getexif()

    def date_country(self, d):
        dt = datetime.strptime(d, '%y%m%d')
        en_mouth = format_date(dt, 'MMM', locale='en')
        locale_mouth = format_date(dt, 'MMM', locale=self.country_document)
        return f'{dt.day} {en_mouth}/{locale_mouth} {dt.year}'.upper()

    def paste_mrz(self):
        pass

    def paste_vertical_pasport_number(self, passport_number):
        line_height = sum(self.font_vertical_id.getmetrics())
        fontimage = Image.new(
            'L', (self.font_vertical_id.getsize(passport_number)[0], line_height))
        text = ImageDraw.Draw(fontimage).text((0, 0), passport_number,
                                              fill=120, font=self.font_vertical_id)
        fontimage = fontimage.rotate(90, resample=Image.BICUBIC, expand=True)
        return fontimage

    def paste_signature(self):
        pass


# def main():
#     kw = {
#         'document_type': 'P',
#         'country_code': 'USA',
#         'surname': 'Valery',
#         'given_names': 'Artrar',
#         'document_number': '99221120',
#         'nationality': 'USA',
#         'birth_date': '20001212',
#         'sex': 'M',
#         'expiry_date': '20291212',
#         'issue_date': '20191212',
#         'optional_data': ''
#     }

#     face = 'images/face_5VxveiX.jpeg'
#     passport = 'images/template.png'
#     background = 'ex.jpg'
#     ex = 'ex.jpg'
#     im = Imager(passport, face, background, ex, True)
#     mrz = MRVACodeGenerator('V', 'USA', 'Valery', 'Artrar', '99221120',
#                             'USA', '001212', 'M', '291212', '191212', '', force=False)
#     withoutbginfo = im.info_paste(str(mrz), **kw)
#     im.paste_background(withoutbginfo)


# if __name__ == '__main__':
#     main()
