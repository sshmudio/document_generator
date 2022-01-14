from django.shortcuts import render
from pathlib import Path
from wallets.models import UserBalance
import glob


class ObjectsHomeMixin:
    model = None
    template = None

    def get(self, request):
        objects = UserBalance.objects.filter(username=request.user)
        dirs = []
        p = Path('media/conf/')
        for x in p.iterdir():
            dirs.append(x.name)
        context = {
            'objects': objects,
            'dirs': dirs,

        }

        return render(request, self.template, context)


class ObjectsProfileMixin:
    model = None
    template = None

    def get(self, request):
        files = []
        for filepath in glob.iglob(f'media/out/{request.user}/**/*.png', recursive=True):
            files.append(filepath)
        print(files)
        context = {
            'objects': UserBalance.objects.filter(username=request.user),
            'files': files,

        }

        return render(request, self.template, context)
