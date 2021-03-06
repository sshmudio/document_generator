from django.shortcuts import render
from pathlib import Path
from wallets.models import UserBalance, UserHistory
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
            'history': UserHistory.objects.filter(user=request.user),

        }

        return render(request, self.template, context)


class ObjectsProfileMixin:
    model = None
    template = None

    def get(self, request):
        files = []
        for filepath in glob.iglob(f'media/{request.user}/done-*.png', recursive=True):
            files.append(filepath)
        context = {
            'objects': UserBalance.objects.filter(username=request.user),
            'files': files,
            'files_name': str([x for x in files]).replace(f'media/{request.user}/', ''),

        }

        return render(request, self.template, context)
