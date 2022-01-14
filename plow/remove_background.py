import random
from PIL import Image

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
    print('Сгенерировано лицо без фона', image_no_bg_path)
    img.save(image_no_bg_path)
    return image_no_bg_path
