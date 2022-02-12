from django.shortcuts import render
from . import forms

# Create your views here.


def feedback_view(request):
    if request.method=='GET':
        form=forms.FeedbackForm()

    if request.method=='POST':
        form=forms.FeedbackForm(request.POST)
        if form.is_valid():
            print("validation successfull printing the data")
            print("Student Name",form.cleaned_data['name'])
            print("Student Rollno",form.cleaned_data['rollno'])
            print("Student Mailid",form.cleaned_data['email'])
            print("Student Feedback",form.cleaned_data['feedback'])
            return render(request,'testapp/thankyou.html')
    return render(request,'testapp/feedback.html',{'form':form})
