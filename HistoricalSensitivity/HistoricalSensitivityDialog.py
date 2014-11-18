# -*- coding: utf-8 -*-
# ---------------------------------------------------------
#    HistoricalSensitivityDialog - the plugin's dialog
#
#    author               : Benedikt Budig
#    email                : benedikt.budig@uni-wuerzburg.de
# ---------------------------------------------------------

from PyQt4 import QtCore, QtGui

class HistoricalSensitivityDialog(QtGui.QDialog):
    def __init__(self, info):
        super(HistoricalSensitivityDialog, self).__init__()
        self.initUI(info)

    def initUI(self,info):
        # Add label with information about the presented assignment
        label = QtGui.QLabel('Sensitivity value: ' + str(info[0]) + '\n' + 
          'Assignment rank: ' + str(info[1] + 1) + ' of ' + str(info[2]), self)
        
        # Add buttons for 'Next' and 'Quit'
        nbtn = QtGui.QPushButton('Next', self)
        nbtn.clicked.connect(self.accept)
        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(self.reject)
        
        # Create dialog layout
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(nbtn)
        hbox.addWidget(qbtn)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(label)
        vbox.addLayout(hbox)
        vbox.setSpacing(10)
		
        self.setWindowTitle('HistoricalSensitivity')
        self.setLayout(vbox)
        self.show()

