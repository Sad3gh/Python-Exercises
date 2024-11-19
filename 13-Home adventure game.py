class Room:
    def __init__(self, name, description, items, exits):
        """
        Initialize a room with a name, description, items, and exits.

        Parameters:
        name (str): The name of the room.
        description (str): The description of the room.
        items (list): List of items in the room.
        exits (dict): A dictionary of exits (direction: Room).
        """
        self.name = name  # Set the room's name
        self.description = description  # Set the room's description
        self.items = items  # Set the list of items in the room
        self.exits = exits  # Set the exits available from this room

    def describe(self):
        """Print the description of the room and its items."""
        print(f"\nYou are in the {self.name}.")
        print(self.description)
        if self.items:
            print("You see the following items:", ', '.join(self.items))
        else:
            print("There are no items here.")


class Player:
    def __init__(self, starting_room):
        """
        Initialize the player with their current room and inventory.

        Parameters:
        starting_room (Room): The room where the player starts.
        """
        self.current_room = starting_room  # Set the player's starting room
        self.inventory = []  # Initialize the player's inventory

    def move(self, room):
        """Change the player's current room."""
        self.current_room = room  # Update the current room

    def take_item(self, item):
        """Add an item to the player's inventory."""
        if item in self.current_room.items:  # Check if the item is in the current room
            self.current_room.items.remove(item)  # Remove item from the room
            self.inventory.append(item)  # Add item to inventory
            print(f"You have taken the {item}.")
        else:
            print(f"{item} is not in this room.")

    def show_inventory(self):
        """Display the player's inventory."""
        if self.inventory:
            print("You have the following items:", ', '.join(self.inventory))
        else:
            print("Your inventory is empty.")


def main():
    """Main function to run the adventure game."""
    # Create rooms
    living_room = Room("Living Room", "It's cozy and has a sofa and a coffee table.", ["remote", "book"], {})
    kitchen = Room("Kitchen", "It's bright and has a refrigerator and a stove.", ["cookbook"], {})
    bedroom = Room("Bedroom", "It's quiet and has a bed and a wardrobe.", [], {})

    # Define exits
    living_room.exits = {"kitchen": kitchen, "bedroom": bedroom}
    kitchen.exits = {"living room": living_room}
    bedroom.exits = {"living room": living_room}

    # Initialize player in the living room
    player = Player(living_room)

    while True:  # Start the game loop
        player.current_room.describe()  # Describe the current room

        command = input("\n> ").strip().lower()  # Get user input

        # Process commands
        if command.startswith("go to "):
            direction = command[6:]  # Extract the direction
            if direction in player.current_room.exits:
                player.move(player.current_room.exits[direction])  # Move to the new room
            else:
                print("You can't go that way.")

        elif command.startswith("examine "):
            item = command[8:]  # Extract the item to examine
            if item in player.current_room.items:
                print(f"You examine the {item}. It's quite interesting.")
            else:
                print(f"There is no {item} here.")

        elif command.startswith("take "):
            item = command[5:]  # Extract the item to take
            player.take_item(item)  # Attempt to take the item

        elif command == "inventory":
            player.show_inventory()  # Show player's inventory
            continue  # Skip the room description after showing inventory

        elif command == "exit":
            print("Goodbye!")  # Exit the game
            break

        else:
            print("Invalid command. Try 'go to', 'examine', 'take', or 'inventory'.")

if __name__ == "__main__":
    main()