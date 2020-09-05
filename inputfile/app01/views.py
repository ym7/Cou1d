from django.shortcuts import render,HttpResponse

# Create your views here.
import os
def input(request):
    if request.method == "GET":
        return render(request,"upload.html")
    else:
        try:
            files = request.FILES['files']
            with open(os.path.join("E:\\Uploadfiles",files.name), 'wb+') as destination:
                for chunk in files.chunks():
                    destination.write(chunk)
        except Exception:
            return render(request, "upload.html", {"msg": "请选择文件!!!!!!"})
        else:
            return HttpResponse("上传OK！")
