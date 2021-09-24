# This Python file uses the following encoding: utf-8
import sys
from Widgets.OpenGLWidget import OpenGLWidget
from PySide2.QtWidgets import QApplication, QMainWindow


class IView(QMainWindow):
    def __init__(self, parent=None):
        super(IView, self).__init__(parent)
        self.openglWidget = OpenGLWidget(self)
        self.setCentralWidget(self.openglWidget)
        self.setWindowTitle("SceneViewer")
        self.setGeometry(200, 200, 400, 400)


if __name__ == "__main__":
    app = QApplication([])
    window = IView()
    window.show()
    sys.exit(app.exec_())
