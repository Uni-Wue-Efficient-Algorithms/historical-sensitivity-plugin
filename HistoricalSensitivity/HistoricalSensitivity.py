# -*- coding: utf-8 -*-
# ---------------------------------------------------------
#    HistoricalSensitivity - the plugin's business logic
#
#    author               : Benedikt Budig
#    email                : benedikt.budig@uni-wuerzburg.de
# ---------------------------------------------------------

# Import PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

# Initialize Qt resources from resources.py
import resources

# Import the dialog from HistoricalSensitivityDialog.py
from HistoricalSensitivityDialog import HistoricalSensitivityDialog

class HistoricalSensitivity: 
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):  
        # Create action that will start the plugin
        self.action = QAction(QIcon(":/plugins/HistoricalSensitivity/icon.png"),
          "Historical Map Sensitivity", self.iface.mainWindow())
        
        # Connect the action to the run method
        QObject.connect(self.action, SIGNAL("activated()"), self.run)
        
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Historical Map Sensitivity", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Historical Map Sensitivity",self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self): 
        # Get active QGIS layer
        layer = self.iface.activeLayer()
        try:
            # Sort features by sensitivity values
            features = layer.getFeatures()
            sortedFeatures = sorted(features,key=lambda x : x.attributes()[1])
        except:
            QMessageBox.critical(None, 'Layer Error', 
              'No valid layer selected. Please select a layer containing ' + 
              'sensitivity information and try again.')
            return
    
        # Iterate over features in ascending sensitivity order
        for feature in sortedFeatures:
            # Select and pan map to current feature
            layer.select(feature.id())
            self.iface.actionPanToSelected().trigger()
      
            # Show the dialog
            dlg = HistoricalSensitivityDialog([feature.attributes()[1], 
              sortedFeatures.index(feature), len(sortedFeatures)])  
            dlg.show()
            result = dlg.exec_() 
            
            # Check if 'Next' or 'Quit' was pressed
            if result == 1: 
                print "Next..."
            else:
                print "Aborting..."
                layer.deselect(feature.id())
                break
            layer.deselect(feature.id())

