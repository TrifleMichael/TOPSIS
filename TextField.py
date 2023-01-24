import arcade


class TextField:

    def __init__(self, window, i, j ,x, y, a):
        self.window = window
        self.x = x
        self.y = y
        self.a = a
        self.i = i
        self.j = j
        self.width, self.height = self.window.get_size()
        self.clicked = False
        self.active = False
        self.content = ""
        self.key_map = {
            arcade.key.KEY_0: '0',
            arcade.key.KEY_1: '1',
            arcade.key.KEY_2: '2',
            arcade.key.KEY_3: '3',
            arcade.key.KEY_4: '4',
            arcade.key.KEY_5: '5',
            arcade.key.KEY_6: '6',
            arcade.key.KEY_7: '7',
            arcade.key.KEY_8: '8',
            arcade.key.KEY_9: '9',
            arcade.key.BACKSPACE: 'bs'
        }
        self.font_size = round(self.a*0.33)

    def enable(self):
        self.active = True

    def disable(self):
        self.active = False
        self.clicked = False

    def click(self):
        self.clicked = not self.clicked

    def on_draw(self):
        if self.active:
            if self.clicked:
                self._draw_rectangle(self.x, self.y, self.x+self.a, self.y+self.a, arcade.color.WHITE_SMOKE)
            else:
                self._draw_rectangle(self.x, self.y, self.x+self.a, self.y+self.a, arcade.color.BONE)
            arcade.draw_text(self.content, self.x, self.y+self.a//2-self.font_size//2, color=arcade.color.BLUEBERRY, font_size=self.font_size)

    def on_key_press(self, symbol: int, modifiers: int):
        if self.active and self.clicked:
            key = self.key_map.get(symbol)
            if key is not None:
                if key == 'bs':
                    if len(self.content) > 0:
                        self.content = self.content[:-1]
                elif len(self.content) < 4:
                    self.content += key

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
        self.font_size = round(self.a*0.33)

    def put_data(self, matrix):
        if len(self.content) > 0:
            matrix[self.i, self.j] = int(self.content)
        else:
            matrix[self.i, self.j] = 0

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
