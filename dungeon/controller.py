class DungeonController:
    def __init__(self, dungeon: list[str], rooms: list, player):
        self.__dungeon = dungeon
        self.rooms = rooms
        self.player = player
        self.position = 0
        self.running = True

    def show_player_info(self):
        print(f"Вы: {self.player.name}")
        print(self.player.description)
        print(f"Жизни: {self.player.life}")

    #возращаем комнату
    def get_current_room(self):
        room_index = 0
        for i, tile in enumerate(self.__dungeon):
            if tile in (' ', 'E'):
                if i == self.position:
                    break
                room_index += 1
        return self.rooms[room_index]

    #в зависимости от условия выводим описание
    def show_location(self):
        tile = self.__dungeon[self.position]

        print("=========================================")

        if tile == "Ex":
            print(f"Вы у выхода из подземелья!")
            return

        if tile == "St":
            print(f"Вы у входа в подземелье!")
            return

        room = self.get_current_room()
        print(room.description)

        # описание врага, если он есть
        if room.enemy and room.enemy.alive:
            print(f"Вы видите противника: {room.enemy.name}")
            print(room.enemy.description)

    # действия, если в комнате есть или нет врага
    def available_actions(self):
        tile = self.__dungeon[self.position]
        room = self.get_current_room() if tile in (' ', 'E') else None

        if room and room.enemy and room.enemy.alive:
            print("Вы можете:")
            print("    3: Атаковать!")
            print("    4: Паниковать!")
            print("    5: Заорать!")
            print("    6: Подождать!")
        else:
            print("Вы можете:")
            if self.position < len(self.__dungeon) - 1:
                print("    1: Пойти дальше!")
            if self.position > 0:
                print("    2: Вернуться назад!")
            if tile == "Ex":
                print("    0: Выйти из подземелья!")

    # обрабатываем действия
    def handle_choice(self, choice: str):
        tile = self.__dungeon[self.position]
        room = self.get_current_room() if tile in (' ', 'E') else None

        if room and room.enemy and room.enemy.alive:
            if choice == "3":
                room.enemy.alive = False
                print(f"{room.enemy.name} уничтожен! {room.enemy.death_description}")
                return

            elif choice in ("4", "5", "6"):
                actions_dict = {"4": "паниковать", "5": "заорать", "6": "подождать"}
                action_name = actions_dict.get(choice, choice)
                print("=========================================")
                print(f"Зачем вы выбрали «{action_name}»? Надо было атаковать! Вы ранены...")
                self.player.life = max(self.player.life - 5, 0)
                if self.player.life > 0:
                    print(f"Жизни: {self.player.life}")
                else:
                    print("=========================================")
                    print(self.player.death_descriptions)
                    print("Игра окончена.")
                    self.running = False
                return
            else:
                print("Неверная команда.")
                return


        if choice == "1" and self.position < len(self.__dungeon) - 1:
            self.position += 1
        elif choice == "2" and self.position > 0:
            self.position -= 1
        elif choice == "0" and tile == 'Ex':
            print("Вы вышли из подземелья.")
            self.running = False
        else:
            print("Неверная команда.")