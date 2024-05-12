from django.shortcuts import render
from employee.models import Employee,Department
from employee.forms import EmployeeForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,"home.html")

def list(request):
    l=Employee.objects.all()
    return render(request,'emp list.html',{'emp':l})

def detailedview(request,n):
    d=Employee.objects.get(id=n)
    return render(request,'DetailedView.html',{'d':d})

# def addemployee(request):
#     if(request.method=="POST"):
#         form=EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     form=EmployeeForm()
#     return render(request,'addemployee.html',{'form':form})


def addemployee(request):

    if(request.method=="POST"):
        i=request.POST['i']
        n=request.POST['n']
        a=request.POST['a']
        ad=request.POST['ad']
        cn=request.POST['cn']
        jd=request.POST['jd']
        d=request.POST['d']
        dp=request.POST['dp']

        e=Employee.objects.create(emp_id=i,emp_name=n,emp_age=a,emp_address=ad,emp_contact_no=cn,emp_joining_date=jd,emp_designation=d,d_name=dp)
        e.save()
        return list(request)
    return render(request,'addemployee.html')


def update(request,n):
    e=Employee.objects.get(id=n)
    if(request.method=="POST"):
        form=EmployeeForm(request.POST,instance=e)
        if form.is_valid():
            form.save()
            return list(request)
    form=EmployeeForm(instance=e)
    return render(request,'addemployee.html',{'form':form})

def delete(request,n):
    e=Employee.objects.get(id=n)
    e.delete()
    return list(request)

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']

        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if(cp==p):
            user=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            user.save()
            return list(request)
        else:
            return HttpResponse("Passwords are not match")

    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)

        if user:
            login(request,user)
            return list(request)
        else:
            return HttpResponse("Invlid Credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return user_login(request)

