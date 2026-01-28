import pytest
from dungeon.generator import DungeonGenerator
from dungeon.controller import DungeonController

@pytest.fixture
def controller():
    gen = DungeonGenerator()
    dungeon = gen.generate()
    return DungeonController(dungeon, gen.rooms, gen.player)
