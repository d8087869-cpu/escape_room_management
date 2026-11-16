def show_all_rooms(rooms):
    if not rooms:
        print("No rooms found.")
        return
    print("\n========== ALL ROOMS ==========")
    for room in rooms:
        status = "Active" if room["is_active"] else "Inactive"
        print(
            f'{room["room_id"]} | '
            f'{room["name"]} | '
            f'{room["difficulty"]} | '
            f'{status}')
    print("===============================")



def find_room(rooms, room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            return room
    return None


def show_room_details(rooms, room_id):
    room = find_room(rooms, room_id)
    if room is None:
        print("Room not found.")
        return

    status = "Active" if room["is_active"] else "Inactive"

    print("\n========== ROOM DETAILS ==========")
    print(f'Room ID: {room["room_id"]}')
    print(f'Name: {room["name"]}')
    print(f'Difficulty: {room["difficulty"]}')
    print(f'Duration: {room["duration"]} minutes')
    print(f'Minimum players: {room["min_players"]}')
    print(f'Maximum players: {room["max_players"]}')
    print(f'Price per player: {room["price_per_player"]}')
    print(f'Status: {status}')
    print("==================================")


#פונקציה לשימוש חוזר כל פעם שאני אצטרך אינפוט של מספר שלם אני אקח אותו ,והבא זה ל FLOAT
def get_positive_int(message):
    value = ""
    while not value.isdigit() or int(value) <= 0:
        value = input(message)
        if not value.isdigit() or int(value)<=0:
            print("Please enter a positvie integer.")
    return int(value)
        


def get_positive_float(message):
    valid = False
    while not valid:
        try:
            value = float(input(message))
            if value > 0:
                valid = True
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a positive number.")
    return value


def get_difficulty():
    difficulty = ""
    while difficulty not in ["Easy", "Medium", "Hard"]:
        difficulty = input("Difficulty (Easy/Medium/Hard): ").capitalize()
        if difficulty not in ["Easy", "Medium", "Hard"]:
            print("Invalid difficulty.")
    return difficulty


def add_room(rooms):
    print("\n========== ADD NEW ROOM ==========")
    room_id = input("Room ID: ").strip().upper()
    if find_room(rooms, room_id) is not None:
        print("Room ID already exists.")
        return False
    name = input("Room name: ").strip()
    if not name:
        print("Room name cannot be empty")
        return False
    difficulty = get_difficulty()
    
    duration = get_positive_int("Duration in minutes: ")
    min_players = get_positive_int("Minimum players: ")
    max_players = get_positive_int("Maximum players: ")
    
    while max_players < min_players:
        print("Maximum players cannot be smaller them minimum players.")
        max_players = get_positive_int("Maximum players: ")
    
    price = get_positive_float("Price per player: ")
    
    new_room = {
        "room_id": room_id,
        "name": name,
        "difficulty": difficulty,
        "duration": duration,
        "min_players": min_players,
        "max_players": max_players,
        "price_per_player": price,
        "is_active": True
    }
    rooms.append(new_room)
    print("Room added successfully.")
    return True
    
    
    
def update_room(rooms):
    room_id = input("Enter room ID to update: ").strip().upper()
    room = find_room(rooms, room_id)
    if room is None:
        print("Room not found.")
        return False
    print("\n========== UPDATE ROOM ==========")
    name = input("New room name: ").strip()
    if not name:
        print("Room name cannot be empty.")
        return False
    difficulty = get_difficulty()
    
    duration = get_positive_int("New duration: ")
    min_players = get_positive_int("New minimum players: ")
    max_players = get_positive_int("New maximum players: ")
    
    while max_players < min_players:
        print("maximum players cannot be smaller then minimum players.")
        max_players = get_positive_int("New maximu players: ")
        
    price = get_positive_float("New price per player: ")
    
    room["name"] = name
    room["difficulty"] = difficulty
    room["duration"] = duration
    room["min_players"] = min_players
    room["max_players"] = max_players
    room["price_per_player"] = price
    
    print("Room update successfully.")
    return True


def change_room_status(rooms):
    room_id = input("Enter room ID: ").strip().upper()
    room = find_room(rooms, room_id)

    if room is None:
        print("Room not found.")
        return False

    if room["is_active"]:
        room["is_active"] = False
        print(f'{room["name"]} has been deactivated.')

    else:
        room["is_active"] = True
        print(f'{room["name"]} has been activated.')

    return True