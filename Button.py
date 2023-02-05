import arcade


class Button:

    def __init__(self, window, i, j, x, y, a, content):
        self.window = window
        self.x = x
        self.y = y
        self.a = a
        self.i = i
        self.j = j
        self.width, self.height = self.window.get_size()
        self.clicked = False
        self.active = False
        self.content = content
        self.font_size = round(self.a*0.15)

    def enable(self):
        self.active = True

    def disable(self):
        self.active = False

    def click(self):
        self.clicked = not self.clicked

    def on_draw(self):
        if self.active:
            b = self.a*0.67
            if self.clicked:
                self._draw_rectangle(self.x, self.y, self.x+self.a, self.y+b, arcade.color.WHITE_SMOKE)
            else:
                self._draw_rectangle(self.x, self.y, self.x+self.a, self.y+b, arcade.color.BONE)
            arcade.draw_text(self.content, self.x, self.y+b//2-self.font_size//2, color=arcade.color.BLUEBERRY, font_size=self.font_size)

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        if self.active and self._mouse_inside(x, y):
            self.click()

    def on_resize(self, w, h):
        ratio_w, ratio_h = w / self.width, h / self.height
        self.width, self.height = w, h
        self.x *= ratio_w
        self.y *= ratio_h
        self.a *= ratio_w
        self.font_size = round(self.a*0.15)

    def put_data(self, array):
        array[self.j] = self.clicked

    def _mouse_inside(self, x, y):
        return self.x <= x <= self.x + self.a and self.y <= y <= self.y + self.a

    def _draw_rectangle(self, x1, y1, x2, y2, color=arcade.color.WHITE_SMOKE):
        point_list = (
            (x1, y1),
            (x1, y2),
            (x2, y2),
            (x2, y1)
        )
        arcade.draw_polygon_filled(point_list, color)