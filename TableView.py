import arcade

from TextField import TextField


class TableView(arcade.View):

    def __init__(self, window, number, n_features):
        super().__init__(window)
        self.number = number
        self.window = window
        self.active = False
        w, h = window.get_size()
        r = 0.8
        self.text_fields = [TextField(window, number, i, i*(w/n_features)+w//n_features*(1-r)/2, h//2-w//n_features*r//2, w//n_features*r) for i in range(n_features)]
        self.n_features = n_features

    def enable(self):
        self.active = True
        for text_field in self.text_fields:
            text_field.enable()

    def disable(self):
        self.active = False
        for text_field in self.text_fields:
            text_field.disable()

    def put_data(self, matrix):
        for text_field in self.text_fields:
            text_field.put_data(matrix)

    def on_draw(self):
        if self.active:
            w, h = self.window.get_size()
            self._draw_rectangle(0, 0, w, h, (0, 160, 160, 255))
            for text_field in self.text_fields:
                text_field.on_draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if self.active:
            for text_field in self.text_fields:
                text_field.on_key_press(symbol, modifiers)

    def on_resize(self, width: int, height: int):
        if self.active:
            for text_field in self.text_fields:
                text_field.on_resize(width, height)

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        if self.active:
            for text_field in self.text_fields:
                text_field.on_mouse_release(x, y, button, modifiers)

    def _draw_rectangle(self, x1, y1, x2, y2, color=arcade.color.SPANISH_VIOLET):
        point_list = (
            (x1, y1),
            (x1, y2),
            (x2, y2),
            (x2, y1)
        )
        arcade.draw_polygon_filled(point_list, color)