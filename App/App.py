from App.UI.qtUI import Ui_MainWindow
from App.UI.UI import UI
from PyQt5 import QtWidgets

from configparser import ConfigParser
import sys
import os
from App.UI.Commands import InputHandler
from PyQt5 import QtCore, QtGui, QtWidgets

class App:
  cwd: str

  def __init__(self):

    appIsRunning = True
    self.cwd = os.getcwd()
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = QtWidgets.QMainWindow()
    qt = Ui_MainWindow()
    qt.setupUi(mainWindow)
    ui = UI(qt, mainWindow)

    inputHandler = InputHandler(self.cwd, ui)
    mainWindow.show()

    sys.exit(app.exec_())