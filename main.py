from client import run_menu
from storage import load_data


def main():
    rooms = load_data("rooms.json")
    bookings = load_data("bookings.json")

    run_menu(rooms, bookings)


if __name__ == "__main__":
    main()