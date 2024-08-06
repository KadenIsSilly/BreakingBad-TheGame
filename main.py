@namespace
class SpriteKind:
    Methamphetamin = SpriteKind.create()
    Food2 = SpriteKind.create()
    Food3 = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    statusbar.value += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.Food3, on_on_overlap)

def on_on_score():
    global Drugs2, Steven
    tiles.set_current_tilemap(tilemap("""
        level
    """))
    sprites.destroy(Saul)
    tiles.place_on_tile(Walter, tiles.get_tile_location(10, 17))
    Drugs2 = sprites.create(assets.image("""
        myImage2
    """), SpriteKind.Food2)
    tiles.place_on_tile(Drugs2, tiles.get_tile_location(52, 8))
    Steven = sprites.create(assets.image("""
        myImage
    """), SpriteKind.enemy)
    Steven.ay = 300
    Steven.ax = 300
    Steven.set_position(60, 120)
    characterAnimations.loop_frames(Steven,
        assets.animation("""
            StevenWalkingL
        """),
        100,
        characterAnimations.rule(Predicate.MOVING_LEFT))
    characterAnimations.loop_frames(Steven,
        assets.animation("""
            StevenWalkingR0
        """),
        100,
        characterAnimations.rule(Predicate.MOVING_RIGHT))
info.on_score(2, on_on_score)

def on_on_zero(status):
    game.game_over(False)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_on_overlap2(sprite2, otherSprite2):
    music.play(music.create_sound_effect(WaveShape.SINE,
            5000,
            5000,
            255,
            0,
            100,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_score_by(1)
    Drugs.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    music.play(music.create_sound_effect(WaveShape.SINE,
            5000,
            5000,
            255,
            0,
            100,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_score_by(1)
    Drugs2.destroy()
    game.game_over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.Food2, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    statusbar.value += -1
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

Drugs2: Sprite = None
Saul: Sprite = None
Steven: Sprite = None
statusbar: StatusBarSprite = None
Drugs: Sprite = None
Walter: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
"""))
Walter = sprites.create(assets.image("""
    Walter White
"""), SpriteKind.player)
scene.camera_follow_sprite(Walter)
controller.move_sprite(Walter)
Walter.set_velocity(100, 100)
Walter.ay = 600
characterAnimations.loop_frames(Walter,
    assets.animation("""
        WalterIdle
    """),
    300,
    characterAnimations.rule(Predicate.NOT_MOVING))
characterAnimations.loop_frames(Walter,
    assets.animation("""
        WalterWalkingL0
    """),
    100,
    characterAnimations.rule(Predicate.MOVING_RIGHT))
characterAnimations.loop_frames(Walter,
    assets.animation("""
        WalterWalkingL
    """),
    100,
    characterAnimations.rule(Predicate.MOVING_LEFT))
characterAnimations.loop_frames(Walter,
    assets.animation("""
        WalterWalkingR0
    """),
    300,
    characterAnimations.rule(Predicate.MOVING_UP))
Walter.set_position(160, 120)
Drugs = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.food)
tiles.place_on_tile(Drugs, tiles.get_tile_location(86, 17))
Drugs = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.food)
tiles.place_on_tile(Drugs, tiles.get_tile_location(40, 3))
statusbar = statusbars.create(20, 4, StatusBarKind.health)
statusbar.attach_to_sprite(Walter)
Hank = sprites.create(assets.image("""
    Hank Schrader
"""), SpriteKind.enemy)
Hank.ay = 300
Hank.set_position(24, 120)
Hank.set_velocity(50, 50)
tiles.place_on_tile(Hank, tiles.get_tile_location(45, 13))
characterAnimations.loop_frames(Hank,
    assets.animation("""
        HankWalkingR0
    """),
    100,
    characterAnimations.rule(Predicate.MOVING_RIGHT))
characterAnimations.loop_frames(Hank,
    assets.animation("""
        HankWalkingL0
    """),
    100,
    characterAnimations.rule(Predicate.MOVING_LEFT))
Steven = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
Steven.ay = 300
Steven.set_position(60, 120)
Steven.set_velocity(50, 50)
characterAnimations.loop_frames(Steven,
    assets.animation("""
        StevenWalkingR0
    """),
    100,
    characterAnimations.rule(Predicate.MOVING_RIGHT))
characterAnimations.loop_frames(Steven,
    assets.animation("""
        StevenWalkingL
    """),
    100,
    characterAnimations.rule(Predicate.MOVING_LEFT))
Saul = sprites.create(assets.image("""
    myImage1
"""), SpriteKind.Food3)
tiles.place_on_tile(Saul, tiles.get_tile_location(37, 2))
characterAnimations.loop_frames(Saul,
    assets.animation("""
        SaulStanding
    """),
    100,
    characterAnimations.rule(Predicate.NOT_MOVING))