def show_all_bookings(bookings):
    if not bookings:
        print("No bookings found.")
        return
    print("\n========== ALL BOOKINGS ==========")
    for booking in bookings:
        print(
            f'{booking["booking_id"]} | '
            f'{booking["customer_name"]} | '
            f'{booking["room_id"]} | '
            f'{booking["booking_date"]} | '
            f'{booking["start_time"]} | '
            f'{booking["status"]}'
        )
    print("==================================")



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