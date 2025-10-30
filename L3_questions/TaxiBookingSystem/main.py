from customer import Customer
from booking_system import BookingSystem
from cancel_booking import CancelBooking

def main():

    total_taxis=int(input("No.of taxi's available for booking : "))
    booking_system = BookingSystem(total_taxis)
    print()
    
    i=1
    while i>0:
        print("choices :\n 1.Book taxi\n 2.Display taxi details\n 3.Cancel taxi\n 4.Exit")
        choice=int(input("Enter your choice : "))
        match choice:
            case 1:
                customer_id = int(input("Customer ID: "))
                pickup = input("Pickup point (A-F): ").upper()
                drop = input("Drop point (A-F): ").upper()
                pick_time = int(input("Pickup time (hour in 24h format): "))

                customer = Customer(customer_id, pickup, drop, pick_time)
                booking_system.book_taxi(customer)

            case 2:
                print("\n--- Final Taxi Details ---")
                booking_system.display_taxi()

            case 3:
                b_id=int(input("Enter the booking id :"))
                CancelBooking.cancelBooking(b_id)

            case 4:
                print("Exiting...")
                break

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()


