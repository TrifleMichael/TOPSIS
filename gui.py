import arcade
import numpy as np

import main
from ResultsView import ResultsView
from TableView import TableView

class Gui(arcade.Window):

    def __init__(self, matrix, n_features):
        super().__init__(1920, 1080, resizable=True)
        self.matrix = matrix
        self.table_num = 0
        self.n_features = n_features
        self.table_views = [TableView(self, self.table_num, n_features)]
        self.table_views[self.table_num].enable()
        self.resultsView = ResultsView(self, [])

    def run(self):
        arcade.run()

    def on_draw(self):
        self.clear()
        self.table_views[self.table_num].on_draw()
        self.resultsView.on_draw()

    def on_update(self, dt: float):
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        self.table_views[self.table_num].on_mouse_release(x, y, button, modifiers)

    def on_resize(self, width: float, height: float):
        self.table_views[self.table_num].on_resize(width, height)
        self.resultsView.on_resize(width, height)

    def on_key_press(self, symbol: int, modifiers: int):
        self.table_views[self.table_num].on_key_press(symbol, modifiers)
        if symbol == arcade.key.ESCAPE:
            self._escape_click()
        elif symbol == arcade.key.RIGHT:
            self.resultsView.disable()
            self.table_views[self.table_num].disable()
            self.table_num += 1
            if self.table_num == len(self.table_views):
                self.table_views.append(TableView(self, self.table_num, self.n_features))
            self.table_views[self.table_num].enable()
        elif symbol == arcade.key.LEFT:
            self.resultsView.disable()
            self.table_views[self.table_num].disable()
            self.table_num = max(self.table_num-1, 0)
            self.table_views[self.table_num].enable()
        elif symbol == arcade.key.ENTER:
            self.matrix = np.zeros((len(self.table_views), self.n_features))
            for table_view in self.table_views:
                table_view.put_data(self.matrix)
            result = main.calculate(self.matrix)
            self.resultsView.rank = result
            self.resultsView.enable()

    def _draw_label(self, x1, y1, x2, y2, text):
        # self._draw_rectangle(x1, y1, x2, y2, (0, 100, 100))
        # font_size = int(self.width * 0.017)
        # arcade.draw_text(text, x1+2, y1+(y2-y1)*0.2, font_size=font_size)
        pass

    def _draw_rectangle(self, x1, y1, x2, y2, color=arcade.color.SPANISH_VIOLET):
        point_list = (
            (x1, y1),
            (x1, y2),
            (x2, y2),
            (x2, y1)
        )
        arcade.draw_polygon_filled(point_list, color)

    def _escape_click(self):
        arcade.exit()
