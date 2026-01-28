from dungeon.generator import DungeonGenerator
from dungeon.controller import DungeonController

def main():
    generator = DungeonGenerator()
    dungeon = generator.generate()

    controller = DungeonController(
        dungeon,
        generator.rooms,
        generator.player
    )

    controller.show_player_info()

    while controller.running:
        controller.show_location()
        controller.available_actions()
        choice = input("Выберите действие: ")
        controller.handle_choice(choice)

if __name__ == "__main__":
    main()

