#проверка вперед, назад
def test_controller_move_forward(controller):
    start_position = controller.position
    controller.handle_choice("1")

    assert controller.position == start_position + 1

def test_controller_move_backward(controller):
    controller.position = 1
    controller.handle_choice("2")

    assert controller.position == 0

#жизни уменьшаются если игрок выбирает неправильное действие
def test_controller_reduce_lives(controller):
    while True:
        controller.position += 1
        room = controller.get_current_room()
        if room.enemy:
            break

    start_life = controller.player.life
    controller.handle_choice("4")

    assert controller.player.life < start_life #жизни уменьшились

#игрок умирает если выбирает неправильное действие несколько раз
def test_controller_game_over(controller):
    while True:
        controller.position += 1
        room = controller.get_current_room()
        if room.enemy:
            break

    while controller.player.life > 0:
        controller.handle_choice("4")

    assert controller.running is False #игрок погиб