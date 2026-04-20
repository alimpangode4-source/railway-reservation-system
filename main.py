seats = 50
bookings = {}
booking_id_counter = 1

def check_availability():
    print("Available seats:", seats)

def book_ticket():
    global seats, booking_id_counter
    
    if seats <= 0:
        print("No seats available!")
        return
    
    name = input("Enter name: ")
    age = input("Enter age: ")
    
    booking_id = booking_id_counter
    bookings[booking_id] = {
        "name": name,
        "age": age
    }
    
    booking_id_counter += 1
    seats -= 1
    
    print("Ticket booked successfully!")
    print("Your Booking ID:", booking_id)

def view_ticket():
    bid = int(input("Enter booking ID: "))
    
    if bid in bookings:
        print("Booking Details:")
        print("Name:", bookings[bid]["name"])
        print("Age:", bookings[bid]["age"])
    else:
        print("Booking not found!")

def cancel_ticket():
    global seats
    
    bid = int(input("Enter booking ID to cancel: "))
    
    if bid in bookings:
        del bookings[bid]
        seats += 1
        print("Ticket cancelled successfully!")
    else:
        print("Invalid booking ID!")

def menu():
    while True:
        print("\n--- Railway Reservation System ---")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            check_availability()
        elif choice == 2:
            book_ticket()
        elif choice == 3:
            view_ticket()
        elif choice == 4:
            cancel_ticket()
        elif choice == 5:
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

menu()
