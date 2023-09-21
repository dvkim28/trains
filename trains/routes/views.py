from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RouteForm, RouteModelForm

from .services import get_routes
from cities_main.models import City
from wagon.models import Airplane


def home(request):
    form = RouteForm
    return render(request, 'routes/routes.html', {'form': form})


def find_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/routes.html', {'form': form})
            return render(request, 'routes/routes.html', context)
        return render(request, 'routes/routes.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Invalid')
        return render(request, 'routes/routes.html', {'form': form})


def add_route(request):
    if request.method == 'POST':
        context = {}
        data = request.POST
        if data:
            total_time = data['travel_times']
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            airplanes = data['airplane'].split(',')
            airplanes_list = [int(t) for t in airplanes if t.isdigit()]
            qs = Airplane.objects.filter(id__in=airplanes_list).select_related('from_city', 'to_city')
            cities = City.objects.filter(
                id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    'from_city': cities[from_city_id],
                    'to_city': cities[to_city_id],
                    'travel_times': total_time,
                    'airplanes': qs
                }
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, 'Invalid')
        return redirect('/')
