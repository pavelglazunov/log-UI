import sqlite3
import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from sqlite3 import *
from config import *

connect = sqlite3.connect("data_base.db")
cursor = connect.cursor()


class Example(QWidget):
    def __init__(self):
        super().__init__()

        # self.active_config = import_config()
        console_log([CONFIG])

        """SET CONFIG"""
        self.active_size = CONFIG["screen_size"].split(", ")
        self.active_theme = THEME[CONFIG["theme"]]
        self.active_font_size = CONFIG["font_size"]

        self.dictionary_of_fraze = {"INFO": "#FFFF00", "DEBUG": "#04FF00"}
        self.fraze = ["INFO"]

        self.setGeometry(0, 0, int(self.active_size[0]), int(self.active_size[1]))
        self.setWindowTitle('LOG ')
        self.setStyleSheet(f"background-color: {self.active_theme['back_ground']}")

        # self.hot_bar = QLabel(self)
        # self.hot_bar.move(0, 0)
        # self.hot_bar.resize(1500, 50)
        # self.hot_bar.setStyleSheet("background-color: #404050")
        # self.hot_bar.setStyleSheet("border: #000000")

        self.output_window = QTextEdit('', self)
        self.output_window.setGeometry(200, 60, 1000, 800)
        self.output_window.setStyleSheet(f"background-color: {self.active_theme['window_color']}; "
                                         f"border: {self.active_theme['border_color']};"
                                         f"font-size: {self.active_font_size}px")
        # self.output_window.setFontWeight(self.active_font_size)
        self.output_window.setTextColor(QtGui.QColor(f"{self.active_theme['text_color']}"))

        self.count_log_window = QTextEdit('Info', self)
        self.count_log_window.move(1250, 200)
        self.count_log_window.resize(200, 400)
        self.count_log_window.setStyleSheet(f"background-color: {self.active_theme['window_color']}; "
                                            f"border: {self.active_theme['border_color']}")
        self.count_log_window.setTextColor(QtGui.QColor(f"{self.active_theme['text_color']}"))

        self.load_button_btn = QPushButton("Open", self)
        self.load_button_btn.move(0, 0)
        self.load_button_btn.resize(50, 50)
        self.load_button_btn.setStyleSheet(
            "QPushButton {color: "
            f"{self.active_theme['text_color']};"
            " border:  none} QPushButton::hover {background-color : "
            f"{self.active_theme['button_color']};"
            " border:  none}")
        self.load_button_btn.clicked.connect(self.open_log_file)

        self.setting_btn = QPushButton("Setting", self)
        self.setting_btn.move(50, 0)
        self.setting_btn.resize(70, 50)
        self.setting_btn.setStyleSheet(
            "QPushButton {color: "
            f"{self.active_theme['text_color']};"
            " border:  none} QPushButton::hover {background-color : "
            f"{self.active_theme['button_color']};"
            " border:  none}")
        self.setting_btn.clicked.connect(self.open_setting)

        self.border = QLabel(self)
        self.border.resize(1500, 2)
        self.border.move(0, 50)
        self.border.setStyleSheet(f"background-color: {self.active_theme['border_color']};")

        self.add_color_filter_btn = QPushButton("Add color filter", self)
        self.add_color_filter_btn.resize(100, 50)
        self.add_color_filter_btn.move(120, 0)
        self.add_color_filter_btn.setStyleSheet(
            "QPushButton {color: "
            f"{self.active_theme['text_color']};"
            " border:  none} QPushButton::hover {background-color : "
            f"{self.active_theme['button_color']};"
            " border:  none}")
        self.add_color_filter_btn.clicked.connect(self.add_color_filter)

        self.help_btn = QPushButton("Help", self)
        self.help_btn.resize(50, 50)
        self.help_btn.move(220, 0)
        self.help_btn.setStyleSheet(
            "QPushButton {color: "
            f"{self.active_theme['text_color']};"
            " border:  none} QPushButton::hover {background-color : "
            f"{self.active_theme['button_color']};"
            " border:  none}")
        self.help_btn.clicked.connect(self.help_funck)

        self.search_menu = QLineEdit(self)
        self.search_menu.move(1280, 15)

        self.search_btn = QPushButton("🔍", self)
        self.search_btn.move(1430, 15)
        self.search_btn.resize(20, 20)
        self.search_btn.clicked.connect(self.search)

        # self.open_log_file()

    def open_log_file(self, open_code=False):
        if not open_code:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
            cursor.execute(f"""UPDATE config SET val='{fname}' WHERE cfg='already_open';""")
            print("add")
        else:
            fname = cursor.execute(f"""SELECT val FROM config WHERE cfg='already_open'""")

        # open_file = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        # if not was_open:
        #
        #     print(fname)
        #     cursor.execute(f"""UPDATE config SET val = '{fname}' WHERE cfg='already_open';""")
        # else:
        if fname:
            self.output_window.clear()
            with open(fname) as file:
                print(self.dictionary_of_fraze)
                for f in file:
                    for name in self.dictionary_of_fraze:
                        if name in f.split():
                            self.output_window.setTextColor(QtGui.QColor(self.dictionary_of_fraze[name]))

                            break
                    else:
                        self.output_window.setTextColor(QtGui.QColor("#FFFFFF"))
                    self.output_window.append(f)
            # self.set_info()
        else:
            print(1)

    def set_info(self):
        pass

    def add_color_filter(self):
        self.c_filter = ColorFilter()
        self.c_filter.show()

    def search(self):
        print(self.search_menu.text())
        self.search_menu.setText("")

    def open_setting(self):
        print(5564)
        self.stg = SettingMenu()
        self.stg.show()

    def help_funck(self):
        pass


class ColorFilter(QWidget):
    def __init__(self):
        super().__init__()

        self.active_size = CONFIG["screen_size"].split(", ")
        self.active_theme = THEME[CONFIG["theme"]]
        self.active_font_size = CONFIG["font_size"]

        self.color = None

        self.resize(600, 400)
        self.setWindowTitle("Color filter")
        self.setStyleSheet(f"background-color: {self.active_theme['back_ground']}")

        self.border0 = QLabel(self)
        self.border0.move(65, 49)
        self.border0.resize(202, 202)
        self.border0.setStyleSheet(f"background-color: {self.active_theme['border_color']};")
        self.border0.setStyleSheet(f"border: 1px solid {self.active_theme['border_color']};")

        self.border1 = QLabel(self)
        self.border1.move(330, 50)
        self.border1.resize(200, 200)
        self.border1.setStyleSheet(f"background: {self.active_theme['back_ground']};")
        self.border1.setStyleSheet(f"border: 1px solid {self.active_theme['border_color']};")

        # self.border2 = QLabel(self)
        # self.border2.move(320, 50)
        # self.border2.resize(2, 200)
        # self.border2.setStyleSheet(f"background-color: {self.active_theme['border_color']};")
        #
        # self.border3 = QLabel(self)
        # self.border3.move(320, 250)
        # self.border3.resize(200, 2)
        # self.border3.setStyleSheet(f"background-color: {self.active_theme['border_color']};")
        #
        # self.border4 = QLabel(self)
        # self.border4.move(520, 50)
        # self.border4.resize(2, 200)
        # self.border4.setStyleSheet(f"background-color: {self.active_theme['border_color']};")

        self.color_list = QTextEdit(self)
        self.color_list.move(66, 50)
        self.color_list.resize(200, 200)
        self.color_list.setStyleSheet(f"background-color: {self.active_theme['window_color']}; "
                                      f"border: {self.active_theme['border_color']};"
                                      f"font-size: {self.active_font_size}px")
        self.already_add_color_filter()

        self.add_color_filter_btn = QPushButton("Add", self)
        self.add_color_filter_btn.move(355, 200)
        self.add_color_filter_btn.resize(150, 20)
        self.add_color_filter_btn.setStyleSheet(
            "QPushButton {color: "
            f"{self.active_theme['text_color']};"
            " border:  none} QPushButton::hover {background-color : "
            f"{self.active_theme['button_color']};"
            " border:  none}")
        self.add_color_filter_btn.clicked.connect(self.add)

        self.color_btn = QPushButton("Color", self)
        self.color_btn.resize(150, 20)
        self.color_btn.move(355, 120)
        self.color_btn.setStyleSheet(
            "QPushButton {color: "
            f"{self.active_theme['text_color']};"
            " border:  none} QPushButton::hover {background-color : "
            f"{self.active_theme['button_color']};"
            " border:  none}")
        self.color_btn.clicked.connect(self.add_color)

        self.filter_input = QLineEdit(self)
        self.filter_input.resize(150, 20)
        self.filter_input.move(355, 80)
        self.filter_input.setStyleSheet(f"background-color: {self.active_theme['window_color']}; "
                                        f"border: {self.active_theme['border_color']};"
                                        f"font-size: {self.active_font_size}px;"
                                        f"color: {self.active_theme['text_color']}")
        self.filter_input.setReadOnly(False)

    def already_add_color_filter(self):
        self.color_list.clear()
        for filter_name in ex.dictionary_of_fraze:
            self.color_list.setTextColor(QtGui.QColor(ex.dictionary_of_fraze[filter_name]))
            self.color_list.append(filter_name)

    def add_color(self):
        self.color = QColorDialog.getColor().name()

    def add(self):
        if self.filter_input.text() != "":
            print(self.filter_input.text())
            ex.dictionary_of_fraze[self.filter_input.text()] = self.color
            print(ex.dictionary_of_fraze)
            self.already_add_color_filter()
            # if ex.output_window.text() != "":
            ex.open_log_file(True)
            self.filter_input.setText("")


class SettingMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.active_size = CONFIG["screen_size"].split(", ")
        self.active_theme = THEME[CONFIG["theme"]]
        self.active_font_size = CONFIG["font_size"]

        self.resize(600, 400)
        self.setWindowTitle("Setting")
        self.setStyleSheet(f"background-color: {self.active_theme['back_ground']}")

        self.theme_setting = QLabel(self)
        self.theme_setting.move(10, 10)
        self.theme_setting.resize(100, 50)
        self.theme_setting.setText("Theme")
        self.theme_setting.setStyleSheet(
            f"color: {self.active_theme['text_color']}; font-size: {self.active_font_size}px")

        self.theme_choose = QComboBox(self)
        self.theme_choose.move(150, 30)
        self.theme_choose.resize(150, 20)
        self.theme_choose.setStyleSheet(f"color: {self.active_theme['text_color']}")
        self.add_theme_choose()

        self.theme_choose.activated[str].connect(self.update_theme)

    def add_theme_choose(self):
        theme_list = ["dark", "white", "green", "blue"]
        self.theme_choose.addItem(CONFIG["theme"])
        for theme in theme_list:
            if theme != CONFIG["theme"]:
                self.theme_choose.addItem(theme)

        # self.theme_choose.addItem("dark")
        # self.theme_choose.addItem("white")
        # self.theme_choose.addItem("green")
        # self.theme_choose.addItem("blue")

    def update_theme(self, theme):
        print(theme)
        cursor.execute(
            f"""UPDATE config SET val = '{theme}' WHERE cfg = 'theme';""")
        self.repaint()


def import_config():
    theme = cursor.execute(f"""SELECT val FROM config WHERE cfg='theme'""").fetchone()[0]
    font_size = cursor.execute(f"""SELECT val FROM config WHERE cfg='font_size'""").fetchone()[0]
    screen_size = cursor.execute(f"""SELECT val FROM config WHERE cfg='screen_size'""").fetchone()[0]

    return {"theme": theme,
            "font_size": font_size,
            "screen_size": screen_size}


def console_log(logs):
    for log in logs:
        print(log)


if __name__ == '__main__':
    CONFIG = import_config()
    app = QApplication(sys.argv)
    ex = Example()
    cl = ColorFilter()
    cl.show()
    sys.exit(app.exec())

# def main():
#     app = QApplication(sys.argv)
#     ex = stackedExample()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
