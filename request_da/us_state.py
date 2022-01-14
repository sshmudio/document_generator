import random
from plow.state_usa_card import write_usa_state, paste_photo
from plow.remove_background import remove_background

def request_info_state_usa_card(date_form):
    passport_card_number = date_form['passport_card_number']
    nationality = date_form['nationality']
    surname = date_form['surname']
    given_names = date_form['given_names']
    sex = date_form['sex']
    date_of_birdth = date_form['date_of_birdth']
    place_of_birth = date_form['place_of_birth']
    issues_on = date_form['issues_on']
    expiries_on = date_form['expiries_on']
    documment_id = date_form['documment_id']
    photo_document = date_form['photo_document']
    remove_bg = date_form['remove_bg']
    img_exif = date_form['get_exif_info']
    background_path = date_form['background_image']
    save_after_main_data_p = write_usa_state(passport_card_number, nationality, surname, given_names, sex, date_of_birdth, place_of_birth, issues_on, expiries_on, documment_id)
    temp_face_photo_path = f'media/cfg/tmp/idcard{random.randint(1000,9999)}.png'
    print('путь после записи основных данных', temp_face_photo_path)
    
    if remove_bg == True:
        path = remove_background(photo_document)
        all_done = paste_photo(save_after_main_data_p, path, img_exif, background_path)
        return all_done
    else:
        all_done = paste_photo(save_after_main_data_p, photo_document, img_exif, background_path)
        print('Путь к файлу готово', all_done)

        return all_done


