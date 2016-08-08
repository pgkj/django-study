from django.shortcuts import render,  render_to_response
from restaurants.models import Restaurant, Food, Comment
from django.http import HttpResponse, HttpResponseRedirect
import datetime
# Create your views here.
def menu(request):
	if 'id' in request.GET:
		print(type(request.GET['id']))
		r = Restaurant.objects.get(id=request.GET['id'])
		return render_to_response('menu.html', locals())
	else:
		return HttpResponseRedirect("/restaurants_list/")

def meta(request):
    values = request.META.items()  # Meta is the header of request: key-values -> array

    values.sort()                  # sort array

    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def welcome(request):
    if 'user_name' in request.GET:
        return HttpResponse('Welcome!~ ' + request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())

def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurants_list.html', locals())

def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if 'ok' in request.POST:
        print("it is a POST request, we have to create the data using the post!!!")
        user = request.POST['user']
        content = request.POST['content']
        email = request.POST['email']
        date_time = datetime.datetime.now() # get the current time

        Comment.objects.create(user=user, email=email, content=content, date_time=date_time, restaurant = r)
    else:
        print("no post so just return the current comments")
    return render_to_response('comments.html', locals())
