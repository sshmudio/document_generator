import datetime
import random

from babel.dates import format_date
from mrz.generator.td3 import *
from PIL import Image, ImageDraw, ImageFont

MF = ImageFont.truetype('media/cfg/font/sans.ttf', 34)  # Основной шрифт
FFMRZ = ImageFont.truetype('media/cfg/font/cour.ttf', 47)  # Шрифт для MRZ
WIDTH = 510
SW = 510
SH = 1200
MFC = (40, 40, 40)  # Основной цвет шрифта


def endt(datestr):
    s = " "
    d = datetime.datetime.strptime(datestr, '%y%m%d')  # YYMMDD
    # print('Дата в функции dt', d)
    en_mouth = format_date(d, "MMM", locale='en')
    # print(en_mouth)
    day = format_date(d, "d", locale='en')
    # print(day)
    year = format_date(d, "yyyy", locale='en')
    # print(year)
    ukr_date = format_date(d, "MMM", locale='uk')
    # print(ukr_date)
    ukr_date_f = str(ukr_date)[0:3]
    # print(ukr_date_f)
    done = str(day + s + en_mouth + s + year
               ).replace(".", "/").upper()
    return done


def dt(datestr):
    s = " "
    d = datetime.datetime.strptime(datestr, '%y%m%d')  # YYMMDD
    print('Дата в функции dt', d)
    en_mouth = format_date(d, "MMM", locale='en')
    print(en_mouth)
    day = format_date(d, "d", locale='en')
    print(day)
    year = format_date(d, "yyyy", locale='en')
    print(year)
    ukr_date = format_date(d, "MMM", locale='uk')
    print(ukr_date)
    ukr_date_f = str(ukr_date)[0:3]
    print(ukr_date_f)
    done = str(
        day + s + ukr_date_f + "/" + en_mouth + s + year
    ).replace(".", "/").upper()
    return done


def write_main_data(
        mrz, save_after_main_data,
        typedoc, country,
        passport_number, surname,
        given_name, genre,
        birth_date, data_start,
        exp_date, personal_number):
    """ Нанесение на шаблон документа основной информации """
    img = Image.open('media/cfg/template/usavisa.png')  # Шаблон паспорта

    draw = ImageDraw.Draw(img)

    draw.text((WIDTH, SH), str(typedoc), MFC, font=MF)  # Тип документа

    draw.text((WIDTH + 290, SH), str(country), MFC, font=MF)  # Страна выдачи

    draw.text((WIDTH + 510, SH),  passport_number, MFC,
              font=MF)  # Уникальный номер документа

    draw.text(
        (WIDTH, SH + 70),
        str(surname).upper(),
        MFC, font=MF)  # Фамилия

    draw.text(
        (WIDTH, SH + 145),
        str(given_name).upper(),
        MFC, font=MF)  # Имя влядельца документа

    draw.text((WIDTH, SH + 215),  country, MFC, font=MF)  # Гражданство

    draw.text((WIDTH, SH + 300), endt(birth_date),
              MFC, font=MF)  # Дата рождения

    draw.text((WIDTH+719, SH + 375), genre, MFC, font=MF)  # Пол, genre

    draw.text((WIDTH, SH + 525), endt(birth_date), MFC,
              font=MF)  # Дата окончания действия документа

    draw.text((WIDTH, SH + 370), str(country).upper(), MFC, font=MF)  # Город

    # draw.text((WIDTH + 460, 770), str(personal_number).upper(), (178, 34, 34),
    #           font=ImageFont.truetype('media/cfg/font/sans.ttf', 40))

    draw.text((WIDTH, SH + 450), endt(data_start), MFC, font=MF)  # Дата выдачи

    draw.text((WIDTH+610, SH + 450), str('    United States \nDepartment of State'),
              MFC, font=MF)  # United States Department of State

    draw.text((WIDTH, SH + 600), 'SEE PAGE 24', MFC, font=MF)  # 123456789

    # draw.text((WIDTH + 489, SH + 402), '8099', MFC, font=MF)

    draw.text((120, SH + 700), str(mrz), MFC, font=FFMRZ)  # Добавляем mrz

    img.save(save_after_main_data)
    return save_after_main_data


def write_id(save_after_main_data_p, passport_number):
    font = ImageFont.truetype('media/cfg/font/SNEgCheck1MP.ttf', 120)

    print('чик чирык мазафака')
    line_height = sum(font.getmetrics())  # в нашем случае 33 + 8 = 41
    fontimage = Image.new('L', (font.getsize(passport_number)[0], line_height))
    # И рисуем на ней белый текст
    ImageDraw.Draw(fontimage).text(
        (0, 0), passport_number, fill=120, font=font)
    fontimage = fontimage.rotate(90, resample=Image.BICUBIC, expand=True)
    orig = Image.open(save_after_main_data_p)
    orig.paste((67, 67, 67), box=(30, 180), mask=fontimage)
    orig.save(save_after_main_data_p)
    return save_after_main_data_p


def holohrama_paster(passport_temp_path, holo_path):
    passport_temp = Image.open(passport_temp_path).convert('RGBA')
    img = Image.open(holo_path)  # открываем файл голограммы
    wpercent = (500 / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((500, hsize), Image.ANTIALIAS)
    if img.mode != 'RGBA':
        alpha = Image.new('RGBA', (10, 10), 20)
        img.putalpha(alpha)
    paste_mask = img.split()[3].point(lambda i: i * 17 // 100)
    passport_temp.paste(img, (140, SH + 310), mask=paste_mask)
    with_holo_path = f'media/cfg/tmp/usa/passport{random.randint(1000,9999)}.png'
    passport_temp.save(with_holo_path)
    return with_holo_path


def remove_background(image):
    img = Image.open(image).convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    image_no_bg_path = f'media/cfg/out/without_bg{random.randint(1000,9999)}.png'
    img.save(image_no_bg_path)
    return image_no_bg_path


def paste_photo(passport_temp_path, pasport_photo_path, exif_infor, background_path):
    passport_temp = Image.open(passport_temp_path).convert('RGBA')
    passport_photo = Image.open(pasport_photo_path).convert('RGBA')
    background = Image.open(background_path).convert('RGBA')
    print('Загружен фон ', background.size)
    width, height = passport_photo.size
    print('Размер фото в паспорте', passport_photo.size)
    new_height = 450  # Высота
    new_width = new_height * width // height
    print(new_width)
    passport_photo = passport_photo.resize(
        (new_width, new_height), Image.ANTIALIAS)
    if passport_photo.mode != 'RGBA':
        alpha_passpor_photo = Image.new('RGBA', (36, 25), 100)
        passport_photo.putalpha(alpha_passpor_photo)
    paste_mask_passport_photo = passport_photo.split()[
        3].point(lambda i: i * 90 // 100)
    print("pastemask", paste_mask_passport_photo)

    passport_temp.paste(passport_photo, (63, SH + 114),
                        mask=paste_mask_passport_photo)

    # img_lis = random.choice(os.listdir('media/cfg/sing_png'))
    # sing = Image.open("cfg/sing_png/" +
    #                   img_lis).resize((190, 140), Image.ANTIALIAS)
    # sing_passport_photo = sing.split()[
    #     3].point(lambda i: i * 90 // 100)
    # passport_temp.paste(sing, (950, SH + 800), mask=sing_passport_photo)
    im = Image.open(exif_infor)
    img_exif_data = im.getexif()
    passport_temp_crop = passport_temp.copy()
    w, h = passport_temp_crop.size
    nh = 500  # Высота
    nw = int(nh * w / h)
    im = passport_temp_crop.resize((nw, nh), Image.ANTIALIAS)
    im = passport_temp.copy()
    rad = 15
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    # im.putalpha(alpha)
    background_width, background_height = background.size
    passport_width, passport_height = im.size

    position = (int(background_width // 2 - passport_width // 2) + 200,
                int(background_height // 2 - passport_height // 2))
    # background_new = Image.new("RGBA", (passport_width+13,
    #                                     passport_height+13), (60, 60, 60))
    # background.paste(background_new, position)
    background.paste(im, position, mask=im)

    all_done_path = f'media/cfg/out/usavisa{random.randint(1000,9999)}.jpeg'
    print(all_done_path)
    background.convert('RGB').save(all_done_path, exif=img_exif_data,
                                   quality=10, subsampling=0)
    return all_done_path
