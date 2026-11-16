from datetime import datetime, timedelta
from rooms import find_room, get_positive_int


def show_all_bookings(bookings):
    if not bookings:
        print("No bookings found.")
        return
    print("\n========== ALL BOOKINGS ==========")
    for booking in bookings:
        show_booking_summary(booking)
    print("===================================")


def find_booking(bookings, booking_id):
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            return booking
    return None


def show_booking_details(bookings, booking_id):
    booking = find_booking(bookings, booking_id)
    if booking is None:
        print("Booking not found.")
        return
    print("\n========== BOOKING DETAILS ==========")
    print(f'Booking ID: {booking["booking_id"]}')
    print(f'Customer: {booking["customer_name"]}')
    print(f'Room_ID: {booking["room_id"]}')
    print(f'Date: {booking["booking_date"]}')
    print(f'Start time: {booking["start_time"]}')
    print(f'Players: {booking["players"]}')
    print(f'Total price: {booking["total_price"]}')
    print(f'Status: {booking["status"]}')
    print(f'Cancellation fee: {booking["cancellation_fee"]}')
    print("=====================================")
    
    
def show_booking_summary(booking):
    print(
        f'{booking["booking_id"]} | '
        f'{booking["customer_name"]} | '
        f'{booking["room_id"]} | '
        f'{booking["booking_date"]} | '
        f'{booking["start_time"]} | '
        f'{booking["status"]}')
    
    
def show_customer_bookings(bookings, customer_name):
    found = False
    print("\n========== CUSTOMER BOOKINGS ===========")
    for booking in bookings:
        if booking["customer_name"].lower() == customer_name.lower():
            show_booking_summary(booking)
            found = True
    if not found:
        print("No bookings found for this customer.")
    print("=======================================")
    

def show_booking_by_date(bookings, booking_date):
    found = False
    
    print("\n========== BOOKINGS BY DATE ==========")
    for booking in bookings:
        if booking["booking_date"] == booking_date:
            show_booking_summary(booking)
            found = True
    if not found:
        print("No bookings found for this date.")
    print("======================================")
    

def validate_booking_time(booking_date, start_time, duration):
    try:
        start_datetime = datetime.strptime(
            f"{booking_date} {start_time}",
            "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format")
        return False
    
    if start_datetime < datetime.now():
        print("Cannot create a booking in the past.")
        return False
    
    opening_time = start_datetime.replace(hour=10, minute=0, second=0)
    #פונקציה בנויה שמייצר לי אובייקט עם ערכים חדשים בלי לשנות את המקורי 
    closing_time = start_datetime.replace(hour=22, minute=0, second=0)
    
    end_datetime = start_datetime + timedelta(minutes=duration)#מייצג לי יצוג הפרשי הזמן בין הזמנים ונותן אפשרות לבצע חישוב על הזמנים

    if start_datetime < opening_time:
        print("The complex opens at 10:00.")
        return False

    if end_datetime > closing_time:
        print("The game must finish by 22:00.")
        return False

    return True



def check_room_availability(rooms, bookings, room_id, booking_date, start_time, duration, exclude_booking_id=None):
    new_start = datetime.strptime(
        f"{booking_date} {start_time}",
        "%Y-%m-%d %H:%M")

    new_end = new_start + timedelta(minutes=duration + 15)

    for booking in bookings:
        if booking["booking_id"] == exclude_booking_id:
            continue

        if booking["room_id"] != room_id:
            continue
        
        if booking["booking_date"] != booking_date:
            continue
        
        if booking["status"] != "Active":
            continue
        
        existing_room = find_room(rooms, room_id)
        if existing_room is None:
            return False
        
        existing_start = datetime.strptime(
            f'{booking["booking_date"]} {booking["start_time"]}',
            "%Y-%m-%d %H:%M")
        
        existing_end = existing_start + timedelta(
                minutes=existing_room["duration"] + 15)

        if new_start < existing_end and new_end > existing_start:
            print("Room is already booked at this time.")
            return False

    return True


def calculate_booking_price(room, players, booking_date):
    base_price = players * room["price_per_player"]
    
    if players >= 7:
        discount = 0.15
        
    elif players >= 5:
        discount = 0.10
        
    else:
        discount = 0
    
    total_price = base_price * (1 - discount)

    booking_day = datetime.strptime(
        booking_date, "%Y-%m-%d"
    ).weekday()

    if booking_day in [4, 5]:
        total_price *= 1.15

    return round(total_price, 2)


def create_booking(rooms, bookings):
    print("\n========== CREATE BOOKING ==========")

    customer_name = input("Customer name: ").strip()

    if not customer_name:
        print("Customer name cannot be empty.")
        return False

    room_id = input("Room ID: ").strip().upper()

    room = find_room(rooms, room_id)

    if room is None:
        print("Room not found.")
        return False

    if not room["is_active"]:
        print("This room is currently inactive.")
        return False

    players = get_positive_int("Number of players: ")

    if players < room["min_players"] or players > room["max_players"]:
        print("Number of players is not allowed for this room.")
        return False

    booking_date = input("Booking date (YYYY-MM-DD): ").strip()
    start_time = input("Start time (HH:MM): ").strip()

    if not validate_booking_time(
        booking_date, start_time, room["duration"]
    ):
        return False

    if not check_room_availability(
        rooms, bookings, room_id, booking_date,
        start_time, room["duration"]
    ):
        return False

    total_price = calculate_booking_price(
        room, players, booking_date
    )

    booking_id = get_next_booking_id(bookings)

    new_booking = {
        "booking_id": booking_id,
        "customer_name": customer_name,
        "room_id": room_id,
        "booking_date": booking_date,
        "start_time": start_time,
        "players": players,
        "total_price": total_price,
        "status": "Active",
        "cancellation_fee": 0.0
    }

    bookings.append(new_booking)

    print("\nBooking created successfully!")
    print(f"Booking ID: {booking_id}")
    print(f"Total price: {total_price}")

    return True
    
    
def get_next_booking_id(bookings):
    max_id = 0

    for booking in bookings:
        number = int(booking["booking_id"][1:])

        if number > max_id:
            max_id = number

    return f"B{max_id + 1:03d}"#B זה אות קבועה שזה המזהה שלנו עבור ההזמנה 
#והמקס זה במביא לי את המספר הבא שלא אכנס להזמנה הקודמת 
#:03d - מציג מספר שלם עם 3 ספרות 


def update_booking(rooms, bookings):
    print("\n========== UPDATE BOOKING ==========")
    booking_id = input("Enter booking ID: ").strip().upper()
    booking = find_booking(bookings, booking_id)
    if booking is None:
        print("booking not found.")
        return False

    if booking["status"] != "Active":
        print("cannot update a cancelled booking")
        return False
    room = find_room(rooms, booking["room_id"])
    
    if room is None:
        print("room not found")
        return False
    if not room["is_active"]:
        print("room is inactive")
        return False

    booking_date = input("New booking date (YYYY-MM-DD): ").strip()
    start_time = input("New start time (HH:MM): ").strip()
    players = get_positive_int("New number of players: ")
    
    if players < room["min_players"] or players > room["max_players"]:
        print("number of players or not allowd for this room")
        return False
    
    if not validate_booking_time(
        booking_date,start_time, room["duration"]
    ):
        return False
   
    if not check_room_availability(
       rooms,
       bookings,
       booking["room_id"],
       booking_date,
       start_time,
       room["duration"],
       booking_id
   ):
       return False
    
    total_price = calculate_booking_price(
        room, players, booking_date)
    
    booking["booking_date"] = booking_date
    booking["start_time"] = start_time
    booking["players"] = players
    booking["total_price"] = total_price
    
    print("\nBooking update successfully!")
    print(f"Booking ID: {booking_id}")
    print(f"New total price: {total_price}")
    
    return True




def cancel_booking(bookings):
    print("============== CANCEL BOOKING =============")
    booking_id = input("Enter booking ID: ").strip().upper()
    booking = find_booking(bookings, booking_id)
    
    if booking is None:
        print("booking not found")
        return False
    
    if booking["status"] == "Cancelled":
        print("this booking is alrady cancelled.")
        return False
    
    booking_datetime = datetime.strptime(
        f'{booking["booking_date"]} {booking["start_time"]}',
        "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()
    time_remaining = booking_datetime - current_datetime
    hours_remaining = time_remaining.total_seconds()/3600
    if hours_remaining <=0:
        print("cannot cancel a booking after it start time.")
        return False
    
    if hours_remaining > 24:
        cancelltion_fee = 0 
    elif hours_remaining >= 6:
        cancelltion_fee = booking["total_price"] * 0.25
    else:
        cancelltion_fee = booking["total_price"] * 0.50
        
    booking["status"] = "Cancelled"
    booking["cancelltion_fee"] = round(cancelltion_fee, 2)
    
    print("\nBooking cancelled successfully!")
    print(f"Booking ID: {booking_id}")
    print(f"Orginal price: {booking['total_price']}")
    print(f"Cancellation fee: {booking['cancelltion_fee']}")
    
    return True