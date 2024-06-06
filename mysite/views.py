from django.shortcuts import redirect, render


def about_us(request):
    return render(request,'mysite/about_us.html')
def contact_us(request):
    return render(request,'mysite/contact_us.html')





