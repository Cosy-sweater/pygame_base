import pygame

import comon
import GUI
import sys

app = comon.App()
comon.Node.set_app(app)
app.set_window_mode((0, 0), pygame.FULLSCREEN)
t = comon.Scene(app=app)
app.add_scene(t)
t.add_node(GUI.Button(
    text=GUI.Text(text="123", font_size=24, font_color=(255, 255, 255)),
    pos=app.screen.get_rect().center,
    surface=pygame.Surface((150, 50)),
    anchor="center",
    text_anchor="bottomright",
    command="sys.exit()"
))
app.set_scene(0)

app.run()
