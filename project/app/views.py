from django.shortcuts import render,redirect # type: ignore
from .models import studentDB
from django.contrib import messages
# Create your views here.
def index(request):
    data=studentDB.objects.all()
    context={'data':data}
    return render(request,'index.html',context)

def insertData(request):
    data=studentDB.objects.all()
    context={'data':data}
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=studentDB.objects.create(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully..")
        return render(request,'index.html',context)
        
def deletedata(request,rid):
    data=studentDB.objects.get(id=rid)
    data.delete()
    messages.error(request,"Data Deleted Successfully..")
    return redirect('/')

def updatedata(request,rid):
    data=studentDB.objects.filter(id=rid)
    context={}
    if request.method == 'GET':
        context['d'] = data[0]
        return render(request,'update.html',context)
    else:    
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        print(gender)
        data.update(name=name,email=email,age=age,gender=gender)
        messages.warning(request,"Data Updated Successfully..")
        return redirect('/')

        

    
