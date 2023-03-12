from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EnquiryForm

# Create your views here.


def inquiry_car(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        enquiry_type = request.POST['enquiry_type']
        state = request.POST['state']
        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']

        if request.user.is_authenticated:
            user_id = request.user.id
            already_required = EnquiryForm.objects.all().filter(car_id=car_id, user_id=user_id)
            if already_required:
                messages.error(request, 'You already sent a enquiry about this car. Soon we will contact you!')
                return redirect('/car_view/'+car_id)

        inquiry = EnquiryForm(car_id=car_id, car_title=car_title,
        user_id=user_id, first_name=first_name, last_name=last_name,
        enquiry_type=enquiry_type, state=state, city=city,
        email=email, phone=phone, comment=comment)

        inquiry.save()
        messages.success(request, 'Thank you for message,'
        ' one of our team member will contact you shortly!')
        return redirect('/car_view/'+car_id)