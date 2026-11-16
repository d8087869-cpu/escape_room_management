from rooms import (show_all_rooms,show_room_details,add_room,update_room, change_room_status)
from storage import save_data
from bookings import show_all_bookings, show_booking_details, show_customer_bookings, show_booking_by_date, create_booking

def show_menu():
    print("\n========== ESCAPE ZONE ==========")
    print("1. Manage Rooms")
    print("2. Manage Bookings")
    print("3. Reports")
    print("0. Exit")
    print("=================================")


def run_menu(rooms, bookings):
    choice = ""

    while choice != "0":
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            manage_rooms(rooms)

        elif choice == "2":
            manage_bookings(rooms, bookings)

        elif choice == "3":
            print("Reports - Coming soon")

        elif choice != "0":
            print("Invalid option. Please try again.")

    print("Goodbye!")

            
def manage_rooms(rooms):
    choice = ""

    while choice != "0":
        print("\n========== ROOM MANAGEMENT ==========")
        print("1. Show all rooms")
        print("2. Show room details")
        print("3. Add new room")
        print("4. Update room")
        print("5. Activate / Deactivate room")
        print("0. Back to main menu")
        print("=====================================")

        choice = input("Choose an option: ")

        if choice == "1":
            show_all_rooms(rooms)

        elif choice == "2":
            room_id = input("Enter room ID: ").strip().upper()
            show_room_details(rooms, room_id)

        elif choice == "3":
            if add_room(rooms):
                save_data("rooms.json", rooms)

        elif choice == "4":
            if update_room(rooms):
                save_data("rooms.json", rooms)
                
        elif choice == "5":
            if change_room_status(rooms):
                save_data("rooms.json", rooms)

        elif choice != "0":
            print("Invalid option. Please try again.")




def manage_bookings(rooms, bookings):
    choice = ""

    while choice != "0":
        print("\n========== BOOKING MANAGEMENT ==========")
        print("1. Show all bookings")
        print("2. Search booking by ID")
        print("3. Show customer bookings")
        print("4. Show bookings by date")
        print("5. Create new bookings")
        print("0. Back to main menu")
        print("========================================")

        choice = input("Choose an option: ")

        if choice == "1":
            show_all_bookings(bookings)

        elif choice == "2":
            booking_id = input("Enter booking ID: ").strip().upper()
            show_booking_details(bookings, booking_id)

        elif choice == "3":
            customer_name = input("Enter customer name: ").strip()
            show_customer_bookings(bookings,customer_name)
            
        elif choice == "4":
            booking_date = input("Enter date (YYYY-MM-DD): ").strip()
            show_booking_by_date(bookings, booking_date)
            
        elif choice == "5":
            if create_booking(rooms, bookings):
                save_data("bookings.json", bookings)
             
        elif choice != "0":
            print("Invalid option. Please try again.")