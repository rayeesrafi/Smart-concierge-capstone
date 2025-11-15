# Simple mocked search results

def mock_search(kind: str, leg: dict):
    dest = leg.get('dest')
    start = leg.get('start_date')
    end = leg.get('end_date')
    if kind == 'flights':
        return [
            {'id': f'{dest}-F1', 'price': 15000, 'airline': 'AirMock', 'depart': start, 'arrive': start, 'duration': '4h'},
            {'id': f'{dest}-F2', 'price': 18000, 'airline': 'FlyDemo', 'depart': start, 'arrive': start, 'duration': '4h 30m'},
            {'id': f'{dest}-F3', 'price': 21000, 'airline': 'Skies', 'depart': start, 'arrive': start, 'duration': '3h 50m'}
        ]
    if kind == 'hotels':
        return [
            {'id': f'{dest}-H1', 'name': f'{dest} Budget Inn', 'price_per_night': 4000, 'rating': 3.8},
            {'id': f'{dest}-H2', 'name': f'{dest} Comfort Hotel', 'price_per_night': 7000, 'rating': 4.2},
            {'id': f'{dest}-H3', 'name': f'{dest} Luxury Stay', 'price_per_night': 12000, 'rating': 4.8}
        ]
    if kind == 'activities':
        return [
            {'id': f'{dest}-A1', 'title': f'{dest} City Tour', 'duration': '3h'},
            {'id': f'{dest}-A2', 'title': f'{dest} Food Walk', 'duration': '2h'},
            {'id': f'{dest}-A3', 'title': f'{dest} Museum Visit', 'duration': '1.5h'}
        ]
    return []
