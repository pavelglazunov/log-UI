import sqlite3
import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# from sqlite3 import *
# from config import *

from config.StyleConfig import Style, THEME, edit_style_config, Config


class LogWindow(QTextEdit):
    def __init__(self, text):
        super(LogWindow, self).__init__()
        # self.text = text
        # print(self.text)

        self.resize(1000, 800)
        self.move(200, 60)
        self.setStyleSheet(stl.window)

        for i in text.split("\n"):
            for word in i.lower().split():
                if word in stl.logs_word_colors and stl.logs_word_colors[word][1]:
                    # new_s = "<font color='{}'>{}</font>".format(stl.logs_word_colors[word], word)
                    # self.insertHtml(new_s + "<br>")
                    self.setTextColor(QtGui.QColor(stl.logs_word_colors[word][0]))
                    self.append(i)
                    self.setTextColor(QtGui.QColor(stl.text_color))
                    break
                if word in stl.logs_word_colors and not stl.logs_word_colors[word][1]:
                    before, after = i.lower().split(word.lower())
                    new_s = before + "<font color='{}'>{}</font>".format(stl.logs_word_colors[word][0], word.upper()) + after
                    self.insertHtml("<br>" + new_s)
                    print(new_s)
                    break
            else:
                self.setTextColor(QtGui.QColor(stl.text_color))
                self.append(i)


            # for c in stl.logs_word_colors:
            #     if c.lower() in i.lower().split():
            #         if stl.logs_word_colors[c][1]:
            #             # print("full")
            #

            #         else:
            #             before, after = i.lower().split(c.lower())
            #             new_s = before + "<font color='{}'>{}</font>".format(stl.logs_word_colors[c][0], c) + after
            #             self.insertHtml(new_s)
            #             break
            # else:
            #     self.setTextColor(QtGui.QColor(stl.text_color))
            #     self.append(i)
            # print(i)
            # self.append("\n")
            # self.append(i)

        # print(self.dictionary_of_fraze)
        #         for f in file:
        #             for name in self.dictionary_of_fraze:
        #                 if name in f.split():
        #                     self.output_window.setTextColor(QtGui.QColor(self.dictionary_of_fraze[name]))
        #
        #                     break
        #             else:
        #                 self.output_window.setTextColor(QtGui.QColor("#FFFFFF"))
        #             self.output_window.append(f)
        # self.setText(text)

        # self.opened_files_tab = QTextEdit(self)
        # self.opened_files_tab.resize(1000, 800)
        #
        # self.output_window = QTextEdit('', self)
        # self.output_window.setGeometry(200, 60, 1000, 800)
        # self.output_window.setStyleSheet(stl.window)
        # self.output_window.setTextColor(QtGui.QColor(stl.text_color))
        # self.output_window.setFont(QtGui.QFont(stl.font_style, stl.font_size))


class Example(QMainWindow):
    def __init__(self):
        super().__init__(super(Example, self).__init__())

        self.file_tab = QTabWidget(self)
        self.file_tab.move(200, 60)
        self.file_tab.resize(1000, 800)
        self.file_tab.setTabPosition(QTabWidget.TabPosition.South)

        self.open_files()

        # count = self.file_tab.count()
        # print(count)
        # index = self.tabWidget.count() - 1
        # open_file_tab = LogWindow(self)
        # self.file_tab.insertTab(count - 1, open_file_tab, f"Tab {count}")
        # self.file_tab.setCurrentIndex(count)

        # self.centralwidget = QWidget(self)
        # self.centralwidget.resize(1000, 800)
        # self.centralwidget.move(200, 60)
        # # self.setCentralWidget(self.centralwidget)
        #
        # self.tabWidget = QTabWidget(self)
        # self.tabWidget.resize(1000, 800)
        # self.tabWidget.move(200, 60)
        # count = self.tabWidget.count()
        # self.nb = QtWidgets.QToolButton(text="Добавить", autoRaise=True)
        # self.nb.clicked.connect(self.new_tab)
        # self.tabWidget.insertTab(count, QtWidgets.QWidget(), "")
        # self.tabWidget.tabBar().setTabButton(
        #     count, QtWidgets.QTabBar.RightSide, self.nb)
        #
        # self.new_tab()

        # self.layout = QtWidgets.QGridLayout(self.centralwidget)
        # self.layout.addWidget(self.tabWidget)

        self.setGeometry(0, 0, int(stl.window_width), int(stl.window_height))
        self.setWindowTitle('LOG ')
        self.setStyleSheet(stl.bg)

        # self.output_window = QTextEdit('', self)
        # self.output_window.setGeometry(200, 60, 1000, 800)
        # self.output_window.setStyleSheet(stl.window)
        # self.output_window.setTextColor(QtGui.QColor(stl.text_color))
        # self.output_window.setFont(QtGui.QFont(stl.font_style, stl.font_size))  # , QtGui.QFont.Bold

        self.count_log_window = QTextEdit('Info', self)
        self.count_log_window.move(1250, 200)
        self.count_log_window.resize(200, 400)
        self.count_log_window.setStyleSheet(stl.window)
        self.count_log_window.setTextColor(QtGui.QColor(stl.text_color))

        self.load_button_btn = QPushButton("Open", self)
        self.load_button_btn.move(0, 0)
        self.load_button_btn.resize(50, 50)
        self.load_button_btn.setStyleSheet(stl.menu_btn)
        self.load_button_btn.clicked.connect(self.open_log_file)

        self.setting_btn = QPushButton("Setting", self)
        self.setting_btn.move(50, 0)
        self.setting_btn.resize(70, 50)
        self.setting_btn.setStyleSheet(stl.menu_btn)
        self.setting_btn.clicked.connect(self.open_setting)

        self.border = QLabel(self)
        self.border.resize(1500, 2)
        self.border.move(0, 50)
        self.border.setStyleSheet(stl.line)

        self.add_color_filter_btn = QPushButton("Add color filter", self)
        self.add_color_filter_btn.resize(100, 50)
        self.add_color_filter_btn.move(120, 0)
        self.add_color_filter_btn.setStyleSheet(stl.menu_btn)
        self.add_color_filter_btn.clicked.connect(self.add_color_filter)

        self.help_btn = QPushButton("Help", self)
        self.help_btn.resize(50, 50)
        self.help_btn.move(220, 0)
        self.help_btn.setStyleSheet(stl.menu_btn)
        self.help_btn.clicked.connect(self.help_funck)

        self.search_menu = QLineEdit(self)
        self.search_menu.move(1280, 15)

        self.search_btn = QPushButton("🔍", self)
        self.search_btn.move(1430, 15)
        self.search_btn.resize(20, 20)
        self.search_btn.clicked.connect(self.search)

    # def new_tab(self):
    #     index = self.tabWidget.count() - 1
    #     tabPage = LogWindow(self)
    #     self.tabWidget.insertTab(index, tabPage, f"Tab {index}")
    #     self.tabWidget.setCurrentIndex(index)

    def open_files(self):
        self.file_tab.clear()
        already_opened = cfg.last_opened_files
        for o in already_opened:
            count = self.file_tab.count()
            with open(o) as file:
                open_file_tab = LogWindow(file.read())
            self.file_tab.insertTab(count, open_file_tab, f"{file.name.split('/')[-1]}")
            self.file_tab.setCurrentIndex(count)

    def open_log_file(self):
        open_file = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
        already_opened = cfg.last_opened_files
        already_opened.append(open_file)
        edit_style_config("last_open_file", already_opened)
        self.open_files()

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
        super(ColorFilter, self).__init__()

        self.color = None

        # layout = QGridLayout()

        self.resize(600, 400)
        self.setWindowTitle("Color filter")
        self.setStyleSheet(stl.bg)

        self.color_list = QTextEdit(self)
        self.color_list.move(66, 50)
        self.color_list.resize(200, 200)
        self.color_list.setStyleSheet(stl.window_color)
        self.color_list.setDisabled(True)
        self.already_add_color_filter()

        self.filter_input = QLineEdit(self)
        self.filter_input.resize(150, 30)
        self.filter_input.move(355, 50)
        self.filter_input.setStyleSheet(stl.input_line)
        self.filter_input.setPlaceholderText("Input log filter")
        self.filter_input.setReadOnly(False)

        self.color_btn = QPushButton("Color", self)
        self.color_btn.resize(150, 25)
        self.color_btn.move(355, 100)
        self.color_btn.setStyleSheet(stl.add_menu_btn)
        self.color_btn.clicked.connect(self.add_color)

        self.view_color_lb = QLabel(self)
        self.view_color_lb.move(355, 145)
        self.view_color_lb.resize(150, 40)
        self.view_color_lb.setStyleSheet("border-radius: 5px;")
        self.view_color_lb.setStyleSheet(stl.window_color)
        self.view_color_lb.setAlignment(Qt.AlignCenter)

        self.full_highlight = QCheckBox("Highlight full string", self)
        self.full_highlight.move(355, 195)
        self.full_highlight.setStyleSheet(stl.check_box)

        self.add_color_filter_btn = QPushButton("Add", self)
        self.add_color_filter_btn.move(355, 225)
        self.add_color_filter_btn.resize(150, 25)
        self.add_color_filter_btn.setStyleSheet(stl.add_menu_btn)
        self.add_color_filter_btn.clicked.connect(self.add)

        self.ok_btn = QPushButton("Ok", self)
        self.ok_btn.resize(70, 20)
        self.ok_btn.move(520, 370)
        self.ok_btn.setStyleSheet(stl.add_menu_btn)
        self.ok_btn.clicked.connect(self.close_add_window)

        self.delete_filter_input = QLineEdit(self)
        self.delete_filter_input.resize(200, 30)
        self.delete_filter_input.move(66, 300)
        self.delete_filter_input.setStyleSheet(stl.input_line)
        self.delete_filter_input.setPlaceholderText("Input log filter for delete")
        self.delete_filter_input.setReadOnly(False)

        self.delete_filter_btn = QPushButton("DELETE", self)
        self.delete_filter_btn.move(66, 340)
        self.delete_filter_btn.resize(200, 25)
        self.delete_filter_btn.setStyleSheet(stl.warning_btn)
        self.delete_filter_btn.clicked.connect(self.delete_filter)

        # layout.addWidget(self.color_list)
        # layout.addWidget(self.filter_input)
        # layout.addWidget(self.color_btn)
        # layout.addWidget(self.view_color_lb)
        # layout.addWidget(self.full_highlight)
        # layout.addWidget(self.add_color_filter_btn)
        # layout.addWidget(self.ok_btn)
        # layout.addWidget(self.delete_filter_btn)
        # layout.addWidget(self.delete_filter_input)
        #
        # self.setLayout(layout)

    def clear_form(self):
        self.color = None

        self.delete_filter_input.setText("")
        self.filter_input.setText("")
        self.view_color_lb.setText("")
        self.full_highlight.setChecked(False)

        self.already_add_color_filter()

    def already_add_color_filter(self):
        stl.update()
        self.color_list.clear()
        for k, v in [[i, j] for i, j in stl.logs_word_colors.items() if j]:
            self.color_list.setTextColor(QtGui.QColor(v[0]))
            self.color_list.append(str(k).upper() + str(" - full" * v[1]))

    def add_color(self):
        self.color = QColorDialog.getColor().name()
        self.view_color_lb.setText(self.filter_input.text())
        self.view_color_lb.setStyleSheet("border-radius: 5px;")
        self.view_color_lb.setStyleSheet(f"color: {self.color}; {stl.window_color}")

    def add(self):
        if not (text := " ".join(self.filter_input.text().split())) or not self.color:
            return

        edit_style_config("log_text_colors", [self.color, bool(self.full_highlight.checkState())], key=text.lower())
        ex.open_files()
        self.clear_form()

    def delete_filter(self):
        filter_text = " ".join(self.delete_filter_input.text().split())
        if filter_text in stl.logs_word_colors:
            edit_style_config("log_text_colors", None, key=f"-{filter_text}")
            self.clear_form()

    def close_add_window(self):
        self.close()


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
            f"""UPDATE log_ui_config SET config_value = '{theme}' WHERE config_name = 'theme';""")
        self.repaint()


def import_config():
    theme = cursor.execute(f"""SELECT config_value FROM log_ui_config WHERE config_name='theme'""").fetchone()[0]
    font_size = cursor.execute(f"""SELECT config_value FROM log_ui_config WHERE config_name='font_size'""").fetchone()[
        0]
    screen_size = \
        cursor.execute(f"""SELECT config_value FROM log_ui_config WHERE config_name='screen_size'""").fetchone()[0]

    return {"theme": theme,
            "font_size": font_size,
            "screen_size": screen_size}


def console_log(logs):
    for log in logs:
        print(log)


def add_db():
    cursor.execute("""INSERT INTO log_ui_config (config_name, config_value) VALUES (123, 123)""")


if __name__ == '__main__':
    connect = sqlite3.connect("cash/data_base.db")
    cursor = connect.cursor()
    add_db()
    CONFIG = import_config()

    stl = Style()
    cfg = Config()

    app = QApplication(sys.argv)
    ex = Example()
    # cl = ColorFilter()
    # cl.show()
    ex.show()
    sys.exit(app.exec())

# print(4)
# connect.close()

# def main():
#     app = QApplication(sys.argv)
#     ex = stackedExample()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
