from psd_tools import PSDImage

psd = PSDImage.open(
    '/home/user/MEGAcmd/sdk/examples/PSD/Passports/+indonesia.psd')
for layer in psd:
    print(layer)
    try:
        print(layer.text)

    except:
        print('ff')
    if layer.is_group():
        for child in layer:
            print(child.name)


child = psd[0][0]
