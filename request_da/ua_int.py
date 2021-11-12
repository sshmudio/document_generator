from plow.plow import *
from plow.rand_let import issuing_d, exp_date_r, generator_unique_id
import random


def get_data_from_form(date_form):
    # typedoc = date_form['typedoc']
    country = 'UKR'
    surname = date_form['surname']
    given_name = date_form['given_name']
    passport_number = date_form['passport_number']
    genre = date_form['genre']
    nationality = 'UKRAINE'
    birth_date = date_form['birth_date']
    personal_number = str(generator_unique_id())
    locations = date_form['locations']
    # id_number = date_form['id_number']
    img_exif = date_form['get_exif_info']
    background_path = date_form['background_image']
    # issuing = exp_date()
    pasport_photo_path = date_form['photo_doc']
    # background = date_form['background']
    remove_bg = date_form['remove_bg']
    bdate_for_mrz = birth_date[2::]
    print(bdate_for_mrz)
    data_start = issuing_d(bdate_for_mrz)
    exp_date = exp_date_r(data_start)

    mrz = TD3CodeGenerator('P', country, surname, given_name, passport_number, nationality,
                           bdate_for_mrz, genre, exp_date, passport_number, dictionary.cyrillic_ukrainian())

    save_after_main_data_p = write_main_data(mrz, f'media/cfg/tmp/after_m_data{random.randint(1000,9999)}.png', 'P', country, passport_number, surname, given_name, genre, birth_date,
                                             data_start, exp_date, personal_number)
    print('путь после записи основных данных', save_after_main_data_p)
    write_id_path = write_id(save_after_main_data_p,
                             passport_number)  # вставка id слева
    print('Путь после записи ID', write_id_path)

    temp_face_photo_path = f'media/cfg/tmp/passport{random.randint(1000,9999)}.png'
    print('Сгенерирован путь к файлу фото лица', temp_face_photo_path)
    # face_after_crop_image = crop_face(
    #     pasport_photo_path, temp_face_photo_path)
    path_gg = 'media/cfg/template/holo.png'
    path_with_holohrama = holohrama_paster(save_after_main_data_p, path_gg)

    print('Отдаем темплейт с голограммой', path_with_holohrama)

    if remove_bg == True:
        image_no_bg_path = remove_background(pasport_photo_path)
        all_done = paste_photo(path_with_holohrama,
                               image_no_bg_path, img_exif, background_path)
    else:
        all_done = paste_photo(path_with_holohrama,
                               pasport_photo_path, img_exif, background_path)
        print('Путь к файлу готово', all_done)

    return all_done
