import json
import random
from .config import PLAYERS_FILE, ENEMIES_FILE, ROOMS_FILE

class Player:
    def __init__(self, name: str, description: str, life: int, death_descriptions: str):
        self.name = name
        self.description = description
        self.life = life
        self.death_descriptions = death_descriptions

#считаем что противник 1 ударом ранит игрока, т.е. вычитается 5 из жизней
    def take_damage(self):
        damage = 5
        self.life -= damage
        return self.life

    def is_dead(self) -> bool:
        return self.life <= 0

class Enemy:
    def __init__(self, name: str, description: str, death_description: str):
        self.name = name
        self.description = description
        self.death_description = death_description
        self.alive = True

    def kill(self):
        self.alive = False

class Room:
    def __init__(self, description: str, enemy: Enemy | None):
        self.description = description
        self.enemy = enemy
        self.visited = False

class DungeonGenerator:
    def __init__(self):
        self.__dungeon = []
        self.rooms = []
        self.player = None

    def generate(self):
        # считаем, что первая комната всегда пустая, а последняя всегда с врагом, чтоб было интереснее
        # на 5 комнат - 3 врага
        self.__dungeon = []
        self.__dungeon.append('St')
        self.__dungeon.append(' ')

        middle_rooms = ['E', 'E', ' ']
        random.shuffle(middle_rooms)
        self.__dungeon.extend(middle_rooms)
        self.__dungeon.append('E')
        self.__dungeon.append('Ex')

        # сам игрок
        with open(PLAYERS_FILE, "r", encoding="utf-8") as f:
            player_data = json.load(f)

        #у игрока рандомно выбираем имя, описание и описание кончины
        self.player = Player(
            name=random.choice(player_data["player"]["name"]),
            description=random.choice(player_data["player"]["description"]),
            death_descriptions=random.choice(player_data["player"]["deathDescription"]),
            life = player_data["player"]["life"]
        )

        # перемешиваем чтоб интересно было пройти несколько раз
        with open(ENEMIES_FILE, "r", encoding="utf-8") as f:
            enemies_data = json.load(f)
        enemies = [Enemy(e["name"], e["description"], e["death_description"]) for e in enemies_data]
        random.shuffle(enemies)

        # тоже перемешиваем чтоб интересно было пройти несколько раз
        with open(ROOMS_FILE, "r", encoding="utf-8") as f:
            room_descriptions = json.load(f)
            random.shuffle(room_descriptions)

        #добавляем противников в комнаты
        desc_index = 0
        for tile in self.__dungeon:
            if tile in (' ', 'E'):
                enemy = None
                if tile == 'E' and enemies:
                    enemy = enemies.pop()
                self.rooms.append(Room(room_descriptions[desc_index], enemy))
                desc_index += 1

        return self.__dungeon