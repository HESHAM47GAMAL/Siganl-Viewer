# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI12.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from PyQt5 import QtCore, QtWidgets
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget
import sys
import shutil
import os
import csv
import datetime
import numpy as np
import pandas as pd
import pyqtgraph.exporters
import pyqtgraph as pg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore, QtGui, QtWidgets

from pyqtgraph import PlotWidget
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore
import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import os
from scipy import signal
import matplotlib.pyplot as plt
import pyqtgraph.exporters
from matplotlib.animation import FuncAnimation


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONS/wicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 480, 1201, 281))
        self.tabWidget.setIconSize(QtCore.QSize(60, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.hide_1 = QtWidgets.QCheckBox(self.tab_1)
        self.hide_1.setGeometry(QtCore.QRect(730, 75, 89, 20))
        self.hide_1.setObjectName("hide_1")
        self.labelY_1 = QtWidgets.QLabel(self.tab_1)
        self.labelY_1.setGeometry(QtCore.QRect(478, 155, 42, 32))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelY_1.setFont(font)
        self.labelY_1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelY_1.setObjectName("labelY_1")
        self.speedSlider_1 = QtWidgets.QSlider(self.tab_1)
        self.speedSlider_1.setGeometry(QtCore.QRect(488, 75, 181, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speedSlider_1.sizePolicy().hasHeightForWidth())
        self.speedSlider_1.setMaximum(50)
        self.speedSlider_1.setMinimum(1)
        self.speedSlider_1.setSizePolicy(sizePolicy)
        self.speedSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider_1.setObjectName("speedSlider_1")
        self.horizontalSlider_1 = QtWidgets.QSlider(self.tab_1)
        self.horizontalSlider_1.setGeometry(QtCore.QRect(658, 165, 181, 22))
        self.horizontalSlider_1.setMaximum(10)
        self.horizontalSlider_1.setMinimum(0)
        self.horizontalSlider_1.setSingleStep(1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_1.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_1.setSizePolicy(sizePolicy)
        self.horizontalSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1.setObjectName("horizontalSlider_1")
        self.play_1 = QtWidgets.QPushButton(self.tab_1)
        self.play_1.setGeometry(QtCore.QRect(29, 160, 93, 29))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.play_1.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ICONS/play1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_1.setIcon(icon1)
        self.play_1.setObjectName("play_1")
        self.open_1 = QtWidgets.QPushButton(self.tab_1)
        self.open_1.setGeometry(QtCore.QRect(29, 66, 93, 29))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ICONS/open1.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_1.setIcon(icon2)
        self.open_1.setObjectName("open_1")
        self.verticalSlider_1 = QtWidgets.QSlider(self.tab_1)
        self.verticalSlider_1.setGeometry(QtCore.QRect(546, 125, 22, 91))
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.verticalSlider_1.setMaximum(5)
        self.verticalSlider_1.setMinimum(-5)
        self.verticalSlider_1.setSingleStep(1)
        self.pause_1 = QtWidgets.QPushButton(self.tab_1)
        self.pause_1.setGeometry(QtCore.QRect(130, 160, 93, 29))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pause_1.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ICONS/pause1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_1.setIcon(icon3)
        self.pause_1.setObjectName("pause_1")
        self.zoom_out_1 = QtWidgets.QPushButton(self.tab_1)
        self.zoom_out_1.setGeometry(QtCore.QRect(333, 160, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        self.zoom_out_1.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ICONS/zoomout1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out_1.setIcon(icon4)
        self.zoom_out_1.setObjectName("zoom_out_1")
        self.labelX_1 = QtWidgets.QLabel(self.tab_1)
        self.labelX_1.setGeometry(QtCore.QRect(588, 155, 42, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelX_1.setFont(font)
        self.labelX_1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelX_1.setObjectName("labelX_1")
        self.zoom_in_1 = QtWidgets.QPushButton(self.tab_1)
        self.zoom_in_1.setGeometry(QtCore.QRect(232, 160, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        self.zoom_in_1.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ICONS/zoomin1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in_1.setIcon(icon5)
        self.zoom_in_1.setChecked(False)
        self.zoom_in_1.setObjectName("zoom_in_1")
        self.labelSpeed_1 = QtWidgets.QLabel(self.tab_1)
        self.labelSpeed_1.setGeometry(QtCore.QRect(358, 75, 105, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelSpeed_1.setFont(font)
        self.labelSpeed_1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeed_1.setObjectName("labelSpeed_1")
        self.comboBoxColor_1 = QtWidgets.QComboBox(self.tab_1)
        self.comboBoxColor_1.setGeometry(QtCore.QRect(168, 75, 121, 22))
        self.comboBoxColor_1.setEditable(True)
        self.comboBoxColor_1.setObjectName("comboBoxColor_1")
        self.comboBoxColor_1.addItem("")
        self.comboBoxColor_1.addItem("")
        self.comboBoxColor_1.addItem("")
        self.comboBox_ColorPalette_1 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_ColorPalette_1.setGeometry(QtCore.QRect(950, 220, 161, 22))
        self.comboBox_ColorPalette_1.setEditable(True)
        self.comboBox_ColorPalette_1.setObjectName("comboBox_ColorPalette_1")
        self.comboBox_ColorPalette_1.addItem("")
        self.comboBox_ColorPalette_1.addItem("")
        self.comboBox_ColorPalette_1.addItem("")
        self.comboBox_ColorPalette_1.addItem("")
        self.comboBox_ColorPalette_1.addItem("")
        self.labelSpecVMax_1 = QtWidgets.QLabel(self.tab_1)
        self.labelSpecVMax_1.setGeometry(QtCore.QRect(910, 180, 36, 22))
        self.labelSpecVMax_1.setObjectName("labelSpecVMax_1")
        self.labelSpecVMin_1 = QtWidgets.QLabel(self.tab_1)
        self.labelSpecVMin_1.setGeometry(QtCore.QRect(1110, 180, 33, 22))
        self.labelSpecVMin_1.setObjectName("labelSpecVMin_1")
        self.SpecVMinSlider_1 = QtWidgets.QSlider(self.tab_1)
        self.SpecVMinSlider_1.setGeometry(QtCore.QRect(1110, 40, 22, 141))
        self.SpecVMinSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.SpecVMinSlider_1.setObjectName("SpecVMinSlider_1")





        self.SpecVMaxSlider_1 = QtWidgets.QSlider(self.tab_1)
        self.SpecVMaxSlider_1.setGeometry(QtCore.QRect(920, 40, 22, 141))
        self.SpecVMaxSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.SpecVMaxSlider_1.setObjectName("SpecVMaxSlider_1")

        self.SpecVMinSlider_1.setMaximum(0)
        self.SpecVMinSlider_1.setMinimum(-50)
        self.SpecVMinSlider_1.setSingleStep(1)


        self.SpecVMaxSlider_1.setMaximum(-51)
        self.SpecVMaxSlider_1.setMinimum(-250)
        self.SpecVMaxSlider_1.setSingleStep(1)





        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.labelSpeed_2 = QtWidgets.QLabel(self.tab_2)
        self.labelSpeed_2.setGeometry(QtCore.QRect(358, 75, 105, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelSpeed_2.setFont(font)
        self.labelSpeed_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeed_2.setObjectName("labelSpeed_2")
        self.labelY_2 = QtWidgets.QLabel(self.tab_2)
        self.labelY_2.setGeometry(QtCore.QRect(478, 155, 42, 32))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelY_2.setFont(font)
        self.labelY_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelY_2.setObjectName("labelY_2")
        self.zoom_in_2 = QtWidgets.QPushButton(self.tab_2)
        self.zoom_in_2.setGeometry(QtCore.QRect(232, 160, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        self.zoom_in_2.setFont(font)
        self.zoom_in_2.setIcon(icon5)
        self.zoom_in_2.setChecked(False)
        self.zoom_in_2.setObjectName("zoom_in_2")
        self.hide_2 = QtWidgets.QCheckBox(self.tab_2)
        self.hide_2.setGeometry(QtCore.QRect(730, 75, 89, 20))
        self.hide_2.setObjectName("hide_2")
        self.zoom_out_2 = QtWidgets.QPushButton(self.tab_2)
        self.zoom_out_2.setGeometry(QtCore.QRect(333, 160, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        self.zoom_out_2.setFont(font)
        self.zoom_out_2.setIcon(icon4)
        self.zoom_out_2.setObjectName("zoom_out_2")
        self.open_2 = QtWidgets.QPushButton(self.tab_2)
        self.open_2.setGeometry(QtCore.QRect(29, 66, 93, 29))
        self.open_2.setIcon(icon2)
        self.open_2.setObjectName("open_2")
        self.play_2 = QtWidgets.QPushButton(self.tab_2)
        self.play_2.setGeometry(QtCore.QRect(29, 160, 93, 29))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.play_2.setFont(font)
        self.play_2.setIcon(icon1)
        self.play_2.setObjectName("play_2")
        self.speedSlider_2 = QtWidgets.QSlider(self.tab_2)
        self.speedSlider_2.setGeometry(QtCore.QRect(488, 75, 181, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speedSlider_2.sizePolicy().hasHeightForWidth())
        self.speedSlider_2.setMaximum(50)
        self.speedSlider_2.setMinimum(1)
        self.speedSlider_2.setSizePolicy(sizePolicy)
        self.speedSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider_2.setObjectName("speedSlider_2")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(658, 165, 181, 22))
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setSingleStep(1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.comboBoxColor_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBoxColor_2.setGeometry(QtCore.QRect(168, 75, 121, 22))
        self.comboBoxColor_2.setEditable(True)
        self.comboBoxColor_2.setObjectName("comboBoxColor_2")
        self.comboBoxColor_2.addItem("")
        self.comboBoxColor_2.addItem("")
        self.comboBoxColor_2.addItem("")
        self.labelX_2 = QtWidgets.QLabel(self.tab_2)
        self.labelX_2.setGeometry(QtCore.QRect(588, 155, 42, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelX_2.setFont(font)
        self.labelX_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelX_2.setObjectName("labelX_2")
        self.verticalSlider_2 = QtWidgets.QSlider(self.tab_2)
        self.verticalSlider_2.setGeometry(QtCore.QRect(546, 125, 22, 91))
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_2.setMaximum(5)
        self.verticalSlider_2.setMinimum(-5)
        self.verticalSlider_2.setSingleStep(1)
        self.pause_2 = QtWidgets.QPushButton(self.tab_2)
        self.pause_2.setGeometry(QtCore.QRect(130, 160, 93, 29))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pause_2.setFont(font)
        self.pause_2.setIcon(icon3)
        self.pause_2.setObjectName("pause_2")
        self.comboBox_ColorPalette_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_ColorPalette_2.setGeometry(QtCore.QRect(950, 220, 161, 22))
        self.comboBox_ColorPalette_2.setEditable(True)
        self.comboBox_ColorPalette_2.setObjectName("comboBox_ColorPalette_2")
        self.comboBox_ColorPalette_2.addItem("")
        self.comboBox_ColorPalette_2.addItem("")
        self.comboBox_ColorPalette_2.addItem("")
        self.comboBox_ColorPalette_2.addItem("")
        self.comboBox_ColorPalette_2.addItem("")
        self.labelSpecVMax_2 = QtWidgets.QLabel(self.tab_2)
        self.labelSpecVMax_2.setGeometry(QtCore.QRect(910, 180, 36, 22))
        self.labelSpecVMax_2.setObjectName("labelSpecVMax_2")
        self.labelSpecVMin_2 = QtWidgets.QLabel(self.tab_2)
        self.labelSpecVMin_2.setGeometry(QtCore.QRect(1110, 180, 33, 22))
        self.labelSpecVMin_2.setObjectName("labelSpecVMin_2")
        self.SpecVMinSlider_2 = QtWidgets.QSlider(self.tab_2)
        self.SpecVMinSlider_2.setGeometry(QtCore.QRect(1110, 40, 22, 141))
        self.SpecVMinSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.SpecVMinSlider_2.setObjectName("SpecVMinSlider_2")
        self.SpecVMaxSlider_2 = QtWidgets.QSlider(self.tab_2)
        self.SpecVMaxSlider_2.setGeometry(QtCore.QRect(920, 40, 22, 141))
        self.SpecVMaxSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.SpecVMaxSlider_2.setObjectName("SpecVMaxSlider_2")
        self.SpecVMinSlider_2.setMaximum(0)
        self.SpecVMinSlider_2.setMinimum(-50)
        self.SpecVMinSlider_2.setSingleStep(1)
        self.SpecVMaxSlider_2.setMaximum(-50)
        self.SpecVMaxSlider_2.setMinimum(-250)
        self.SpecVMaxSlider_2.setSingleStep(1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.labelY_3 = QtWidgets.QLabel(self.tab_3)
        self.labelY_3.setGeometry(QtCore.QRect(478, 155, 42, 32))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelY_3.setFont(font)
        self.labelY_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelY_3.setObjectName("labelY_3")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.tab_3)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(658, 165, 181, 22))
        self.horizontalSlider_3.setMaximum(10)
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setSingleStep(1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.comboBoxColor_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxColor_3.setGeometry(QtCore.QRect(168, 75, 121, 22))
        self.comboBoxColor_3.setEditable(True)
        self.comboBoxColor_3.setObjectName("comboBoxColor_3")
        self.comboBoxColor_3.addItem("")
        self.comboBoxColor_3.addItem("")
        self.comboBoxColor_3.addItem("")
        self.pause_3 = QtWidgets.QPushButton(self.tab_3)
        self.pause_3.setGeometry(QtCore.QRect(130, 160, 93, 29))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pause_3.setFont(font)
        self.pause_3.setIcon(icon3)
        self.pause_3.setObjectName("pause_3")
        self.labelX_3 = QtWidgets.QLabel(self.tab_3)
        self.labelX_3.setGeometry(QtCore.QRect(588, 155, 42, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelX_3.setFont(font)
        self.labelX_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelX_3.setObjectName("labelX_3")
        self.speedSlider_3 = QtWidgets.QSlider(self.tab_3)
        self.speedSlider_3.setGeometry(QtCore.QRect(488, 75, 181, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speedSlider_3.sizePolicy().hasHeightForWidth())
        self.speedSlider_3.setMaximum(50)
        self.speedSlider_3.setMinimum(1)
        self.speedSlider_3.setSizePolicy(sizePolicy)
        self.speedSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider_3.setObjectName("speedSlider_3")
        self.zoom_in_3 = QtWidgets.QPushButton(self.tab_3)
        self.zoom_in_3.setGeometry(QtCore.QRect(232, 160, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        self.zoom_in_3.setFont(font)
        self.zoom_in_3.setIcon(icon5)
        self.zoom_in_3.setChecked(False)
        self.zoom_in_3.setObjectName("zoom_in_3")
        self.play_3 = QtWidgets.QPushButton(self.tab_3)
        self.play_3.setGeometry(QtCore.QRect(29, 160, 93, 29))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.play_3.setFont(font)
        self.play_3.setIcon(icon1)
        self.play_3.setObjectName("play_3")
        self.hide_3 = QtWidgets.QCheckBox(self.tab_3)
        self.hide_3.setGeometry(QtCore.QRect(730, 75, 89, 20))
        self.hide_3.setObjectName("hide_3")
        self.zoom_out_3 = QtWidgets.QPushButton(self.tab_3)
        self.zoom_out_3.setGeometry(QtCore.QRect(333, 160, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        self.zoom_out_3.setFont(font)
        self.zoom_out_3.setIcon(icon4)
        self.zoom_out_3.setObjectName("zoom_out_3")
        self.comboBox_ColorPalette_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_ColorPalette_3.setGeometry(QtCore.QRect(950, 220, 161, 22))
        self.comboBox_ColorPalette_3.setEditable(True)
        self.comboBox_ColorPalette_3.setObjectName("comboBox_ColorPalette_3")
        self.comboBox_ColorPalette_3.addItem("")
        self.comboBox_ColorPalette_3.addItem("")
        self.comboBox_ColorPalette_3.addItem("")
        self.comboBox_ColorPalette_3.addItem("")
        self.comboBox_ColorPalette_3.addItem("")
        self.open_3 = QtWidgets.QPushButton(self.tab_3)
        self.open_3.setGeometry(QtCore.QRect(29, 66, 93, 29))
        self.open_3.setIcon(icon2)
        self.open_3.setObjectName("open_3")
        self.verticalSlider_3 = QtWidgets.QSlider(self.tab_3)
        self.verticalSlider_3.setGeometry(QtCore.QRect(546, 125, 22, 91))
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalSlider_3.setMaximum(5)
        self.verticalSlider_3.setMinimum(-5)
        self.verticalSlider_3.setSingleStep(1)
        self.labelSpeed_3 = QtWidgets.QLabel(self.tab_3)
        self.labelSpeed_3.setGeometry(QtCore.QRect(358, 75, 105, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelSpeed_3.setFont(font)
        self.labelSpeed_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeed_3.setObjectName("labelSpeed_3")
        self.labelSpecVMax_3 = QtWidgets.QLabel(self.tab_3)
        self.labelSpecVMax_3.setGeometry(QtCore.QRect(910, 180, 36, 22))
        self.labelSpecVMax_3.setObjectName("labelSpecVMax_3")
        self.labelSpecVMin_3 = QtWidgets.QLabel(self.tab_3)
        self.labelSpecVMin_3.setGeometry(QtCore.QRect(1110, 180, 33, 22))
        self.labelSpecVMin_3.setObjectName("labelSpecVMin_3")
        self.SpecVMinSlider_3 = QtWidgets.QSlider(self.tab_3)
        self.SpecVMinSlider_3.setGeometry(QtCore.QRect(1110, 40, 22, 141))
        self.SpecVMinSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.SpecVMinSlider_3.setObjectName("SpecVMinSlider_3")
        self.SpecVMaxSlider_3 = QtWidgets.QSlider(self.tab_3)
        self.SpecVMaxSlider_3.setGeometry(QtCore.QRect(920, 40, 22, 141))
        self.SpecVMaxSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.SpecVMaxSlider_3.setObjectName("SpecVMaxSlider_3")
        self.SpecVMinSlider_3.setMaximum(0)
        self.SpecVMinSlider_3.setMinimum(-50)
        self.SpecVMinSlider_3.setSingleStep(1)
        self.SpecVMaxSlider_3.setMaximum(-51)
        self.SpecVMaxSlider_3.setMinimum(-250)
        self.SpecVMaxSlider_3.setSingleStep(1)
        self.tabWidget.addTab(self.tab_3, "")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 11, 1201, 451))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView_1 = PlotWidget(self.widget)
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.graphicsView_1.getPlotItem().hideAxis('bottom')
        self.verticalLayout.addWidget(self.graphicsView_1)
        self.graphicsView_2 = PlotWidget(self.widget)
        self.graphicsView_2.setInteractive(True)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_2.getPlotItem().hideAxis('bottom')
        self.verticalLayout.addWidget(self.graphicsView_2)
        self.graphicsView_3 = PlotWidget(self.widget)
        self.graphicsView_3.setInteractive(True)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_3.getPlotItem().hideAxis('bottom')
        self.verticalLayout.addWidget(self.graphicsView_3)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget_2.setObjectName("tabWidget_2")


        self.tabSpec_1 = QtWidgets.QWidget()
        self.tabSpec_1.setObjectName("tabSpec_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tabSpec_1)
        self.gridLayout.setObjectName("gridLayout")
        self.Spec_1 = QtWidgets.QWidget(self.tabSpec_1)
        self.Spec_1.setObjectName("Spec_1")
        self.l_1 = QtWidgets.QVBoxLayout(self.Spec_1)
        self.canvas_1 = MyMplCanvas(self.Spec_1)
        self.gridLayout.addWidget(self.canvas_1, 0, 0, 1, 1)



        self.tabWidget_2.addTab(self.tabSpec_1, "")
        self.tabSpec_2 = QtWidgets.QWidget()
        self.tabSpec_2.setObjectName("tabSpec_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabSpec_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Spec_2 = QtWidgets.QWidget(self.tabSpec_2)
        self.Spec_2.setObjectName("Spec_2")
        self.l_2 = QtWidgets.QVBoxLayout(self.Spec_2)
        self.canvas_2 = MyMplCanvas(self.Spec_2)
        self.gridLayout_2.addWidget(self.canvas_2, 0, 0, 1, 1)


        self.tabWidget_2.addTab(self.tabSpec_2, "")
        self.tabSpec_3 = QtWidgets.QWidget()
        self.tabSpec_3.setObjectName("tabSpec_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabSpec_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Spec_3 = QtWidgets.QWidget(self.tabSpec_3)
        self.Spec_3.setObjectName("Spec_3")
        self.l_3 = QtWidgets.QVBoxLayout(self.Spec_3)
        self.canvas_3 = MyMplCanvas(self.Spec_3)
        self.gridLayout_3.addWidget(self.canvas_3, 0, 0, 1, 1)




        self.tabWidget_2.addTab(self.tabSpec_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionChannel_1 = QtWidgets.QAction(MainWindow)
        self.actionChannel_1.setObjectName("actionChannel_1")
        self.actionChannel_2 = QtWidgets.QAction(MainWindow)
        self.actionChannel_2.setObjectName("actionChannel_2")
        self.actionChannel_3 = QtWidgets.QAction(MainWindow)
        self.actionChannel_3.setObjectName("actionChannel_3")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionGenerate_PDF = QtWidgets.QAction(MainWindow)
        self.actionGenerate_PDF.setObjectName("actionGenerate_PDF")
        self.menuOpen.addAction(self.actionChannel_1)
        self.menuOpen.addAction(self.actionChannel_2)
        self.menuOpen.addAction(self.actionChannel_3)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.actionGenerate_PDF)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.palette = ['viridis', 'plasma', 'Blues', 'Greys','pink']


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal Viewer"))
        self.hide_1.setText(_translate("MainWindow", "Hide Signal"))
        self.labelY_1.setText(_translate("MainWindow", "<html><head/><body><p>Scroll<br/>Y-Axis</p></body></html>"))
        self.play_1.setText(_translate("MainWindow", "PLAY"))
        self.open_1.setText(_translate("MainWindow", "OPEN"))
        self.pause_1.setText(_translate("MainWindow", "PAUSE"))
        self.zoom_out_1.setText(_translate("MainWindow", "ZOOM\n"
"OUT"))
        self.labelX_1.setText(_translate("MainWindow", "<html><head/><body><p>Scroll<br/>X-Axis</p></body></html>"))
        self.zoom_in_1.setText(_translate("MainWindow", "ZOOM\n"
"IN"))
        self.labelSpeed_1.setText(_translate("MainWindow", "<html><head/><body><p>Speed Control</p></body></html>"))
        self.comboBoxColor_1.setCurrentText(_translate("MainWindow", "RED"))
        self.comboBoxColor_1.setItemText(0, _translate("MainWindow", "RED"))
        self.comboBoxColor_1.setItemText(1, _translate("MainWindow", "Green"))
        self.comboBoxColor_1.setItemText(2, _translate("MainWindow", "Blue"))
        self.comboBox_ColorPalette_1.setCurrentText(_translate("MainWindow", "Color palette 1"))
        self.comboBox_ColorPalette_1.setItemText(0, _translate("MainWindow", "Color palette 1"))
        self.comboBox_ColorPalette_1.setItemText(1, _translate("MainWindow", "Color palette 2"))
        self.comboBox_ColorPalette_1.setItemText(2, _translate("MainWindow", "Color palette 3"))
        self.comboBox_ColorPalette_1.setItemText(3, _translate("MainWindow", "Color palette 4"))
        self.comboBox_ColorPalette_1.setItemText(4, _translate("MainWindow", "Color palette 5"))
        self.labelSpecVMax_1.setText(_translate("MainWindow", "V-Max"))
        self.labelSpecVMin_1.setText(_translate("MainWindow", "V-Min"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Channel 1"))
        self.labelSpeed_2.setText(_translate("MainWindow", "<html><head/><body><p>Speed Control</p></body></html>"))
        self.labelY_2.setText(_translate("MainWindow", "<html><head/><body><p>Scroll<br/>Y-Axis</p></body></html>"))
        self.zoom_in_2.setText(_translate("MainWindow", "ZOOM\n"
"IN"))
        self.hide_2.setText(_translate("MainWindow", "Hide Signal"))
        self.zoom_out_2.setText(_translate("MainWindow", "ZOOM\n"
"OUT"))
        self.open_2.setText(_translate("MainWindow", "OPEN"))
        self.play_2.setText(_translate("MainWindow", "PLAY"))
        self.comboBoxColor_2.setCurrentText(_translate("MainWindow", "RED"))
        self.comboBoxColor_2.setItemText(0, _translate("MainWindow", "RED"))
        self.comboBoxColor_2.setItemText(1, _translate("MainWindow", "Green"))
        self.comboBoxColor_2.setItemText(2, _translate("MainWindow", "Blue"))
        self.labelX_2.setText(_translate("MainWindow", "<html><head/><body><p>Scroll<br/>X-Axis</p></body></html>"))
        self.pause_2.setText(_translate("MainWindow", "PAUSE"))
        self.comboBox_ColorPalette_2.setCurrentText(_translate("MainWindow", "Color palette 1"))
        self.comboBox_ColorPalette_2.setItemText(0, _translate("MainWindow", "Color palette 1"))
        self.comboBox_ColorPalette_2.setItemText(1, _translate("MainWindow", "Color palette 2"))
        self.comboBox_ColorPalette_2.setItemText(2, _translate("MainWindow", "Color palette 3"))
        self.comboBox_ColorPalette_2.setItemText(3, _translate("MainWindow", "Color palette 4"))
        self.comboBox_ColorPalette_2.setItemText(4, _translate("MainWindow", "Color palette 5"))
        self.labelSpecVMax_2.setText(_translate("MainWindow", "V-Max"))
        self.labelSpecVMin_2.setText(_translate("MainWindow", "V-Min"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Channel 2"))
        self.labelY_3.setText(_translate("MainWindow", "<html><head/><body><p>Scroll<br/>Y-Axis</p></body></html>"))
        self.comboBoxColor_3.setCurrentText(_translate("MainWindow", "RED"))
        self.comboBoxColor_3.setItemText(0, _translate("MainWindow", "RED"))
        self.comboBoxColor_3.setItemText(1, _translate("MainWindow", "Green"))
        self.comboBoxColor_3.setItemText(2, _translate("MainWindow", "Blue"))
        self.pause_3.setText(_translate("MainWindow", "PAUSE"))
        self.labelX_3.setText(_translate("MainWindow", "<html><head/><body><p>Scroll<br/>X-Axis</p></body></html>"))
        self.zoom_in_3.setText(_translate("MainWindow", "ZOOM\n"
"IN"))
        self.play_3.setText(_translate("MainWindow", "PLAY"))
        self.hide_3.setText(_translate("MainWindow", "Hide Signal"))
        self.zoom_out_3.setText(_translate("MainWindow", "ZOOM\n"
"OUT"))
        self.comboBox_ColorPalette_3.setCurrentText(_translate("MainWindow", "Color palette 1"))
        self.comboBox_ColorPalette_3.setItemText(0, _translate("MainWindow", "Color palette 1"))
        self.comboBox_ColorPalette_3.setItemText(1, _translate("MainWindow", "Color palette 2"))
        self.comboBox_ColorPalette_3.setItemText(2, _translate("MainWindow", "Color palette 3"))
        self.comboBox_ColorPalette_3.setItemText(3, _translate("MainWindow", "Color palette 4"))
        self.comboBox_ColorPalette_3.setItemText(4, _translate("MainWindow", "Color palette 5"))
        self.open_3.setText(_translate("MainWindow", "OPEN"))
        self.labelSpeed_3.setText(_translate("MainWindow", "<html><head/><body><p>Speed Control</p></body></html>"))
        self.labelSpecVMax_3.setText(_translate("MainWindow", "V-Max"))
        self.labelSpecVMin_3.setText(_translate("MainWindow", "V-Min"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Channel 3"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabSpec_1), _translate("MainWindow", "Channel 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabSpec_2), _translate("MainWindow", "Channel 2"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabSpec_3), _translate("MainWindow", "Channel 3"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionChannel_1.setText(_translate("MainWindow", "Channel_1"))
        self.actionChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_3.setText(_translate("MainWindow", "Channel 3"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionGenerate_PDF.setText(_translate("MainWindow", "Generate PDF"))

class MyMplCanvas(FigureCanvas):


    def __init__(self, parent=None, width=2, height=2, dpi=100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.figure = plt.Figure()
        super().__init__(fig)

        self.axes = fig.add_subplot(111)


        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
