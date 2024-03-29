# -*- coding: utf-8 -*-
"""Assignment 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cH21RH5Zw-brQz8rFhZn50aKo7-wruS6
"""

from datetime import datetime

class Passenger:
    def __init__(self, first_name, last_name, booking_reference, email, seat_number):
        self._first_name = first_name
        self._last_name = last_name
        self._booking_reference = booking_reference
        self._email = email
        self._seat_number = seat_number

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_booking_reference(self):
        return self._booking_reference

    def set_booking_reference(self, booking_reference):
        self._booking_reference = booking_reference

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_seat_number(self):
        return self._seat_number

    def set_seat_number(self, seat_number):
        self._seat_number = seat_number

    def check_in(self):
        # Logic to check in the passenger
        pass

    def request_seat_change(self, new_seat):
        # Logic to change the seat of the passenger
        pass

class Flight:
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time):
        self._flight_number = flight_number
        self._departure_airport = departure_airport
        self._arrival_airport = arrival_airport
        self._departure_time = departure_time
        self._arrival_time = arrival_time

    def get_flight_number(self):
        return self._flight_number

    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    def get_departure_airport(self):
        return self._departure_airport

    def set_departure_airport(self, departure_airport):
        self._departure_airport = departure_airport

    def get_arrival_airport(self):
        return self._arrival_airport

    def set_arrival_airport(self, arrival_airport):
        self._arrival_airport = arrival_airport

    def get_departure_time(self):
        return self._departure_time

    def set_departure_time(self, departure_time):
        self._departure_time = departure_time

    def get_arrival_time(self):
        return self._arrival_time

    def set_arrival_time(self, arrival_time):
        self._arrival_time = arrival_time

    def get_flight_details(self):
        return f"Flight Number: {self._flight_number}, Departure: {self._departure_airport}, Arrival: {self._arrival_airport}"

    def update_flight_status(self, new_status):
        # Update the status of the flight
        pass

class BoardingPass:
    def __init__(self, passenger, flight, seat_number, gate_number, boarding_time):
        self._passenger = passenger
        self._flight = flight
        self._seat_number = seat_number
        self._gate_number = gate_number
        self._boarding_time = boarding_time
        self._barcode = self.generate_barcode()  # Barcode is generated during instantiation

    def generate_barcode(self):
        # Placeholder logic for barcode generation
        return "1234567890ABCDEF"

    def get_seat_number(self):
        return self._seat_number

    def set_seat_number(self, seat_number):
        self._seat_number = seat_number

    def get_gate_number(self):
        return self._gate_number

    def set_gate_number(self, gate_number):
        self._gate_number = gate_number

    def get_boarding_time(self):
        return self._boarding_time.strftime('%Y-%m-%d %H:%M')

    def set_boarding_time(self, boarding_time):
        self._boarding_time = boarding_time

    def get_passenger(self):
        return self._passenger

    def set_passenger(self, passenger):
        self._passenger = passenger

    def get_flight(self):
        return self._flight

    def set_flight(self, flight):
        self._flight = flight

    def get_barcode(self):
        return self._barcode

    def set_barcode(self, barcode):
        self._barcode = barcode

class AirlineStaff:
    '''Class that Represents an Airline Staff Member'''
    def __init__(self, staff_id, position, department):
        self._staff_id = staff_id
        self._position = position
        self._department = department

    def get_staff_id(self):
        return self._staff_id

    def set_staff_id(self, staff_id):
        self._staff_id = staff_id

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    def log_in_system(self):
        '''Staff logs into the airline's system'''
        pass  # Placeholder for login logic

    def modify_booking(self, passenger, new_details):
        '''Modifies the booking details of a passenger'''
        pass  # Placeholder for booking modification logic

    def reissue_boarding_pass(self, passenger, flight):
        '''Reissues a boarding pass for a passenger for a given flight'''
        # Placeholder for reissuing a boarding pass logic
        # This would typically involve creating a new BoardingPass instance
        return BoardingPass(passenger, flight, passenger.get_seat_number(), "New Gate Number", datetime.now())

    def check_boarding_pass(self, boarding_pass):
        '''Checks the validity of a boarding pass'''
        pass  # Placeholder for boarding pass checking logic

    def __str__(self):
        return f"AirlineStaff [ID: {self._staff_id}, Position: {self._position}, Department: {self._department}]"

# Creating an instance of the AirlineStaff class
passenger = Passenger("Mohammed", "Almulla", "BR123", "Mohammed@keefk.com", "12A")
flight = Flight("FL123", "JFK", "LAX", datetime(2024, 4, 5, 15, 30), datetime(2024, 4, 5, 18, 45))
staff = AirlineStaff("AS12345", "Check-In Agent", "Customer Service")

# Staff logs in to the system
staff.log_in_system()

# Staff modifies a booking for the passenger
# Placeholder for new booking details
new_details = {
    "seat_number": "12C"
}
staff.modify_booking(passenger, new_details)

# Reissue the boarding pass if needed
new_boarding_pass = staff.reissue_boarding_pass(passenger, flight)

# Staff checks the boarding pass
staff.check_boarding_pass(new_boarding_pass)

# Print the details of the new boarding pass
print("New Boarding Pass Details:")
print(f"Passenger Name: {new_boarding_pass._passenger.get_full_name()}")
print(f"Flight: {new_boarding_pass._flight.get_flight_details()}")
print(f"Seat: {new_boarding_pass._seat_number}")
print(f"Gate: {new_boarding_pass._gate_number}")
print(f"Boarding Time: {new_boarding_pass._boarding_time.strftime('%Y-%m-%d %H:%M')}")
print(f"Barcode: {new_boarding_pass._barcode}")