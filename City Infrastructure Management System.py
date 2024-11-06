# Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, registration_number, type, owner):
        self.reg_num = registration_number
        self.type = type
        self.owner = owner

    def display_information(self):
        return f"Vehicle Registration #: {self.reg_num}, Type: {self.type}, Owner: {self.owner}"
    
    def update_owner(self,new_owner):
        self.owner = new_owner
        return f"Vehicle Registration #: {self.reg_num} is now owned by {new_owner}"
    

vehicle1 = Vehicle("333220", "Truck", "Lucy Lane")
vehicle2 = Vehicle("974920", "Car", "Jack Henry")
vehicle3 = Vehicle("872561", "Van", "Jason Johnson")

print(vehicle1.display_information())
print(vehicle2.display_information())
print(vehicle3.display_information())

print(vehicle1.update_owner("Suzie Summers"))
print(vehicle2.update_owner("Michael Murphy"))
print(vehicle3.update_owner("Jane Doe"))
 
# Task 2: Event Management System Enhancement

class Event:

    def __init__(self, name, date):
        self.name = name 
        self.date = date 
        self.participant_count = 0 

    def add_participant(self, change): 
        if change > 0:
            self.participant_count += change 
            return True
        return False

    def get_participant_count(self):
        return f"The total number of participants attending the {self.name} event is {self.participant_count}" 

event = {}

while True:
    choice = input("Would you like to [1] Add an event, [2] Add Participants, [3] View Participant Count, [4] Exit: ")
    if choice == '4':
        break

    elif choice == '1':
        name = input("Enter the name of the event: ")
        date = input("Enter the date of the event: ")
        event = Event(name, date)
        print(f"{event.name} has been added.")

    elif choice == '2':
        participant_count = int(input("Enter the number of participants attending: "))
        event.add_participant(participant_count)
        print(f"Participants added to the {name} event.")
        

    elif choice == '3':
        print(event.get_participant_count())