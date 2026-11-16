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