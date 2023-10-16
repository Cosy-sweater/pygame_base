import pygame

import comon
import GUI

app = comon.App()
app.set_window_mode((0, 0), pygame.FULLSCREEN)
t = comon.Scene()
app.add_scene(t)
t.add_node(GUI.Text("16", font_color=(255, 255, 255), pos=(500, 500), font_size=30))
app.set_scene(0)

app.run()
