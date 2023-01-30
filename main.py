# Библиотеки

import sys
# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QLineEdit, QPushButton


class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('To-Do App')
        self.setGeometry(600, 600, 600, 600)

        # Create a list widget to display the to-do items
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(20, 20, 260, 200)

        # Create a line edit to add new to-do items
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(20, 230, 200, 30)

        # Create a button to add the new to-do item
        self.add_button = QPushButton('Add', self)
        self.add_button.setGeometry(230, 230, 60, 30)
        self.add_button.clicked.connect(self.addtodo)

        # Добавлем кнопку для открытия файлов
        self.add_button_to_open = QPushButton('Открыть', self)
        self.add_button_to_open.setToolTip('Так это <b>QWidget</b> для этой кнопки')
        self.add_button_to_open.setGeometry(80,80,80,80)
        self.add_button_to_open.clicked.connect()

    def addtodo(self):
        # Get the text from the line edit
        todo_text = self.line_edit.text()
        # Add the text to the list widget
        self.list_widget.addItem(todo_text)
        # Clear the line edit
        self.line_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo = ToDoApp()
    todo.show()
    sys.exit(app.exec_())
