from datetime import datetime, timedelta
from rooms import find_room

def show_active_bookings_count(bookings):
    active_bookings = 0
    for booking in bookings:
        if booking["status"] == "Active":
            active_bookings += 1 
    print(f"Active bookings: {active_bookings}")
    
    

def show_cancelled_bookings_count(bookings):
    cancelled_bookings = 0
    for booking in bookings:
        if booking["status"] == "Cancelled":
            cancelled_bookings += 1
    print(f"Cancelled bookings: {cancelled_bookings}")


def show_total_revenue(bookings):
    total_revenue = 0
    for booking in bookings:
        if booking["status"] == "Active":
            total_revenue += booking["total_price"]
    print(f"Total revneue: {total_revenue:.2f}")
    
    
def show_total_cancellation_fees(bookings):
    total_fees = 0
    for booking in bookings:
        if booking["status"] == "Cancelled":
            total_fees += booking["cancellation_fee"]
    print(f"Total cancellation fees: {total_fees:.2f}")
    
    
def show_most_popular_room(rooms, bookings):
    room_bookings = {}

    for room in rooms:
        room_bookings[room["room_id"]] = 0

    for booking in bookings:
        if booking["status"] == "Active":
            room_id = booking["room_id"]
            room_bookings[room_id] += 1

    if not room_bookings or max(room_bookings.values()) == 0:
        print("No active bookings found.")
        return

    popular_room_id = max(room_bookings, key=lambda room_id: room_bookings[room_id])
#למדה לוקח את האובייקט של מקס ומחפש במילון את מספר ההמזנות של אותו החדר ומחזיר מספר הזמנות 
    room = None

    for current_room in rooms:
        if current_room["room_id"] == popular_room_id:
            room = current_room
            break
        
    if room is None:
        print("Room not found.")
        return

    print("\n========== MOST POPULAR ROOM ==========")
    print(f'Room: {room["name"]}')
    print(f'Room ID: {popular_room_id}')
    print(f'Active bookings: {room_bookings[popular_room_id]}')
    print("=======================================")
    
    
def show_bookings_per_room(rooms, bookings):
    room_bookings = {}

    for room in rooms:
        room_bookings[room["room_id"]] = 0

    for booking in bookings:
        room_id = booking["room_id"]

        if room_id in room_bookings:
            room_bookings[room_id] += 1

    print("\n========== BOOKINGS PER ROOM ==========")

    for room in rooms:
        room_id = room["room_id"]

        print(
            f'{room["name"]} | '
            f'{room_id} | '
            f'Bookings: {room_bookings[room_id]}'
        )

    print("=======================================")
    

def show_room_occupancy(rooms, bookings):
    room_id = input("Enter room ID: ").strip().upper()

    room = find_room(rooms, room_id)

    if room is None:
        print("Room not found.")
        return

    booking_date = input("Enter date (YYYY-MM-DD): ")

    try:
        date = datetime.strptime(booking_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    occupied_minutes = 0

    for booking in bookings:
        if (booking["room_id"] == room_id
                and booking["booking_date"] == booking_date
                and booking["status"] == "Active"):

            start_time = datetime.strptime(
                f"{booking_date} {booking['start_time']}",
                "%Y-%m-%d %H:%M")

            end_time = start_time + timedelta(
                minutes=room["duration"] + 15)

            closing_time = start_time.replace(
                hour=22, minute=0)

            if end_time > closing_time:
                end_time = closing_time

            occupied_minutes += (
                end_time - start_time
            ).total_seconds() / 60

    occupancy = (occupied_minutes / 720) * 100

    print("\n========== ROOM OCCUPANCY ==========")
    print(f'Room: {room["name"]}')
    print(f"Room ID: {room_id}")
    print(f"Date: {booking_date}")
    print(f"Occupied minutes: {occupied_minutes}")
    print(f"Occupancy: {occupancy:.2f}%")
    print("====================================")