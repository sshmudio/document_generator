# import easyocr
# # this needs to run only once to load the model into memory
# reader = easyocr.Reader(['en', 'en'])
# result = reader.readtext('id_state_temp.png', detail=1)
# print(result)

from psd_tools.api.numpy_io import get_image_data
from psd_tools.api.psd_image import PSDImage
from psd_tools.psd.engine_data import DictElement
from psd_tools.psd.image_resources import ImageResources
# from psd_tools.constants import Resource

psd = PSDImage.open('USA/state_ing_usa.psd')
for layer in psd:
    if layer.kind == 'type':
        print(layer.text)
        print(layer.engine_dict['StyleRun'])

        # Extract font for each substring in the text.
        text = layer.engine_dict['Editor']['Text'].value
        fontset = layer.resource_dict['FontSet']
        runlength = layer.engine_dict['StyleRun']['RunLengthArray']
        rundata = layer.engine_dict['StyleRun']['RunArray']
        index = 0
        for length, style in zip(runlength, rundata):
            substring = text[index:index + length]
            stylesheet = style['StyleSheet']['StyleSheetData']
            font = fontset[stylesheet['Font']]
            print('%r gets %s' % (substring, font))
            index += length
# for x in psd.image_resources:
#     print(x.get_data)
# if psd.is_visible():
#     for layer in psd.descendants():
#         print('Имя слоя: ', layer.name, 'Левая координата: ',
#               layer.left, 'Правая координата: ', layer.right, 'Слева сверху: ', layer.offset, '(ширина, высота) кортеж: ', layer.size)

#     # Iterate over all layers in reverse order
#     for layer in reversed(list(psd.descendants())):
#         print(layer)
