from django.contrib import messages
from django.shortcuts import render
from .models import Insurance
from django.views import View
from .forms import UserInfoForm, InsuranceForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date, timedelta


class UserInfoClass(View):
    def get(self, request):
        if (not request.user.is_authenticated) or (request.user.is_superuser):
            return render(request, 'index.html')
        form = UserInfoForm()

        return render(request,'info.html',{
            'form':form
        })

    def post(self, request):
        form = UserInfoForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            user_info=form.save(commit=False)
            user_info.username=request.user
            user_info.save()
            return HttpResponseRedirect(reverse("success"))
        print(form.errors)
        return render(request, 'info.html', {
            'form': form
        })
class InsuranceRequest(View):
    def get(self, request):
        print('what')
        form = InsuranceForm()
        return render(request , 'requestform.html',{
            'form':form
        })
    def post(self, request):
        print("Post method triggered")
        form = InsuranceForm(request.POST)
        if form.is_valid():
            print("view")
            insurance_info=form.save(commit=False)
            insurance_info.user=request.user
            insurance_info.save()
            return HttpResponseRedirect(reverse("success"))
        print("Form errors:", form.errors)
        return render(request, 'requestform.html', {
            'form': form
        })
class SignUpClass(View):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'signup.html', {
            'form': form
        })

    def post(self, request,):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, "ثبت نام شدی ",'success')
            return HttpResponseRedirect(reverse("login"))
        print('bad entry')
        print(form.errors)
        return render(request, 'signup.html', {
            'form': form,
            "err":form.errors
        })
class LoginClass(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {
            'form': form
        })
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            print(form.cleaned_data)
            return HttpResponseRedirect("/index")
        print('bad entry')
        return render(request, 'login.html', {
            'form': form
        })

def StartingPage(request):
    return render(request,'index.html')
def historytables(request):
    obj = Insurance.objects.filter(user=request.user)
    empty = False
    if len(obj) == 0:
        empty = True
    return render(request, "insurance_table.html" ,{
        'insurances':obj,
        'empty':empty
    })


def extends(request):
    if request.method == "POST":
        insurance_id = request.POST.get("insurance_id")

        # Fetch the insurance object
        insurance = get_object_or_404(Insurance, id=insurance_id)

        # Update the status based on the action
        insurance.status = "accepted"
        insurance.expired_date=date.today()+timedelta(days=30)
        insurance.save()
        return HttpResponseRedirect(reverse("index"))
    insurances = Insurance.objects.filter(user=request.user)
    obj = [insurance for insurance in insurances if insurance.time_left < 30 and insurance.status=='accepted']
    empty=False
    if len(obj) == 0:
        empty=True
    return render(request, 'extends.html', {
        'insurances': obj,
        'empty': empty
    })






def admin_requests(request):
    all_requests = Insurance.objects.filter(status="checking")
    empty = False
    if len(all_requests) == 0:
        empty = True
    return render(request,'accept.html',{'all_requests':all_requests,
                                         'empty':empty})


def process_request(request):
    if request.method == "POST":
        insurance_id = request.POST.get("insurance_id")
        action = request.POST.get("action")

        # Fetch the insurance object
        insurance = get_object_or_404(Insurance, id=insurance_id)

        # Update the status based on the action
        if action == "accept":
            insurance.status = "accepted"
            insurance.accepted_date=date.today()

        elif action == "reject":
            insurance.status = "rejected"

        insurance.save()

        # Redirect back to the admin requests page
        return HttpResponseRedirect(reverse("accept"))

def success(request):
    return render(request,'successful.html')