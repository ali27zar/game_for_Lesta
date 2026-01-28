from dungeon.generator import DungeonGenerator

#игрок создался
def test_generator_creates_player():
    gen = DungeonGenerator()
    gen.generate()

    assert gen.player is not None
    assert gen.player.life > 0

#количество комнат - это сумма точек " " и "E" на карте. т.е. не учитываются точки "старт" и "финиш"
def test_rooms_count_matches_dungeon():
    gen = DungeonGenerator()
    dungeon = gen.generate()

    sum_rooms = dungeon.count(" ") + dungeon.count("E")
    assert len(gen.rooms) == sum_rooms

#в пустой комнате нет врага
def test_first_room_has_no_enemy():
    gen = DungeonGenerator()
    gen.generate()

    assert gen.rooms[0].enemy is None

#сопоставление врагов на карте и в комнатах
def test_enemies_count_matches_map():
    gen = DungeonGenerator()
    dungeon = gen.generate()

    enemies_in_rooms = sum(1 for r in gen.rooms if r.enemy)
    enemies_in_map = dungeon.count("E")

    assert enemies_in_rooms == enemies_in_map