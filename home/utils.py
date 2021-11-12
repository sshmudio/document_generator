from django.shortcuts import render


class ObjectsHomeMixin:
    model = None
    template = None

    def get(self, request):
        obj = self.model.objects.all()
        for value in obj:
            curr_balance = value.balance
            context = {
                self.model.__name__.lower(): obj
            }
        return render(request, self.template, context)
