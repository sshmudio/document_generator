from psd_tools import PSDImage
import glob
from pathlib import Path


def search_file(dirs):
    for x in glob.glob(dirs, recursive=True):
        name_file = Path(x).name
        normal_file_list = name_file.replace(' ', '_')
        print(normal_file_list)
    return normal_file_list


def working_psd(image_psd):
    psd = PSDImage.open(image_psd)
    image = psd.compose()

    for layer in psd:
        layer_image = layer.compose()


def create_info_files(file_name):
    with open(file_name, 'w')as info_file:
        info_file.write()


def main():
    image_psd = search_file('USA/*.psd')
    after_psd = working_psd(image_psd)


if __name__ == '__main__':
    main()
