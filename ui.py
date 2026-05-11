import PyQt6
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QSlider, QGroupBox,QTabWidget,QWidget,QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import SimulationVariables

class MainWindow(QMainWindow):
    def __init__(self, figure, axes):
        super().__init__()
        self.figure = figure
        self.axes = axes

        self.wlayout = QtWidgets.QHBoxLayout()
        self.ImageBox = FigureCanvas(self.figure)

        self.wlayout.addWidget(self.ImageBox)

        self.container = QWidget()
        self.container.setLayout(self.wlayout)
        self.setCentralWidget(self.container)


