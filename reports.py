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