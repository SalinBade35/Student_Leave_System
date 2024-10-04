from django.shortcuts import render, redirect
from .models import StudentLeave
from django.contrib import messages

def home(request):
    return render(request, 'crudApp1/home.html')

def form(request):
    # if request.method == 'POST' and request.FILES:
    if request.method == 'POST':
        roll_number = request.POST.get('rollNumber')
        full_name = request.POST.get('fullName')
        faculty = request.POST.get('faculty')
        semester = request.POST.get('semester')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        leave_type = request.POST.get('leaveType')
        reason = request.POST.get('reason')
        document = request.FILES.get('document')
        guardian_contact = request.POST.get('guardianContact')
        student_contact = request.POST.get('studentContact')
        
        # # Validate semester for Architecture faculty
        # if faculty.lower() == 'architecture' :
        #     if not (1 <= int(semester) <= 10):  # Check if semester is between 1 and 10
        #         messages.error(request, "For Architecture, semester must be between 1 and 10.")
        #         return redirect('form')
        # else:  # For other faculties
        #     if not (1 <= int(semester) <= 8):  # Check if semester is between 1 and 8
        #         messages.error(request, "For other faculties, semester must be between 1 and 8.")
        #         return redirect('form')

        # Create a new StudentLeave object if validations pass
        StudentLeave.objects.create(
            roll_number=roll_number,
            full_name=full_name,
            faculty=faculty,
            semester=semester,
            start_date=start_date,
            end_date=end_date,
            leave_type=leave_type,
            reason=reason,
            document=document,
            guardian_contact=guardian_contact,
            student_contact=student_contact
        )
        
        # Extract the first name from full_name
        first_name = full_name.split()[0] if full_name else "User"  # Default to "User" if full_name is empty

        # Display the success message with the first name
        messages.success(request, f"Hey, {first_name.capitalize()}! Your Leave Form Is Successfully Submitted!!!")

        return redirect('form')  # Redirect to the form page after submission
        
    return render(request, 'crudApp1/form.html')

def about(request):
    return render(request, 'crudApp1/about.html')

def contact(request):
    return render(request, 'crudApp1/contact.html')



def home(request):
    # to Fetch all student leave records
    student_leaves = StudentLeave.objects.all()   # it is called query set

    # to Pass the records to the template
    return render(request, 'crudApp1/home.html', {'student_leaves': student_leaves})
