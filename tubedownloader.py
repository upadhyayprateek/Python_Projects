# Python Project for Youtube Downloader

# Necessary Installs in the terminal

#1. pip install 
#2. pip install 

#Necessaty imports

from __future__ import unicode_literals
import os
import youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable


# Operating a window of Tube Downloader

class MainWindow(QMainWindow):
 def __init__(self):
  super(MainWindow,self).__init__()
  self.setGeometry(200,200,502,316)
  self.setWindowTitle("YOUTUBE DOWNLOADER")
  self.font = QtGui.QFont()
  self.font.setFamily("Leelawdee UI")
  self.std_download_path = str(os.path.join(os.path.expanduser("~"), "Downloads"))
  self.initUI()

 def initUI(self):
  self.label_top = QtWidgets.QLabel(self)
  self.label_top.setObjectName("label_top")
  self.label_top.setGeometry


