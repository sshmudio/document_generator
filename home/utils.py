from django.shortcuts import render
from pathlib import Path
from wallets.models import UserBalance


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
