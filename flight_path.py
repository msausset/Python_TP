class FlightPathBroken(Exception):
    pass

class FlightPathDuplicate(Exception):
    pass

class FlightPath:
    def __init__(self, src_airport) :
        self.path = [src_airport]

    def add(self, dst_airport, via_flight) -> None:
        if dst_airport != self.path[-1]:
            raise FlightPathBroken("Flight does not pass through last airport in path")
        self.path.append(dst_airport)

    def flights(self):
        flights = []
        for i in range(len(self.path)-1):
            flights.append(self.via_flight)
        return flights

    def airports(self):
        return self.path

    def steps(self) -> float:
        return len(self.path) - 1

    def duration(self) -> float:
        total_duration = 0
        for flight in self.flights():
            total_duration += flight.duration()
        return total_duration