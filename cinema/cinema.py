from typing import List, Dict, Any

from .models import Cinema


def getCinemaInfo(name: str) -> dict[str, Any]:
    cinema = Cinema.objects.filter(name=name)
    context = {}
    if(cinema.exists()):
        cinema = cinema.first()
        resutls = [{'name': cinema.name, 'number_of_seats': cinema.number_of_seats,
                    'number_of_seats_per_row': cinema.number_of_seats_per_row}]
        context = {
            'cinema':
                {
                    'name': resutls[0]['name'],
                    'number_of_seats': range(resutls[0]['number_of_seats']),
                    'number_of_seats_per_row':range(resutls[0]['number_of_seats_per_row']),
                    'number_of_rows':enumerate(range( resutls[0]['number_of_seats'] // resutls[0]['number_of_seats_per_row'])),
                }
        }

    return context
