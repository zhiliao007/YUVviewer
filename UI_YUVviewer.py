# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_YUVviewer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YUVviewer(object):
    def setupUi(self, YUVviewer):
        YUVviewer.setObjectName("YUVviewer")
        YUVviewer.resize(513, 151)
        self.centralwidget = QtWidgets.QWidget(YUVviewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.frameSizeType_CIF_RadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.frameSizeType_CIF_RadioButton.setObjectName("frameSizeType_CIF_RadioButton")
        self.gridLayout.addWidget(self.frameSizeType_CIF_RadioButton, 0, 0, 1, 1)
        self.frameSizeType_Other_RadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.frameSizeType_Other_RadioButton.setObjectName("frameSizeType_Other_RadioButton")
        self.gridLayout.addWidget(self.frameSizeType_Other_RadioButton, 2, 0, 1, 1)
        self.frameSizeType_QCIF_RadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.frameSizeType_QCIF_RadioButton.setObjectName("frameSizeType_QCIF_RadioButton")
        self.gridLayout.addWidget(self.frameSizeType_QCIF_RadioButton, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.YUVFormat_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.YUVFormat_ComboBox.setObjectName("YUVFormat_ComboBox")
        self.YUVFormat_ComboBox.addItem("")
        self.YUVFormat_ComboBox.addItem("")
        self.YUVFormat_ComboBox.addItem("")
        self.YUVFormat_ComboBox.addItem("")
        self.YUVFormat_ComboBox.addItem("")
        self.YUVFormat_ComboBox.addItem("")
        self.verticalLayout.addWidget(self.YUVFormat_ComboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frameSize_Width_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.frameSize_Width_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
        self.frameSize_Width_LineEdit.setObjectName("frameSize_Width_LineEdit")
        self.verticalLayout_2.addWidget(self.frameSize_Width_LineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.frameSize_Height_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.frameSize_Height_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
        self.frameSize_Height_LineEdit.setObjectName("frameSize_Height_LineEdit")
        self.verticalLayout_3.addWidget(self.frameSize_Height_LineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.frameRate_ComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.frameRate_ComboBox.setObjectName("frameRate_ComboBox")
        self.frameRate_ComboBox.addItem("")
        self.frameRate_ComboBox.addItem("")
        self.frameRate_ComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.frameRate_ComboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.startFrame_LineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.startFrame_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
        self.startFrame_LineEdit.setObjectName("startFrame_LineEdit")
        self.horizontalLayout_3.addWidget(self.startFrame_LineEdit)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.endFrame_LineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.endFrame_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
        self.endFrame_LineEdit.setObjectName("endFrame_LineEdit")
        self.horizontalLayout_3.addWidget(self.endFrame_LineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.openFile_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFile_PushButton.setObjectName("openFile_PushButton")
        self.verticalLayout_5.addWidget(self.openFile_PushButton)
        self.openFolder_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFolder_PushButton.setObjectName("openFolder_PushButton")
        self.verticalLayout_5.addWidget(self.openFolder_PushButton)
        self.about_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.about_PushButton.setObjectName("about_PushButton")
        self.verticalLayout_5.addWidget(self.about_PushButton)
        self.help_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.help_PushButton.setObjectName("help_PushButton")
        self.verticalLayout_5.addWidget(self.help_PushButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        YUVviewer.setCentralWidget(self.centralwidget)

        self.retranslateUi(YUVviewer)
        QtCore.QMetaObject.connectSlotsByName(YUVviewer)

    def retranslateUi(self, YUVviewer):
        _translate = QtCore.QCoreApplication.translate
        YUVviewer.setWindowTitle(_translate("YUVviewer", "YUVviewer"))
        self.groupBox.setTitle(_translate("YUVviewer", "Frame Size"))
        self.frameSizeType_CIF_RadioButton.setText(_translate("YUVviewer", "CIF"))
        self.frameSizeType_Other_RadioButton.setText(_translate("YUVviewer", "Other"))
        self.frameSizeType_QCIF_RadioButton.setText(_translate("YUVviewer", "QCIF"))
        self.label.setText(_translate("YUVviewer", "YUV Format"))
        self.YUVFormat_ComboBox.setItemText(0, _translate("YUVviewer", "YV12"))
        self.YUVFormat_ComboBox.setItemText(1, _translate("YUVviewer", "I420"))
        self.YUVFormat_ComboBox.setItemText(2, _translate("YUVviewer", "YUY2"))
        self.YUVFormat_ComboBox.setItemText(3, _translate("YUVviewer", "UYUV"))
        self.YUVFormat_ComboBox.setItemText(4, _translate("YUVviewer", "4:2:2"))
        self.YUVFormat_ComboBox.setItemText(5, _translate("YUVviewer", "4:4:4"))
        self.label_2.setText(_translate("YUVviewer", "Witdth"))
        self.label_3.setText(_translate("YUVviewer", "Height"))
        self.groupBox_2.setTitle(_translate("YUVviewer", "Play Parameters"))
        self.label_4.setText(_translate("YUVviewer", "Frame Rate"))
        self.frameRate_ComboBox.setItemText(0, _translate("YUVviewer", "30"))
        self.frameRate_ComboBox.setItemText(1, _translate("YUVviewer", "60"))
        self.frameRate_ComboBox.setItemText(2, _translate("YUVviewer", "120"))
        self.label_5.setText(_translate("YUVviewer", "From"))
        self.label_6.setText(_translate("YUVviewer", "To"))
        self.openFile_PushButton.setText(_translate("YUVviewer", "Open file"))
        self.openFolder_PushButton.setText(_translate("YUVviewer", "Open folder"))
        self.about_PushButton.setText(_translate("YUVviewer", "About"))
        self.help_PushButton.setText(_translate("YUVviewer", "Help"))

