import csv

from airport import Airport
from flight import Flight

class FlightMap :

    def __init__(self, listAirports = [], listFlights = []):
        
        self.listAirports = listAirports
        self.listFlights = listFlights

    def import_airports(self, csv_file) :
        

        with open('aeroports.csv') as csv_file:

            lecture = csv.reader(csv_file, delimiter=',')

            for i in lecture:
                airport = Airport(i[0], i[1], i[2], i[3])
                self.listAirports.append(airport)


    def import_flights(self, csv_file) :

        with open('flights.csv') as csv_file:

            lecture = csv.reader(csv_file, delimiter=',')

            for i in lecture : 
                flight = Flight(i[0], i[1], i[2])
                self.listFlights.append(flight)

                      
    def airports(self):

        self.import_airports("aeroports.csv")

        return self.listAirports


    def flights(self):

        self.import_flights("flights.csv")

        return self.listFlights


    def airport_find(self, airport_code):

        for i in self.airports():

            if airport_code in i.code:

                return i
           
        return None


    def flight_exist(self, src_airport_code, dst_airport_code):

        for i in self.flights():

            if src_airport_code in i.src_code:

                if dst_airport_code in i.dst_code:

                    return True

            elif dst_airport_code in i.src_code:

                if src_airport_code in i.dst_code:

                    return True
       
        return False

    
    def flights_where(self, airport_code):

        list = []
        
        for i in self.flights():
            if airport_code in i.src_code:
                list.append(i)

        return list


    def airports_from(self, airport_code):
        list = []
        for i in self.flights():
            if airport_code in i.src_code:
                for j in self.airports():
                    if i.dst_code in j.code:
                        if j not in list:
                            list.append(j)
        return list

        


          
                    
               
        
                


            

            
        


       

