from unicodedata import name
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from django.urls import is_valid_path
from . models import Student
from . forms import studentForm

# Create your views here.

def add_student(request):
 

    if request.method=='POST':
        new=studentForm(request.POST)
        retrieve_data=Student.objects.all()
        if new.is_valid():
            print("form validation")
            name=new.cleaned_data['name']
            email=new.cleaned_data['email']
            role=new.cleaned_data['role']
            db=Student(name=name,email=email,role=role)
            print(name,email,role)
            new.save()
        pass
    else:
           new=studentForm()
        
    retrieve_data=Student.objects.all()
    return render(request,'CrudeApp/create_read.html',{'forms':new,'data':retrieve_data})

# update operation

def update_data(request,id):
    
    if request.method=='POST':
        update=Student.objects.get(pk=id)
        new=studentForm(request.POST,instance=update)
        if new.is_valid():
            print("SuccessFully Updated")
            new.save()

    else:
        update=Student.objects.get(pk=id)
        new=studentForm()


        
    return render(request,'CrudeApp/update.html',{"form":new})


# delete operation 
def delete_data(request,id):
    if request.method=='POST':
        try:
            di=Student.objects.get(pk=id)
            di.delete()
        except:
            print("donot match in data base")
        
        print("deleted successfully")

        return HttpResponseRedirect('/')
