from dungeon.generator import Player


def test_player_creation():
    player = Player("name", "description", 10, "death_descriptions")
    assert player.name == "name"
    assert player.life == 10
    assert not player.is_dead()

#игрок остался жив после 1 атаки
def test_player_take_damage():
    player = Player("name", "description", 10, "death_descriptions")
    player.take_damage()

    assert not player.is_dead()

#после 2 атак противника игрок не выжил
def test_player_death():
    player = Player("name", "description", 10, "death_descriptions")
    player.take_damage()
    player.take_damage()

    assert player.is_dead()