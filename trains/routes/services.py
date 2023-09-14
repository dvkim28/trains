from wagon.models import Airplane


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))
def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph

def get_routes(request, form) -> dict:
    context = {'form': form}
    qs = Airplane.objects.all().select_related('to_city', 'from_city')
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travel_time = data['travel_time']
    all_routes = list(dfs_path(graph, from_city.id, to_city.id))
    if not len(all_routes):
        raise ValueError('No routes found')
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_routes:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('There is no such cities in routes')
    else:
        right_ways = all_routes
    all_route = []
    all_airplanes = {}
    for q in qs:
        all_airplanes.setdefault((q.from_city_id, q.to_city_id),[])
        all_airplanes[(q.from_city_id, q.to_city_id)].append(q)
    for route in right_ways:
        tmp = {}
        tmp['airplanes'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_airplanes[(route[i], route[i+1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['airplanes'].append(q)
        tmp['total_time'] = total_time
        if total_time >= travel_time:
            all_route.append(tmp)
    if not all_route:
        raise ValueError('time travel to much')
    sorted_routes = []
    if len(all_route) == 1:
        sorted_routes = all_route
    else:
        times = list(set(r['total_time'] for r in all_route))
        times = sorted(times)
        for time in times:
            for route in all_route:
                if time == route['total_time']:
                    sorted_routes.append(route)
    context['routes'] = sorted_routes
    context['cities'] = {'from_city': from_city, 'to_city': to_city}
    return context
