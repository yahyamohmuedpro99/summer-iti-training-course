from django.shortcuts import render,redirect
from .models import Task

# Logic of the app 

def task_creat(request):
    if request.method == 'POST':
        title=request.POST['title']
        description=request.POST['description']
        
        if title:
            Task.objects.create(title=title,description=description)
        return redirect('task_creat')
    
    
    # retirive logic
    tasks= Task.objects.all()
    return render(request,'task/task_temp.html',{'tasks':tasks})
        

    
"""
<QueryDict: 'title': ['dsfasdf']}>

"""

"""
tasks
- create -> post
- update -> patch /put
- list -> get
- delete -> delete



"""
