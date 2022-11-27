import sys
from PyQt5.QtWidgets import *


class LogWindow(QTextEdit):
    def __init__(self, parent):
        super(LogWindow, self).__init__()
        # self.parent = parent
        # self.setText(parent)
        # self.setText(self.toPlainText() + " 555")
        # self.append("append")
        # self.insertHtml("insert")
        # self.insertHtml("\n")

        self.append("append ")
        self.insertHtml("insert ")
        self.append("append ")
        self.append("append ")
        self.insertHtml("insert ")
        self.insertHtml("insert ")

        # self.resize(1000, 800)
        # self.move(200, 60)
        # self.text_ed = QtWidgets.QTextEdit(self)


class Example(QMainWindow):
    def __init__(self):
        super().__init__(super(Example, self).__init__())

        self.file_tab = QTabWidget(self)
        self.file_tab.move(200, 60)
        self.file_tab.resize(300, 300)
        self.file_tab.setTabPosition(QTabWidget.TabPosition.South)

        # print(count)
        # index = self.tabWidget.count() - 1

        for i in range(3):
            count = self.file_tab.count()
            open_file_tab = LogWindow(str(i))
            self.file_tab.insertTab(count, open_file_tab, f"Tab {count + 1}")
            # self.file_tab.setCurrentIndex(count)

        # self.file_tab.insertTab(count - 1, open_file_tab1, f"Tab {count}")
        # self.file_tab.setCurrentIndex(count)

    # def new_tab(self):
    #     index = self.tabWidget.count() - 1
    #     tabPage = MyTab(self)
    #     self.tabWidget.insertTab(index, tabPage, f"Tab {index}")
    #     self.tabWidget.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.resize(640, 480)
    win.show()
    sys.exit(app.exec_())
