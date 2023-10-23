import pygame

import comon
import GUI

app = comon.App()
app.set_window_mode((0, 0), pygame.FULLSCREEN)
t = comon.Scene(app=app)
app.add_scene(t)
t.add_node(GUI.Button(app=app,
                      text=GUI.Text(app=app, text="123", font_size=24, font_color=(255, 255, 255)),
                      pos=app.screen.get_rect().center,
                      surface=pygame.Surface((50, 50)),
                      anchor="center",
                      text_anchor="bottomright",
                      command="print(1)"
                      ))
app.set_scene(0)

app.run()
