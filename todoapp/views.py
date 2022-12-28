from django.shortcuts import render
from django.http import HttpResponse
from .models import user,task
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            print('Password not matched!',password1,password2)
            return render(request,'signuppage.html',context={'status':"0"})
        else:
            users=user.objects.all()
            for u in users:
                if u.email==email:
                    print('already exits')
                    return render(request,'index.html',context={'status':"1"})
            
            newUser=user(fname=fname,lname=lname,email=email,password=password1)
            newUser.save()
            return render(request,'index.html',context={'status':"2"})
    

def addtask(request):
    if request.method=='POST':
        addtask=request.POST.get('task')
        adddesc=request.POST.get('desc')
        email=request.POST.get('email')
        # print(addtask,adddesc,email)
        users=user.objects.all()
        # print(users)
        for u in users:
            if u.email==email:
                context={'lname':u.lname,'fname':u.fname,'email':u.email}
        t=task(taskname=addtask,taskdesc=adddesc,email=email,dateadded=timezone.now())
        t.save()
    return render(request,'home.html',context=context)

def navtoaddtask(request):
    email=request.POST.get('email')
    users=user.objects.all()
    for u in users:
        if u.email==email:
            context={'lname':u.lname,'fname':u.fname,'email':u.email}
    return render(request,'home.html',context=context)

def showtask(request):
    email=request.POST.get('email')
    users=user.objects.all()
    for u in users:
        if u.email==email:
            context={'lname':u.lname,'fname':u.fname,'email':u.email}
    tasks=task.objects.all()
    arr=[]
    for t in tasks:
        if t.email==email:
            arr.append(t)
    context['task']=arr
    # print(context)
    return render(request,'task.html',context=context)

def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    # print(email,password)
    users=user.objects.all()
    for u in users:
        if u.email==email and u.password!=password:
            return render(request,'index.html',context={'status':"4"})
        elif u.email==email and u.password==password:
            context={'lname':u.lname,'fname':u.fname,'email':u.email}
            return render(request,'home.html',context=context)
    return render(request,'index.html',context={'status':"3"})

def logout(request):
    return render(request,'index.html')


# To delete the task for the user
def statusChange(request):
    temp=request.POST.get('changestatus').split('+')
    tasks=task.objects.all()
    for t in tasks:
        if t.email==temp[0] and t.taskId==int(temp[1]):
            t.delete()
    email=temp[0] 
    users=user.objects.all()
    for u in users:
        if u.email==email:
            context={'lname':u.lname,'fname':u.fname,'email':u.email}
    tasks=task.objects.all()
    arr=[]
    for t in tasks:
        if t.email==email:
            arr.append(t)
    context['task']=arr
    # print(context)
    return render(request,'task.html',context=context)
    
def signuppage(request):
    return render(request,'signuppage.html')

def loginpage(request):
    return render(request,'index.html')