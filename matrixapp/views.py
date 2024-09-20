from django.shortcuts import render

# Create your views here.

from .models import *



def index(request):
   

    
   return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'product.html')

def test(request):
    return render(request,'testimonial.html')




def dataget(request):
    
   
    bt=request.POST.get("btn")
    print("btn_value >>>>>>>>>>>>>",bt)
    data = { }
    if(request.POST.get("btn")):
    
        name1 = request.POST["name123"]
        if(name1==""):
           er={ "error":"Enter your name"}
         
           return render(request, 'form.html', context=er)
       
        email1 = request.POST["email123"]
         
        if(email1==""):
          er1={

            "error1":"Enter your email"
          }
          return render(request, 'form.html', context=er1)
        
        phone1 = request.POST["phone123"]
        
        if(phone1==""):
         er2={

            "error2":"Enter your phone number"
          }
         return render(request, 'form.html', context=er2)
      
        gender = request.POST.get("gen")

        if(gender==" "):
         er3={

            "error3":"Please select your gender"
          }
         return render(request, 'form.html', context=er3)

        hb2 = request.POST.get("text_h1")
        hb1 = request.POST.get("text_h2")
        ct = request.POST["cities"]
        Employee.objects.create(name=name1,email=email1,phone=phone1,gender=gender, hobby=hb1, city=ct)

        emp=Employee.objects.all()

        for e in emp:
         print("Name",e.name)
         print("Email",e.email)
         print("phone",e. phone)
         print("Gender",e.gender )
         print("Hobby",e.hobby )
         print("city",e.city )
        
        data = {
            "name" : name1,
            "email" : email1,
            "phone" : phone1,
            "gnd": gender,
            "hobby":hb1,
            "hobby2":hb2,
            "ct":ct
        }
   
    return render(request, 'form.html', context=data)
