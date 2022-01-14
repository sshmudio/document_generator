from psd_tools import PSDImage
psd = PSDImage.open('USA/usa1.psd')
for layer in psd:
    ln = layer['NewNew'] = 'olds'
    # layer.name = 'NewNew'
    print(layer.name)
    # if layer.is_group():
    #     for child in layer:
    #         print(child)

child = psd[0][0]
