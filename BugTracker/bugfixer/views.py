from .models import Ticket
from .forms import Createticket, Edit
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import Datepicker
from datetime import date, timedelta



def index(request):
    user_invalid = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return home(request)
        else:
            if user is None:
                user_invalid = True
                return render(request, 'index.html', {'user_invalid': user_invalid} )
    else:
        if request.method == 'GET':
            if request.user.is_authenticated:
                return home(request)
            else:
                return render(request, 'index.html')
        


def home(request):  
    if request.user.is_authenticated:
        start_date = date.today() - timedelta(days = 14)
        end_date =  date.today()
        open_tickets = Ticket.objects.filter(date__gte = start_date, date__lte = end_date, status='OPEN').count()
        ip_tickets = Ticket.objects.filter(date__gte = start_date, date__lte = end_date, status='IN PROGRESS').count()
        ir_tickets = Ticket.objects.filter(date__gte = start_date, date__lte = end_date, status='REVIEW').count()                
        closed_tickets = Ticket.objects.filter(date__gte = start_date, date__lte = end_date, status='CLOSED').count()
        tickets = Ticket.objects.all().exclude(status="CLOSED").order_by('-date')
        return render(request, 'home.html', {'tickets': tickets, 'open_tickets': open_tickets, 'ip_tickets': ip_tickets, 'ir_tickets': ir_tickets, 'closed_tickets':closed_tickets, 'start_date':start_date, 'end_date':end_date})
    else:
        return redirect('/index')

    


def redirect(request):
    return HttpResponseRedirect("/bugfixer/")


def ticket_create(request):
    form = Createticket(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.created = request.user
                ticket.save()
                messages.success(request, "Successfully created")
                return redirect('/home')
            
        else:
            if request.method == 'GET':
                return render(request, 'createticket.html', {'form': form})
    else:
        return redirect('/index')


def ticket_view(request, ticket_number):
    if request.user.is_authenticated:
        ticket_to_display = Ticket.objects.get(id=ticket_number)
        return render(request, 'ticketdetails.html', {'ticket_to_display': ticket_to_display})
    else:
        return redirect('/index')


def ticket_edit(request, ticket_number):
    if request.user.is_authenticated:
        item = get_object_or_404(Ticket, id=ticket_number)
        form = Edit(request.POST or None, instance=item)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully created")
                return redirect('/home')
        else:
            if request.method == 'GET':
                return render(request, 'editticket.html', {'form': form},{'object': item})
    else:
        return redirect('/index')


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def count_tickets(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            new_dates = Datepicker(request.POST)
            if new_dates.is_valid():
                cleaned_from_date = new_dates.cleaned_data['from_date']
                cleaned_to_date = new_dates.cleaned_data['to_date']
                open_tickets = Ticket.objects.filter(date__gte=cleaned_from_date, date__lte=cleaned_to_date,
                                                     status='OPEN').count()
                ip_tickets = Ticket.objects.filter(date__gte=cleaned_from_date, date__lte=cleaned_to_date,
                                                   status='IN PROGRESS').count()
                ir_tickets = Ticket.objects.filter(date__gte=cleaned_from_date, date__lte=cleaned_to_date,
                                                   status='REVIEW').count()
                closed_tickets = Ticket.objects.filter(date__gte=cleaned_from_date, date__lte=cleaned_to_date,
                                                       status='CLOSED').count()
                tickets = Ticket.objects.all().exclude(status="CLOSED").order_by('-date')
                return render(request, 'countres.html',
                              {'tickets': tickets, 'open_tickets': open_tickets, 'ip_tickets': ip_tickets,
                               'ir_tickets': ir_tickets, 'closed_tickets': closed_tickets,
                                'cleaned_from_date':cleaned_from_date, 'cleaned_to_date':cleaned_to_date})
        else:
            if request.method == 'GET':
                return render(request, 'dateselec.html',)
    else:
        return redirect('/index')
