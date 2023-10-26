from __future__ import annotations

import pygame
from pygame.locals import *


class Scene:
    id = 0

    def __init__(self, app: App, nodes: tuple["Node"] = ()):
        self.app = app
        self._id = Scene.id
        Scene.id += 1

        self.__nodes = []
        self.add_nodes(nodes)

    def get_info(self) -> dict:
        return {"id": self.get_id()}

    def get_id(self) -> int:
        return self._id

    def add_node(self, node: "Node"):
        self.__nodes.append(node)

    def add_nodes(self, nodes: list | tuple["Node"]):
        self.__nodes.extend(nodes)

    def update(self, events, dt):
        self.app.screen.fill((127, 127, 127))
        for node in self.__nodes:
            node.update(events, dt)
        for node in self.__nodes:
            node.draw()


class App:
    def __init__(self):
        self._scenes = []
        self.curent_scene = None

        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((200, 100))

        self._fps = 0

    def run(self):
        fps = 90
        clock = pygame.time.Clock()
        deltaTime = 0.0

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.curent_scene.update(events, deltaTime)

            pygame.display.flip()
            deltaTime = clock.tick(fps)
            self._fps = clock.get_fps()

        pygame.quit()

    def get_fps(self):
        return self._fps

    def add_scene(self, scene: Scene):
        if type(scene) is not Scene:
            raise TypeError("Can not add not Scene object to app scenes")
        self._scenes.append(scene)

    def set_scene(self, scene_id: int):
        for item in self._scenes:
            if item.get_id() == scene_id:
                self.curent_scene = item
                break

    def remove_scene(self, scene_id: int):
        for item in self._scenes:
            if item.get_id() == scene_id:
                self.curent_scene = None
                self._scenes.remove(item)
                break

    def get_scenes(self) -> tuple:
        return tuple(self._scenes)

    def set_window_mode(self, *args):
        self.screen = pygame.display.set_mode(*args)


class Node:
    @classmethod
    def set_app(cls, a: App):
        cls.app = a

    def update(self, dt) -> None:
        pass

    def draw(self) -> None:
        pass

    def draw_other_info(self) -> None:
        pass


class AnimationController(Node):
    def __init__(self):
        self.time_counters = {}

    def update(self, dt) -> None:
        for key in self.time_counters.keys():
            current = self.time_counters[key]
            new_time = current - dt
            if new_time <= 0:
                current["class"].get_by_id(current["id"]).do_sth_idk() # idk have no idea(((
            else:
                current["time"] = new_time
            self.time_counters[key] = current


