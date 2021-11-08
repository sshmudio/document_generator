from mrz.generator.mrva import MRVACodeGenerator, dictionary
from plow.potatoballs import write_main_data, write_id, paste_photo, holohrama_paster, remove_background
from plow.rand_let import issuing_d, exp_date_r, generator_unique_id
import random


def get_data_from_usa_visa(date_form):
    doc_type = date_form['doc_type']
    doc_country = date_form['doc_country']
    surname = date_form['surname']
    givenname = date_form['givenname']
    doc_number = date_form['doc_number']
    nationality = date_form['nationality']
    birthdate = date_form['birthdate']
    genre = date_form['genre']
    doc_exp_date = date_form['doc_exp_date']
    optional_data = date_form['optional_data']
    photo_document = date_form['photo_document']
    remove_bg = date_form['remove_bg']
    get_exif_info = date_form['get_exif_info']
    background_image = date_form['background_image']
    mrz = MRVACodeGenerator(doc_type, doc_country, surname, givenname,
                            doc_number, nationality, birthdate, genre, doc_exp_date, optional_data, transliteration=dictionary.latin_based(), force=False)
    print(mrz)
    path_save = 'media/cfg/tmp/usa/after_m_data.png'
    save_after_main_data_p = write_main_data(
        mrz,
        path_save,
        doc_type,
        doc_country,
        doc_number,
        surname,
        givenname,
        genre,
        birthdate,
        doc_exp_date,
        doc_number,
        doc_number,
    )

    print('путь после записи основных данных', save_after_main_data_p)

    write_id_path = write_id(save_after_main_data_p,
                             doc_number
                             )  # вставка id слева

    print('Путь после записи ID', write_id_path)

    temp_face_photo_path = f'media/cfg/tmp/usa/passport{random.randint(1000,9999)}.png'
    print('Сгенерирован путь к файлу фото лица', temp_face_photo_path)

    # face_after_crop_image = crop_face(
    #     pasport_photo_path, temp_face_photo_path)

    path_gg = 'media/cfg/template/holo.png'
    path_with_holohrama = holohrama_paster(write_id_path, path_gg)

    print('Отдаем темплейт с голограммой', path_with_holohrama)

    print('Отрезаем лицо')
    if remove_bg == True:
        path = remove_background(photo_document)
        print(path)
        all_done = paste_photo(save_after_main_data_p, path, get_exif_info, background_image)
        print(all_done)
    else:
        all_done = paste_photo(save_after_main_data_p, photo_document, get_exif_info, background_image)
        print('Путь к файлу готово', all_done)

    return all_done


