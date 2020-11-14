from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image,Category

# Create your views here.

def my_images(request):
    images=Image.objects.all()
    return render(request,'all-photos/images.html',{"images":images})

# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

# def photos_of_day(request):
#     date = dt.date.today()
#     return render(request, 'all-photos/today-photos.html', {"date": date,})


# View Function to present photos from the previous days
def previous_days_photos(request, previous_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(previous_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/previous-photos.html', {"date": date})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})


def MyImage(request,image_id):
    try:
        image = Image.objects.get(Image,id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-photos/images.html", {"image":image})
