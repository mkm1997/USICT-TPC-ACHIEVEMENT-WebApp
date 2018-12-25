from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Achivements,Student
from .forms import AchievementForm
import json

# Create your views here.


def display(request):
    ach_obj = Achivements.objects.filter(is_verified = True)

    #print(ach_obj.student.all())

    #stobj = Student.objects.filter()

    return render(request,'display.html',{"obj":ach_obj})

@csrf_exempt
def verificationListView(request):
    if request.user.is_superuser:
        if request.method == "POST": #post request for verification
            print(request.POST.get("id"))
            try:
                obj = Achivements.objects.get(id=request.POST.get("id"))
                obj.is_verified = True
                obj.save()
            except Exception as e:
                return HttpResponse(str(e))
            return HttpResponse("Verified Successfully")
        ach_obj = Achivements.objects.filter(is_verified=False)
        print(ach_obj)

        return render(request,'display_for_verification.html',{"obj":ach_obj})
    else:
        return HttpResponse("<h1>you have not permission to verify</h1>")

@csrf_exempt
def achievementForm(request):
    if request.method == "POST":
        data = request.POST.dict()
        name = []
        enroll = []
        try:
            file = request.FILES["file"]
        except:
            file =None

        ach_obj = Achivements(image=file,heading=data["heading"],discription=data["discription"])
        ach_obj.save()

        for i in sorted(data.keys()):
            if (i.startswith("name")):
                name.append(data[i])
            if i.startswith("eno"):
                enroll.append(data[i])
        print(name)
        print(enroll)
        for i in range(len(name)):
            obj = Student(name=name[i],e_no=enroll[i])
            obj.save()
            ach_obj.student.add(obj)
            ach_obj.save()


        return HttpResponse("submitted successfully")
    else:
        return render(request,"achieve_form.html")








