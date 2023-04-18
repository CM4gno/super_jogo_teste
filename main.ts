input.onButtonPressed(Button.A, function () {
    if (sprite.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
    } else {
        game.removeLife(1)
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
        music.playMelody("C5 G B A F A C5 B ", 500)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showString("FASE SECRETA")
})
let sprite: game.LedSprite = null
music.playMelody("C4:4 D4:4 E4:4 C4:4 D4:4 E4:4 C4:2", 120)
basic.showString("OI")
game.addLife(5)
sprite = game.createSprite(2, 2)
game.startCountdown(50000)
game.setScore(0)
basic.forever(function () {
    sprite.move(1)
    basic.pause(100)
    sprite.ifOnEdgeBounce()
    sprite.turn(Direction.Right, 45)
    sprite.ifOnEdgeBounce()
    if (game.score() >= 5) {
        basic.pause(500)
        basic.showString("FASE 2")
        basic.showIcon(IconNames.Angry)
        basic.pause(500)
        game.setScore(0)
        sprite.move(2)
        sprite.move(1)
        basic.pause(80)
        sprite.ifOnEdgeBounce()
        sprite.turn(Direction.Right, 35)
        sprite.ifOnEdgeBounce()
        game.setScore(0)
        if (game.score() == 3) {
            basic.pause(500)
            basic.showIcon(IconNames.Happy)
            music.playMelody("G B A G C5 B A B ", 120)
            game.gameOver()
        }
    }
})
