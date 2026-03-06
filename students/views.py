from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Register User
def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully!")
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Check the form.")
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


# Student List
@login_required
def student_list(request):

    students = Student.objects.all()

    return render(request,'students/student_list.html',{'students':students})


# Add Student
@login_required
def student_add(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(request,'students/student_form.html',{'form':form})

# Edit Student
@login_required
def student_edit(request,id):

    student = get_object_or_404(Student,id=id)

    if request.method == "POST":

        form = StudentForm(request.POST,instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(request,'students/student_form.html',{'form':form})

# Delete Student
@login_required
def student_delete(request,id):

    student = get_object_or_404(Student,id=id)

    if request.method == "POST":
        student.delete()
        return redirect('student_list')

    return render(request,'students/student_confirm_delete.html',{'student':student})