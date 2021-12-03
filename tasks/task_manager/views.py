from django.shortcuts import redirect, render
from .models import Tasks
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.
@login_required
def CreateTask(request):
    username = request.user.username
    email = request.user.email
    if request.method == 'POST':
        task_title=request.POST.get('task_title')
        task_description = request.POST.get('task_description')
        #img_file = request.FILES['task_img']
        user = User.objects.get(username=request.user.username)
        new_task=Tasks.objects.create(user_id=user,task_title=task_title,task_description=task_description,time_stamp=timezone.now())
        new_task.save()
        return HttpResponse("Task added successfully!")
    return render(request,'tasks/createtask.html',{'username':request.user.username,'email':request.user.email})

@login_required
def ViewTask(request):
    data=[]
    # result=Tasks.objects.all().filter(user_id__icontains=request.user.username)
    result=Tasks.objects.all().filter(user_id__username=request.user.username)
    if len(result)!=0:
        for task in range(len(result)):
            data.append((result[task].task_title,result[task].task_id))
        
        return render(request,'tasks/view_task.html',{'result':data})
    else:
        return HttpResponse("No tasks found")

def DetailedTasksView(request,slug,pg_id=1):
    try:
        result=Tasks.objects.get(task_id=slug,user_id__username=request.user.username)
        # if len(result)>5:
        #     DetailedTasksView(request,slug,pg_id+1)
        t_name=result.task_title
        t_id=result.task_id
        t_desc=result.task_description
    except:
        return HttpResponse("No such task found")
    
    return render(request,'tasks/detailed_task.html',{'t_name':t_name,'t_id':t_id,'time_stamp':result.time_stamp,'t_desc':t_desc})