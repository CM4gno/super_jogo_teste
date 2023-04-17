def on_button_pressed_a():
    sprite.move(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    sprite.turn(Direction.RIGHT, 45)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: game.LedSprite = None
music.play_melody("E B C5 A B G A F ", 120)
basic.show_string("Oi, seja Bem Vindo!")
basic.show_string("Esse é somente um jogo teste")
basic.show_string("Espero que goste!")