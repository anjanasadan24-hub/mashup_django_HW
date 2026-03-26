

from django.shortcuts import render

def home(request):
    return render(request, 'insta.html')

def about(request):
    return render(request, 'about.html')

def employee_list(request):
    employees = [
        {"name": "Anjana", "job": "Developer", "salary": 50000, "full_time": True},
        {"name": "Rahul", "job": "Designer", "salary": 30000, "full_time": False},
        {"name": "Meena", "job": "Manager", "salary": 70000, "full_time": True},
    ]

    return render(request, 'emp.html', {"employees": employees})
def student_list(request):
    students = [
        {"name": "Anjana", "grade": 85, "passed": True},
        {"name": "Rahul", "grade": 40, "passed": False},
        {"name": "Meena", "grade": 72, "passed": True},
    ]

    return render(request, 'students.html', {"students": students})

def form(request):
    return render(request, 'form.html')

def result(request):
    username = request.GET.get('username', '')  # get data from GET request
    
    return render(request, 'result.html', {
        'username': username,
        'data': request.GET
    })
def vistor(request):
    return render(request, 'vistor.html')
def results(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            color = request.POST.get('color')
    
            return render(request, 'results.html',{
            'name': name,
            'color': color,
            'data': request.POST
            })

        return render(request, 'vistor.html')    
