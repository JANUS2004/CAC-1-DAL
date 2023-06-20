class TrainBookingApplication:
    
    def __init__(self):
        self.train_details = {}

    def add_train(self, tr_no, tr_name, dest, arr_time, depart_time, total_seats, avail_seats):
        train_details = {
            'Train Number': tr_no,
            'Train Name': tr_name,
            'Destination': dest,
            'Arrival Time': arr_time,
            'Departure Time': depart_time,
            'Total Seats': total_seats,
            'Available Seats': avail_seats
        }
        self.train_details[tr_no] = train_details

    def display_train_details(self):
        if not self.train_details:
            print("No train details available.")
        else:
            for tr_no, train_info in self.train_details.items():
                print(f"Train Number: {tr_no}")
                for key, value in train_info.items():
                    print(f"{key}: {value}")
                print()

    def book_ticket(self, tr_no, num_tickets):
        train = self.train_details.get(tr_no)
        if train:
            avail_seats = train['Available Seats']
            if avail_seats >= num_tickets:
                train['Available Seats'] -= num_tickets
                print(f"Ticket(s) booked successfully for Train {tr_no}.")
            else:
                print(f"Insufficient seats available on Train {tr_no}.")
        else:
            print(f"Train {tr_no} not found.")

app = TrainBookingApplication()

# Add trains using the add_train function
app.add_train("12309", "Rajdhani Express", "New Delhi", "08:00 AM", "08:30 AM", 200, 150)
app.add_train("12002", "Shatabdi Express", "Mumbai", "10:00 AM", "10:30 AM", 150, 100)
app.add_train("12269", "Duronto Express", "Kolkata", "06:00 PM", "06:30 PM", 180, 120)

while True:
    app.display_train_details()
    print("Train Booking Application")
    print("1. Book a ticket")
    print("2. Exit")
    
    choice = input("Enter your choice (1-2): ")
        
    if choice == '1':
        tr_no = input("Enter train number: ")
        num_tickets = int(input("Enter number of tickets: "))
        app.book_ticket(tr_no, num_tickets)
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Train Booking App!")