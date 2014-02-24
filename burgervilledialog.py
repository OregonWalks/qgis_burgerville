# -*- coding: utf-8 -*-
"""
/***************************************************************************
 burgerVilleDialog
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

from PyQt4 import QtCore, QtGui
from ui_burgerville import Ui_burgerVille
# create the dialog for zoom to point


class burgerVilleDialog(QtGui.QDialog, Ui_burgerVille):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        # Set up the user interface from Designer.
        self.ui = Ui_burgerVille()
        self.ui.setupUi(self)
    
    def setTextBrowser(self, output):
        self.ui.txtFeedback.setText(output)

    def clearTextBrowser(self):
        self.ui.txtFeedback.clear()
