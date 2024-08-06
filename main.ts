namespace SpriteKind {
    export const Methamphetamin = SpriteKind.create()
    export const Food2 = SpriteKind.create()
    export const Food3 = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite4, otherSprite4) {
    statusbar.value += -1
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food2, function (sprite3, otherSprite3) {
    music.play(music.createSoundEffect(WaveShape.Sine, 5000, 5000, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
    info.changeScoreBy(1)
    Drugs2.destroy()
    game.gameOver(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food3, function (sprite, otherSprite) {
    statusbar.value += 1
})
info.onScore(2, function () {
    tiles.setCurrentTilemap(tilemap`level`)
    sprites.destroy(Saul)
    tiles.placeOnTile(Walter, tiles.getTileLocation(10, 17))
    Drugs2 = sprites.create(assets.image`myImage2`, SpriteKind.Food2)
    tiles.placeOnTile(Drugs2, tiles.getTileLocation(52, 8))
    Steven = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
    Steven.ay = 300
    Steven.ax = 300
    Steven.setPosition(60, 120)
    characterAnimations.loopFrames(
    Steven,
    assets.animation`StevenWalkingL`,
    100,
    characterAnimations.rule(Predicate.MovingLeft)
    )
    characterAnimations.loopFrames(
    Steven,
    assets.animation`StevenWalkingR0`,
    100,
    characterAnimations.rule(Predicate.MovingRight)
    )
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite2, otherSprite2) {
    music.play(music.createSoundEffect(WaveShape.Sine, 5000, 5000, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
    info.changeScoreBy(1)
    Drugs.destroy()
})
let Drugs2: Sprite = null
let Saul: Sprite = null
let Steven: Sprite = null
let statusbar: StatusBarSprite = null
let Drugs: Sprite = null
let Walter: Sprite = null
tiles.setCurrentTilemap(tilemap`level1`)
Walter = sprites.create(assets.image`Walter White`, SpriteKind.Player)
scene.cameraFollowSprite(Walter)
controller.moveSprite(Walter)
Walter.setVelocity(100, 100)
Walter.ay = 600
characterAnimations.loopFrames(
Walter,
assets.animation`WalterIdle`,
300,
characterAnimations.rule(Predicate.NotMoving)
)
characterAnimations.loopFrames(
Walter,
assets.animation`WalterWalkingL0`,
100,
characterAnimations.rule(Predicate.MovingRight)
)
characterAnimations.loopFrames(
Walter,
assets.animation`WalterWalkingL`,
100,
characterAnimations.rule(Predicate.MovingLeft)
)
characterAnimations.loopFrames(
Walter,
assets.animation`WalterWalkingR0`,
300,
characterAnimations.rule(Predicate.MovingUp)
)
Walter.setPosition(160, 120)
Drugs = sprites.create(assets.image`myImage0`, SpriteKind.Food)
tiles.placeOnTile(Drugs, tiles.getTileLocation(86, 17))
Drugs = sprites.create(assets.image`myImage0`, SpriteKind.Food)
tiles.placeOnTile(Drugs, tiles.getTileLocation(40, 3))
statusbar = statusbars.create(20, 4, StatusBarKind.Health)
statusbar.attachToSprite(Walter)
let Hank = sprites.create(assets.image`Hank Schrader`, SpriteKind.Enemy)
Hank.ay = 300
Hank.setPosition(24, 120)
Hank.setVelocity(50, 50)
tiles.placeOnTile(Hank, tiles.getTileLocation(45, 13))
characterAnimations.loopFrames(
Hank,
assets.animation`HankWalkingR0`,
100,
characterAnimations.rule(Predicate.MovingRight)
)
characterAnimations.loopFrames(
Hank,
assets.animation`HankWalkingL0`,
100,
characterAnimations.rule(Predicate.MovingLeft)
)
Steven = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
Steven.ay = 300
Steven.setPosition(60, 120)
Steven.setVelocity(50, 50)
characterAnimations.loopFrames(
Steven,
assets.animation`StevenWalkingR0`,
100,
characterAnimations.rule(Predicate.MovingRight)
)
characterAnimations.loopFrames(
Steven,
assets.animation`StevenWalkingL`,
100,
characterAnimations.rule(Predicate.MovingLeft)
)
Saul = sprites.create(assets.image`myImage1`, SpriteKind.Food3)
tiles.placeOnTile(Saul, tiles.getTileLocation(37, 2))
characterAnimations.loopFrames(
Saul,
assets.animation`SaulStanding`,
100,
characterAnimations.rule(Predicate.NotMoving)
)
