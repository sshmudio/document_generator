import os
import random
from typing import ValuesView
from PIL import Image, ImageDraw, ImageFont


MF = ImageFont.truetype('media/cfg/font/ArialNarrowBold.ttf', 45)  # Основной шрифт
FFMRZ = ImageFont.truetype('media/cfg/font/cour.ttf', 47)  # Шрифт для MRZ
SANS_S = ImageFont.truetype('media/cfg/font/sans.ttf', 40)
WIDTH = 100
SW = 576  # НАчальная ширина
SH = 100
MFC = (47, 47, 44)  # Основной цвет шрифта
defaulth = 240
 
def write_usa_state(passport_card_number, nationality, surname, given_names, sex, date_of_birdth, place_of_birth, issues_on, expiries_on, documment_id):
    img = Image.open('media/cfg/template/state_usa_card.png').convert('RGBA')  # Шаблон паспорта
    
    draw = ImageDraw.Draw(img)

    draw.text((890, 195), passport_card_number, MFC,  font=MF)

    draw.text((SW, defaulth), nationality, MFC, font=MF)  # Страна выдачи

    draw.text((SW, defaulth+70), surname, MFC, font=MF)  # Фамилия

    draw.text((SW, defaulth+155), given_names, MFC, font=MF)  # Имя влядельца документа

    draw.text((575, 241), nationality, MFC, font=MF)  # Гражданство
    
    draw.text((SW+145, defaulth+245), date_of_birdth, MFC, font=MF)  # Дата рождения
    
    draw.text((SW, defaulth+245), sex, MFC, font=MF)  # Пол

    # draw.text((116, 594), documment_id, MFC, font=MF)  # Персональный номер

    draw.text((SW, defaulth+335), place_of_birth, MFC, font=MF)  # Город

    draw.text((116, 650), documment_id, (17, 34, 34), font=SANS_S)

    draw.text((570, 662), issues_on, MFC, font=MF)  # Дата выдачи

    draw.text((900, 662), expiries_on, MFC, font=MF)  # Дата окончания
    temp_face_photo_path = f'media/cfg/tmp/idcard{random.randint(1000,9999)}.png'
    img.save(temp_face_photo_path)
    return temp_face_photo_path


def paste_photo(passport_temp_path, pasport_photo_path, exif_infor, background_path):
    passport_temp = Image.open(passport_temp_path).convert('RGBA')
    passport_photo = Image.open(pasport_photo_path).convert('RGBA')
    background = Image.open(background_path).convert('RGBA')
    print('Загружен фон ', background.size)
    width, height = passport_photo.size
    new_height = 345  # Высота
    new_width = int(new_height * width / height)
    print(new_width)
    passport_photo = passport_photo.resize(
        (new_width, new_height), Image.ANTIALIAS)
    if passport_photo.mode != 'RGBA':
        alpha_passpor_photo = Image.new('RGBA', (14, 14), 100)
        passport_photo.putalpha(alpha_passpor_photo)
    paste_mask_passport_photo = passport_photo.split()[
        3].point(lambda i: i * 90 // 100)
    print(paste_mask_passport_photo)

    passport_temp.paste(passport_photo, (80, SH + 125),
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
    nh = 900  # Высота
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

    all_done_path = f'media/cfg/out/idcard{random.randint(1000,9999)}.png'
    print(all_done_path)
    background.save(all_done_path, exif=img_exif_data, quality=20, subsampling=0)
    return all_done_path


# write_main_data('A8928398293', 'USA', 'John', 'Ebobo', 'M', '21 JAN 1986',
#                 'NEW YORK USA', '21 JAN 2006', '21 JAN 2020', 'A12345', 'Pathpath')

# paste_photo('media/cfg/template/state_usa_card.png' , 'media/cfg/input/lebed.jpg', 'media/cfg/background_image/IMG_20211008_152436.jpg', 'media/cfg/background_image/IMG_20211008_152436.jpg')
