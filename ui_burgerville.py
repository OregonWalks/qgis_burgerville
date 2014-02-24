# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_burgerville.ui'
#
# Created: Sun Feb 23 19:59:18 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_burgerVille(object):
    def setupUi(self, burgerVille):
        burgerVille.setObjectName(_fromUtf8("burgerVille"))
        burgerVille.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(burgerVille)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.txtFeedback = QtGui.QTextBrowser(burgerVille)
        self.txtFeedback.setGeometry(QtCore.QRect(20, 20, 361, 192))
        self.txtFeedback.setObjectName(_fromUtf8("txtFeedback"))
        self.chkActivate = QtGui.QCheckBox(burgerVille)
        self.chkActivate.setGeometry(QtCore.QRect(20, 240, 97, 41))
        self.chkActivate.setObjectName(_fromUtf8("chkActivate"))

        self.retranslateUi(burgerVille)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), burgerVille.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), burgerVille.reject)
        QtCore.QMetaObject.connectSlotsByName(burgerVille)

    def retranslateUi(self, burgerVille):
        burgerVille.setWindowTitle(QtGui.QApplication.translate("burgerVille", "burgerVille", None, QtGui.QApplication.UnicodeUTF8))
        self.chkActivate.setText(QtGui.QApplication.translate("burgerVille", "Activate\n"
"(Check)", None, QtGui.QApplication.UnicodeUTF8))

