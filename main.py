def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)
