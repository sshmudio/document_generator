import os
import json
from werkzeug.utils import secure_filename
from passporteye.mrz.image import MRZPipeline
from passporteye import read_mrz
from PIL import Image
import pytesseract
import cv2
import numpy as np
import re


def process(full_path):
    p = MRZPipeline(full_path, extra_cmdline_params='--oem 0')
    mrz = p.result
    mrz_data = mrz.to_dict()
    full_content = image_to_string(full_path)
    all_infos = {}
    all_infos['last_name'] = mrz_data['surname']
    all_infos['first_name'] = mrz_data['names']
    all_infos['country_code'] = mrz_data['country']
    all_infos['country'] = get_country_name(all_infos['country_code'])
    all_infos['nationality'] = get_country_name(mrz_data['nationality'])
    all_infos['number'] = mrz_data['number']
    all_infos['sex'] = mrz_data['sex']
    all_infos['full_text'] = full_content
    valid_score = mrz_data['valid_score']
    print('valid_score', valid_score)
    if all_infos['last_name'] in full_content:
        splitted_fulltext = full_content.split("\n")
        for w in splitted_fulltext:
            if all_infos['last_name'] in w:
                all_infos['last_name'] = w
                continue

    splitted_firstname = all_infos['first_name'].split(" ")
    if splitted_firstname[0] in full_content:
        splitted_fulltext = full_content.split("\n")
        for w in splitted_fulltext:
            if splitted_firstname[0] in w:
                all_infos['first_name'] = clean_name(w)
                continue

    os.remove(full_path)
    return all_infos


def get_country_name(country_code):
    with open('countries.json') as json_file:
        data = json.load(json_file)
        for d in data:
            if d['alpha-3'] == country_code:
                return d['name']
    return country_code


def clean_name(name):
    pattern = re.compile('([^\s\w]|_)+')
    name = pattern.sub('', name)
    return name.strip()


def image_to_string(img_path):
    img = cv2.imread(img_path)
    file_name = os.path.basename(img_path).split('.')[0]
    file_name = file_name.split()[0]
    output_path = file_name
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    save_path = os.path.join(output_path, file_name + "_filter.jpg")
    cv2.imwrite(save_path, img)
    result = pytesseract.image_to_string(img, lang="eng")

    os.remove(save_path)
    print(result.upper())
    return result.upper()


if __name__ == "__main__":
    path = 'usa1.png'
    process(path)
    country = image_to_string(path)
