from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide2.QtGui import QColor


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)

        self.load_data(data)

    def load_data(self, data):
        self.input_no = data[0].values
        self.input_name = data[1].values

        self.column_count = 2
        self.row_count = len(self.input_no)

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("No", "Name")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            if column == 0:
                return self.input_no[row]
            elif column == 1:
                return self.input_name[row]
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None
