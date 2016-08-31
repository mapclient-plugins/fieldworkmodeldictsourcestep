# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Wed Aug 31 12:43:03 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QtGui.QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(ConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label0)
        self.lineEdit0 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName("lineEdit0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit0)
        self.label1 = QtGui.QLabel(self.configGroupBox)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit1 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit1.setObjectName("lineEdit1")
        self.horizontalLayout_2.addWidget(self.lineEdit1)
        self.fileLocButton = QtGui.QPushButton(self.configGroupBox)
        self.fileLocButton.setObjectName("fileLocButton")
        self.horizontalLayout_2.addWidget(self.fileLocButton)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)
        ConfigureDialog.setTabOrder(self.lineEdit0, self.lineEdit1)
        ConfigureDialog.setTabOrder(self.lineEdit1, self.fileLocButton)
        ConfigureDialog.setTabOrder(self.fileLocButton, self.buttonBox)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Fieldwork Model Dict Source Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("ConfigureDialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("ConfigureDialog", "Config File:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.fileLocButton.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))

