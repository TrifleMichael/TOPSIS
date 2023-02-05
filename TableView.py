import arcade

from TextField import TextField


class TableView(arcade.View):

    def __init__(self, window, number, n_features, labels, items):
        super().__init__(window)
        self.items = items
        self.width, self.height = window.get_size()
        self.x = self.width * 0.05
        self.y = self.height * 0.9
        self.font_size = round(self.height * 0.1)
        self.number = number
        self.window = window
        self.active = False
        w, h = window.get_size()
        r = 0.8
        self.text_fields = [TextField(window, number, i, i*(w/n_features)+w//n_features*(1-r)/2, h//2-w//n_features*r//2, w//n_features*r, labels[i]) for i in range(n_features)]
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
            if self.number == -1:
                arcade.draw_text("Features Weights", self.x, self.y - self.font_size // 2, color=arcade.color.BONE,
                                 font_size=self.font_size)
            elif self.number < len(self.items):
                arcade.draw_text(self.items[self.number], self.x, self.y - self.font_size // 2, color=arcade.color.BONE,
                             font_size=self.font_size)
            else:
                arcade.draw_text('item '+str(self.number), self.x, self.y - self.font_size // 2, color=arcade.color.BONE,
                             font_size=self.font_size)

    def on_key_press(self, symbol: int, modifiers: int):
        if self.active:
            for text_field in self.text_fields:
                text_field.on_key_press(symbol, modifiers)

    def on_resize(self, width: int, height: int):
        for text_field in self.text_fields:
            text_field.on_resize(width, height)
        ratio_w, ratio_h = width / self.width, height / self.height
        self.width, self.height = width, height
        self.x *= ratio_w
        self.y *= ratio_h
        self.font_size = round(self.font_size * ratio_w)

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