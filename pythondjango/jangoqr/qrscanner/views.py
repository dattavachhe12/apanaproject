import qrcode
from django.shortcuts import render
import qrcode
from .forms import QRCOdeForm
import os
from django.conf import settings
# Create your views here.
def h(request):
    if request.method=="POST":
        form=QRCOdeForm(request.POST)
        if form.is_valid():
            res_name=form.cleaned_data['restaurant_name']
            url=form.cleaned_data['url']
            print(res_name,url)

            #generate qr code
            qr=qrcode.make(url)
            file_name=res_name.replace(" ","_").lower()+'_menu.png'
            file_path=os.path.join(settings.MEDIA_ROOT,file_name) #media/rathan_rest_menu.png
            qr.save(file_path)
            #imageurl
            qr_url=os.path.join(settings.MEDIA_URL,file_name)

            context={
                'res_name':res_name,
                'qr_url':qr_url,
                'file_name':file_name,
            }
            return render(request,'qr_result.html',context)
    else:
       form=QRCOdeForm()
       context={
        'form':form,
    }
    return render(request,'h.html',context)

