class Bus():
    def __init__(self):
        self.max_passengers=6
        self.current_count= 0

    
    def get_in_the_bus(self):
        if self.current_count < self.max_passengers:
            self.current_count += 1
            print(f'the current people in the bus: {self.current_count}')
        else:
            print(f'the bus has reached the maximum capacity allowed')

    def get_out_the_bus(self):
        if self.current_count > 0:
            self.current_count -= 1
            print(f'the current people in the bus: {self.current_count}')
        else:
            print(f'the bus is empty. No one to get out.')



my_bus=Bus()

while True:
    person=input("type 1 to get in the bus or type 2 to get out the bus (or type 'exit' to quit): ").strip()

    if person == "1":
        my_bus.get_in_the_bus()
    elif person == "2":
        my_bus.get_out_the_bus()
    elif person.lower()== "exit":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please type 1, 2, or 'exit'.")