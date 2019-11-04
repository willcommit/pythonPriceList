import sys
from PySide2.QtWidgets import QApplication
from view import MainWindow, Widget
from helper import read_excel

if __name__ == "__main__":

    app = QApplication([])

    data = read_excel("Export.xlsx")

    widget = Widget(data)
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec_())