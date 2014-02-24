# -*- coding: utf-8 -*-
"""
/***************************************************************************
 burgerVille
                                 A QGIS plugin
 make this work
                              -------------------
        begin                : 2014-02-23
        copyright            : (C) 2014 by Brylie and katie
        email                : this@that.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from burgervilledialog import burgerVilleDialog
import os.path
# QGIS import
from qgis.gui import *

class burgerVille:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # Reference to map canvas
        self.canvas = self.iface.mapCanvas() #CHANGE
        # Emit a QgsPoint after each click on the map canvas
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'burgerville_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = burgerVilleDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/burgerville/icon.png"),
            u"text for the menu item", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&best fries", self.action)
        result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )
    def handleMouseDown(self, point, button):
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )
        #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&best fries", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # make clickTool the tool that we'll use for now
        self.canvas.setMapTool(self.clickTool)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass
