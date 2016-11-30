from django.shortcuts import render

def index(request):
    return render(request, 'personal_web/home.html') # this files are in "personal_web> templates>"  but some time this can cause name conflicts
    #so use following line instead
    #create sub folder in "personal_web>templates>subfolder-name
    #return render(request, 'subfolder-name/home.html'). In my code, I have given personal_web name to subfolder.

def contact(request):
    return render(request, 'personal_web/basic.html', {'content':['to contact, email me','abcd@xyz.com']})
