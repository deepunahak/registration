from django.shortcuts import render
from .forms import CreateStudentDetails
from cryptography.fernet import Fernet
from django.core.mail import send_mail
from .models import Student
from django.core.mail import send_mail


# Create your views here.


def register(request):
    form = CreateStudentDetails()
    if request.method == "POST":
        form = CreateStudentDetails(request.POST)
        if form.is_valid():
            student = form.save()

            key1 = Fernet.generate_key()
            f1 = Fernet(key1)
            student.email = f1.encrypt(student.email.encode())

            key2 = Fernet.generate_key()
            f2 = Fernet(key2)
            student.mobile = f2.encrypt(student.mobile.encode())
            student.save()

            recipient_email = f1.decrypt(student.email).decode()
            std_id = student.pk
            subject = 'Registration'
            message = 'Registration successfully with ' + recipient_email + "and student id is " + str(std_id)
            from_email = 'deepuranjannahak@gmail.com'
            send_mail(
                        subject,
                        message,
                        from_email,
                        [recipient_email],
                        fail_silently=True,
                    )
            render("student_registration/message.html")

    context = {'form': form}

    return render(request, 'student_registration/register.html', context)
