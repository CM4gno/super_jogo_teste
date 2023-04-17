input.onButtonPressed(Button.A, function on_button_pressed_a() {
    sprite.move(1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    sprite.turn(Direction.Right, 45)
})
let sprite : game.LedSprite = null
music.playMelody("E B C5 A B G A F ", 120)
basic.showString("Oi, seja Bem Vindo!")
basic.showString("Esse é somente um jogo teste")
basic.showString("Espero que goste!")
