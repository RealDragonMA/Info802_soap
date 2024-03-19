from spyne import rpc, ServiceBase, Iterable, Integer, Array, Unicode, String, Float
import json
from utils import to_hours_minutes_seconds

class RoadService(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, _returns=Iterable(String))
    def road(self, electric_stations, road, vehicle):

        road = json.loads(road)
        vehicle = json.loads(vehicle)
        time = road['time']
        distance = road['distance']
        worst_range = vehicle['range']['chargetrip_range']['worst']

        nb_charge = distance // worst_range
        total_time_charge = nb_charge * vehicle['connectors'][0]['time']
        total_time = time + total_time_charge

        total_hours, total_minutes, total_seconds = to_hours_minutes_seconds(total_time)
        hours, minutes, seconds = to_hours_minutes_seconds(time)

        time_dict = {
            "total_hours": int(total_hours),
            "total_minutes": int(total_minutes),
            "total_seconds": int(total_seconds),
            "hours": int(hours),
            "minutes": int(minutes),
            "seconds": int(seconds),
            "total_time_charging": int(total_time_charge),
            "nb_charge": int(nb_charge),
            "time_per_charge": vehicle['connectors'][0]['time'],
        }

        print("time_dict: ", time_dict)

        yield json.dumps(time_dict)
