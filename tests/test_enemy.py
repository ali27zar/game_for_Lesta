from dungeon.generator import Enemy

def test_enemy_creation():
    enemy = Enemy("name", "description", "death_description")
    assert enemy.alive is True

#статус противника меняется на мертв
def test_enemy_kill():
    enemy = Enemy("name", "description", "death_description")
    enemy.kill()
    assert enemy.alive is False