# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 950)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.system_input = QtWidgets.QLineEdit(self.centralwidget)
        self.system_input.setToolTip("")
        self.system_input.setObjectName("system_input")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.system_input)
        self.first_cycle_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.first_cycle_spinBox.setToolTip("")
        self.first_cycle_spinBox.setMinimum(1)
        self.first_cycle_spinBox.setMaximum(1000000)
        self.first_cycle_spinBox.setProperty("value", 1)
        self.first_cycle_spinBox.setObjectName("first_cycle_spinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.first_cycle_spinBox)
        self.num_cycles_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.num_cycles_spinBox.setToolTip("")
        self.num_cycles_spinBox.setStatusTip("")
        self.num_cycles_spinBox.setMinimum(1)
        self.num_cycles_spinBox.setMaximum(100000)
        self.num_cycles_spinBox.setProperty("value", 10)
        self.num_cycles_spinBox.setObjectName("num_cycles_spinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.num_cycles_spinBox)
        self.mass_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.mass_doubleSpinBox.setToolTip("")
        self.mass_doubleSpinBox.setMinimum(0.0)
        self.mass_doubleSpinBox.setMaximum(1000000000.0)
        self.mass_doubleSpinBox.setProperty("value", 15.0)
        self.mass_doubleSpinBox.setObjectName("mass_doubleSpinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mass_doubleSpinBox)
        self.ratio_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ratio_input.setToolTip("")
        self.ratio_input.setObjectName("ratio_input")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ratio_input)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.type_input = QtWidgets.QLineEdit(self.centralwidget)
        self.type_input.setObjectName("type_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.type_input)
        self.anode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.anode_input.setObjectName("anode_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.anode_input)
        self.comments_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comments_input.sizePolicy().hasHeightForWidth())
        self.comments_input.setSizePolicy(sizePolicy)
        self.comments_input.setMinimumSize(QtCore.QSize(0, 0))
        self.comments_input.setPlainText("")
        self.comments_input.setObjectName("comments_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comments_input)
        self.rate_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.rate_comboBox.setToolTip("")
        self.rate_comboBox.setEditable(True)
        self.rate_comboBox.setObjectName("rate_comboBox")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rate_comboBox)
        self.horizontalLayout.addLayout(self.formLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.raw_inputfile = QtWidgets.QLineEdit(self.centralwidget)
        self.raw_inputfile.setText("")
        self.raw_inputfile.setObjectName("raw_inputfile")
        self.horizontalLayout_17.addWidget(self.raw_inputfile)
        self.raw_button = QtWidgets.QPushButton(self.centralwidget)
        self.raw_button.setObjectName("raw_button")
        self.horizontalLayout_17.addWidget(self.raw_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.figure_path = QtWidgets.QLineEdit(self.centralwidget)
        self.figure_path.setText("")
        self.figure_path.setObjectName("figure_path")
        self.horizontalLayout_15.addWidget(self.figure_path)
        self.plot_button = QtWidgets.QPushButton(self.centralwidget)
        self.plot_button.setObjectName("plot_button")
        self.horizontalLayout_15.addWidget(self.plot_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.table_path = QtWidgets.QLineEdit(self.centralwidget)
        self.table_path.setText("")
        self.table_path.setObjectName("table_path")
        self.horizontalLayout_16.addWidget(self.table_path)
        self.table_button = QtWidgets.QPushButton(self.centralwidget)
        self.table_button.setObjectName("table_button")
        self.horizontalLayout_16.addWidget(self.table_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setObjectName("run_button")
        self.horizontalLayout_2.addWidget(self.run_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(4, 5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.rate_comboBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Electrochemical Parsing"))
        self.label.setToolTip(_translate("MainWindow", "The mass ratio between the active material, carbon, and binder"))
        self.label.setText(_translate("MainWindow", "Active:Carbon:Binder Ratio"))
        self.label_6.setToolTip(_translate("MainWindow", "The total cathode mass, including active material, carbon, and binder"))
        self.label_6.setText(_translate("MainWindow", "Cathode Mass (mg)"))
        self.label_7.setToolTip(_translate("MainWindow", "The number of charge/ discharge cycles to plot"))
        self.label_7.setText(_translate("MainWindow", "Number of Cycles to Plot"))
        self.label_8.setToolTip(_translate("MainWindow", "The cycle number you want to start plotting from. This will not affect calculations."))
        self.label_8.setText(_translate("MainWindow", "First Cycle to Plot"))
        self.label_9.setToolTip(_translate("MainWindow", "The name of your system. If left blank, a name will be generated based on your raw data filename"))
        self.label_9.setText(_translate("MainWindow", "System Name"))
        self.ratio_input.setText(_translate("MainWindow", "70:20:10"))
        self.label_2.setText(_translate("MainWindow", "Comments"))
        self.label_3.setText(_translate("MainWindow", "Anode Material"))
        self.label_4.setText(_translate("MainWindow", "Cell Type"))
        self.label_5.setText(_translate("MainWindow", "Cycling Rate"))
        self.type_input.setText(_translate("MainWindow", "Swagelok"))
        self.anode_input.setText(_translate("MainWindow", "Na Metal"))
        self.rate_comboBox.setItemText(0, _translate("MainWindow", "C/100"))
        self.rate_comboBox.setItemText(1, _translate("MainWindow", "C/50"))
        self.rate_comboBox.setItemText(2, _translate("MainWindow", "C/20"))
        self.rate_comboBox.setItemText(3, _translate("MainWindow", "C/10"))
        self.rate_comboBox.setItemText(4, _translate("MainWindow", "C/5"))
        self.rate_comboBox.setItemText(5, _translate("MainWindow", "C"))
        self.rate_comboBox.setItemText(6, _translate("MainWindow", "5C"))
        self.rate_comboBox.setItemText(7, _translate("MainWindow", "10C"))
        self.label_15.setToolTip(_translate("MainWindow", "The excel file that contains raw cycling data"))
        self.label_15.setText(_translate("MainWindow", "Raw Data"))
        self.raw_button.setText(_translate("MainWindow", "Choose File"))
        self.label_13.setToolTip(_translate("MainWindow", "The plot filename will be generated based of the system name"))
        self.label_13.setText(_translate("MainWindow", "Save Plot To"))
        self.plot_button.setText(_translate("MainWindow", "Choose Directory"))
        self.label_14.setToolTip(_translate("MainWindow", "The table filename will be generated based of the system name"))
        self.label_14.setText(_translate("MainWindow", "Save Table To"))
        self.table_button.setText(_translate("MainWindow", "Choose Directory"))
        self.run_button.setText(_translate("MainWindow", "Run"))
