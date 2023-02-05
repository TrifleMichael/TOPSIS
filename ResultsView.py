import arcade

class ResultsView(arcade.View):

    def __init__(self, window, rank, items):
        super().__init__(window)
        self.rank = rank
        self.window = window
        self.width, self.height = window.get_size()
        self._active = False
        self.k = 0
        self.items = items

    def update(self, rank):
        self.rank = rank

    def enable(self):
        self._active = True

    def disable(self):
        self._active = False

    def on_draw(self):
        if self._active:
            self._draw_rectangle(0, 0, self.width, self.height, (0, 160, 160, 255))
            for i, result in enumerate(self.rank[self.k:self.k+15]):
                self._draw_result(self.width * 0.05, self.height * (.9 - i * .05), self.width * 0.95, self.height * (.95 - i * .05), str(i+1+self.k)+". "+self._get_text(result))

    def _get_text(self, num):
        if num < len(self.items):
            return self.items[num]
        else:
            return "item "+str(num)

    def on_resize(self, width: int, height: int):
        self.width = width
        self.height = height

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        self.k = max(min(int(self.k-scroll_y), len(self.rank)), 0)

    def _draw_rectangle(self, x1, y1, x2, y2, color=arcade.color.SPANISH_VIOLET):
        point_list = (
            (x1, y1),
            (x1, y2),
            (x2, y2),
            (x2, y1)
        )
        arcade.draw_polygon_filled(point_list, color)

    def _draw_result(self, x1, y1, x2, y2, text):
        self._draw_rectangle(x1, y1, x2, y2, (0, 100, 100))
        self._draw_rectangle(x1+2, y1+2, x2-2, y2-2, (0, 128, 128))
        font_size = int(self.width * 0.017)
        arcade.draw_text(text, x1+2, y1+(y2-y1)*0.2, font_size=font_size)
