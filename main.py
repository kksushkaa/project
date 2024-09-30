import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from login_window import LoginWindow
# from task_window import TaskWindow
# from schedule_window import ScheduleWindow
# from quiz_window import QuizWindow
# from help_window import HelpWindow
# from distribute_window import DistributeWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем виджет стека для переключения окон
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Инициализируем окна
        self.login_window = LoginWindow(self)
        # self.task_window = TaskWindow(self)
        # self.schedule_window = ScheduleWindow(self)
        # self.quiz_window = QuizWindow(self)
        # self.help_window = HelpWindow(self)
        # self.distribute_window = DistributeWindow(self)

        # Добавляем окна в стек
        self.stack.addWidget(self.login_window)
        # self.stack.addWidget(self.task_window)
        # self.stack.addWidget(self.schedule_window)
        # self.stack.addWidget(self.quiz_window)
        # self.stack.addWidget(self.help_window)
        # self.stack.addWidget(self.distribute_window)

        # Показываем окно входа
        self.stack.setCurrentWidget(self.login_window)

    def switch_window(self, index):
        """Функция для переключения окон."""
        self.stack.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
