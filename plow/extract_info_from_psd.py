# -*- coding: utf-8 -*-

from psd_tools import PSDImage
from glob import glob
from pathlib import Path
import json
import logging

# from psd_tools.user_api import layers
logging.basicConfig(level=logging.INFO)


def get_info_layers(dir_file):
    file_list = glob(dir_file)
    logging.info('Ищу файфы')
    for file in file_list:
        logging.info('Делаю человеческими')
        normalization_file_name = Path(file).name.replace('.psd', '')
        psd = PSDImage.load(file)
        ppsd = list(psd.descendants())
        adv_layers = ppsd.__iter__()
        psd_file = normalization_file_name.encode('ascii', 'ignore').decode("utf-8")
        p = Path(f'conf/{psd_file}')
        print(p)
        p.mkdir(mode=755, parents=True, exist_ok=True)
        logging.info('Зелал папку')

        with open(f'conf/{psd_file}/{psd_file}.json', "a+") as outfile:
            for layer in adv_layers:
                # layer_name = str(layer.name).encode('ascii', 'ignore').decode("utf-8").replace(' ', '')

                cfg = {
                    'file_name': str(psd_file),
                    'layers_name': str(layer.name),
                    # 'layout_text': str(layer),
                    'name': str(layer.name),
                    'ltype': str(layer.kind),
                    'x1': str(layer.bbox.x1),
                    'y1': str(layer.bbox.y1),
                    'opacity': str(layer.opacity),
                    'width': str(layer.bbox.width),
                    'height': str(layer.bbox.height),
                    'visible': str(layer.visible),
                    # 'blend_mode': str(layer.blend_mode),
                    'clip_layers': str(layer.clip_layers)
                }
                json.dump(cfg, outfile, indent=4, ensure_ascii=False)
                logging.info('Сохранил конфиг')
                lays_name = str(layer.name).encode('ascii', 'ignore').decode("utf-8").replace(' ', '')
                logging.info('Переименовал слои')
                # print(lays_name)
                la_img = psd.as_PIL()
                try:
                    logging.info('_______________Пробую сохранить____________________')
                    files_for_save_layer = f'conf/{psd_file}/{lays_name}ly.png'
                    print('Сохранилось', files_for_save_layer)

                except Exception:
                    pass
                    # print('Ошибка делаю способ 2', ke)
                    # logging.info('__________Пробую сохранить после первой неудачи_______')
                    # files_for_save_layer = f'conf/{psd_file}/fainl_bt_gen.png'
                    # print('Сохранилось')
                # try:
                #     la_img.save(files_for_save_layer)
                # except KeyError:
                #     la_img.save(f'conf/{psd_file}/fail_but_gen.png')

                logging.info('Сохранил слойи')
                # print('результат при получении запроса на сейв', la_img)


get_info_layers('/opt/document_generator/media/cfg/PSD/**/*.psd')
