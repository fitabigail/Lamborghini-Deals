from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import EnquiryForm
from .form import UpdateInquiery


# Create Enquiry views here.


def inquiry_car(request):
    if request.method == 'POST':
        slug = request.POST['car_id']        
        user_id = request.POST['user_id']
        car_title = request.POST['car_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        enquiry_type = request.POST['enquiry_type']       
        city = request.POST['city']
        email = request.POST['email']        
        comment = request.POST['comment']

        if request.user.is_authenticated:
            user_id = request.user.id
            already_required = EnquiryForm.objects.all().filter(car_id=slug, user_id=user_id)
            if already_required:
                messages.error(request, 'You already sent a enquiry about this car. Soon we will contact you!')                
                return redirect('dashboard')

        inquiry = EnquiryForm(car_id=slug, user_id=user_id, car_title=car_title, first_name=first_name, last_name=last_name,
                              enquiry_type=enquiry_type, city=city,
                              email=email, comment=comment)

        inquiry.save()
        messages.success(request, 'Thank you for message,'
                         ' one of our team member will contact you shortly!')       
        return redirect('dashboard')
        
        
def update_inquiery(request, id):
    inquiery = EnquiryForm.objects.get(pk=id)
    form = UpdateInquiery(request.POST or None, instance=inquiery)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your inquery was update!')
        return redirect('dashboard')

    context = {
        'inquiery': inquiery,
        'form': form,
    }
    return render(request, 'accounts/inquiery_update.html', context)


def delete_inquiry(request, id):
    d_inquiry = get_object_or_404(EnquiryForm, pk=id)
    d_inquiry.delete()
    messages.success(request, 'Your inquery was removed!')
    return redirect('dashboard')


