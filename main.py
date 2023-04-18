def on_button_pressed_a():
    if sprite.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
    else:
        game.remove_life(1)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # # # .
                        # . . . #
        """)
        music.play_melody("C5 G B A F A C5 B ", 500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("FASE SECRETA")
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: game.LedSprite = None
music.play_melody("C4:4 D4:4 E4:4 C4:4 D4:4 E4:4 C4:2", 120)
basic.show_string("OI")
game.add_life(5)
sprite = game.create_sprite(2, 2)
game.start_countdown(50000)
game.set_score(0)

def on_forever():
    sprite.move(1)
    basic.pause(100)
    sprite.if_on_edge_bounce()
    sprite.turn(Direction.RIGHT, 45)
    sprite.if_on_edge_bounce()
    if game.score() >= 5:
        basic.pause(500)
        basic.show_string("FASE 2")
        basic.show_icon(IconNames.ANGRY)
        basic.pause(500)
        game.set_score(0)
        sprite.move(2)
        sprite.move(1)
        basic.pause(80)
        sprite.if_on_edge_bounce()
        sprite.turn(Direction.RIGHT, 35)
        sprite.if_on_edge_bounce()
        game.set_score(0)
        if game.score() == 3:
            basic.pause(500)
            basic.show_icon(IconNames.HAPPY)
            music.play_melody("G B A G C5 B A B ", 120)
            game.game_over()
basic.forever(on_forever)
