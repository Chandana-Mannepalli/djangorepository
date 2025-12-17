from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
def view1(request):
    return HttpResponse("i am view1")
def view2(request):
    return HttpResponse("i am view2")
def view3(request):
    return HttpResponse("i am view3")
def view4(request):
    return JsonResponse({"name":"chandana","age":22})
def view5(request):
    return JsonResponse({"name":"Triveni","age":22}) #static response  

# dynamic queries wih the help of query parameters

def dynamicview(request):
    qp1=request.GET.get("name") 
    return HttpResponse(f"hello {qp1}")

def personInfo(request):
    name=request.GET.get("name","chan")
    city=request.GET.get("city","kmm")
    role=request.GET.get("role","student")
    info={"name":name,"city":city,"role":role}
    return JsonResponse({"status":"success","data":info})

# dynamic JSON respomse using query parameter
def movieBooking(request):
    movie=request.GET.get("movie","Akanda-2")
    showtime=request.GET.get("showtime","6PM")
    ticketcost=request.GET.get("ticketcost",250)
    total_number_of_tickets=request.GET.get("total_number_of_tickets",4)
    total_price=request.GET.get("total_price",1000)
    info={"movie":movie,"showtime":showtime,"ticketcost":ticketcost,"total_number_of_tickets":total_number_of_tickets,"total_price":total_price}
    return JsonResponse({"status":"success","data":info})

# html template using rendor
def temp(request):
    return render(request,'./first.html/')
