# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from wallets.forms import BtcGenForm
# from wallets.btcgate import gen_address


# def billing(request):
#     if request.method == 'POST':
#         form = BtcGenForm(request.POST)
#         if form.is_valid():
#             form.save()
#             gen_address(form.changed_data)
#             return HttpResponseRedirect('/billing/')
#     else:
#         form = BtcGenForm()
