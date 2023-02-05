import arcade

from Button import Button
from TextField import TextField


class ButtonsView(arcade.View):

    def __init__(self, window, number, n_features, labels):
        super().__init__(window)
        self.width, self.height = window.get_size()
        self.x = self.width * 0.05
        self.y = self.height * 0.9
        self.font_size = round(self.height * 0.1)
        self.number = number
        self.window = window
        self.active = False
        self.label = "Criteria Positive"
        w, h = window.get_size()
        r = 0.8
        self.buttons = [Button(window, number, i, i * (w / n_features) + w // n_features * (1 - r) / 2, h // 2 - w // n_features * r // 2, w // n_features * r, labels[i]) for i in range(n_features)]
        self.n_features = n_features

    def enable(self):
        self.active = True
        for button in self.buttons:
            button.enable()

    def disable(self):
        self.active = False
        for button in self.buttons:
            button.disable()

    def put_data(self, matrix):
        for button in self.buttons:
            button.put_data(matrix)

    def on_draw(self):
        if self.active:
            w, h = self.window.get_size()
            self._draw_rectangle(0, 0, w, h, (0, 160, 160, 255))
            for button in self.buttons:
                button.on_draw()
            arcade.draw_text(self.label, self.x, self.y - self.font_size // 2, color=arcade.color.BONE,
                             font_size=self.font_size)

    def on_resize(self, width: int, height: int):
        for button in self.buttons:
            button.on_resize(width, height)
        ratio_w, ratio_h = width / self.width, height / self.height
        self.width, self.height = width, height
        self.x *= ratio_w
        self.y *= ratio_h
        self.font_size = round(self.font_size * ratio_w)

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        if self.active:
            for button_ in self.buttons:
                button_.on_mouse_release(x, y, button, modifiers)

    def _draw_rectangle(self, x1, y1, x2, y2, color=arcade.color.SPANISH_VIOLET):
        point_list = (
            (x1, y1),
            (x1, y2),
            (x2, y2),
            (x2, y1)
        )
        arcade.draw_polygon_filled(point_list, color)