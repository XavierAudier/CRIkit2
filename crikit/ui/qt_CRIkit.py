# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_CRIkit.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1691, 905)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("font: 8pt \"Arial\";")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabColors = QtWidgets.QTabWidget(self.centralwidget)
        self.tabColors.setEnabled(True)
        self.tabColors.setStyleSheet("")
        self.tabColors.setObjectName("tabColors")
        self.gridLayout_7.addWidget(self.tabColors, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabMain = QtWidgets.QTabWidget(self.centralwidget)
        self.tabMain.setObjectName("tabMain")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sweeperVL = QtWidgets.QVBoxLayout()
        self.sweeperVL.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.sweeperVL.setContentsMargins(-1, 10, -1, 0)
        self.sweeperVL.setSpacing(0)
        self.sweeperVL.setObjectName("sweeperVL")
        self.gridLayout_3.addLayout(self.sweeperVL, 0, 0, 1, 1)
        self.tabMain.addTab(self.tab, "")
        self.tabCompositeLarge = QtWidgets.QWidget()
        self.tabCompositeLarge.setObjectName("tabCompositeLarge")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabCompositeLarge)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sweeperVL_2 = QtWidgets.QVBoxLayout()
        self.sweeperVL_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.sweeperVL_2.setContentsMargins(-1, 10, -1, 0)
        self.sweeperVL_2.setSpacing(0)
        self.sweeperVL_2.setObjectName("sweeperVL_2")
        self.gridLayout_4.addLayout(self.sweeperVL_2, 0, 0, 1, 1)
        self.tabMain.addTab(self.tabCompositeLarge, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabSettings)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.tabMain.addTab(self.tabSettings, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabMain.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabMain)
        self.freqSlider = QtWidgets.QScrollBar(self.centralwidget)
        self.freqSlider.setMinimumSize(QtCore.QSize(400, 30))
        self.freqSlider.setProperty("value", 10)
        self.freqSlider.setOrientation(QtCore.Qt.Horizontal)
        self.freqSlider.setObjectName("freqSlider")
        self.verticalLayout_3.addWidget(self.freqSlider)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditPix = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPix.sizePolicy().hasHeightForWidth())
        self.lineEditPix.setSizePolicy(sizePolicy)
        self.lineEditPix.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEditPix.setMaximumSize(QtCore.QSize(100, 200))
        self.lineEditPix.setStyleSheet("font: 14pt \"Arial\";")
        self.lineEditPix.setObjectName("lineEditPix")
        self.verticalLayout.addWidget(self.lineEditPix, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.labelFreqPixel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFreqPixel.sizePolicy().hasHeightForWidth())
        self.labelFreqPixel.setSizePolicy(sizePolicy)
        self.labelFreqPixel.setMinimumSize(QtCore.QSize(10, 30))
        self.labelFreqPixel.setMaximumSize(QtCore.QSize(100, 20))
        self.labelFreqPixel.setTextFormat(QtCore.Qt.AutoText)
        self.labelFreqPixel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFreqPixel.setObjectName("labelFreqPixel")
        self.verticalLayout.addWidget(self.labelFreqPixel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditFreq = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFreq.sizePolicy().hasHeightForWidth())
        self.lineEditFreq.setSizePolicy(sizePolicy)
        self.lineEditFreq.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEditFreq.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEditFreq.setFont(font)
        self.lineEditFreq.setStyleSheet("font: 14pt \"Arial\";")
        self.lineEditFreq.setObjectName("lineEditFreq")
        self.verticalLayout_2.addWidget(self.lineEditFreq, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.labelWavenumber = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelWavenumber.sizePolicy().hasHeightForWidth())
        self.labelWavenumber.setSizePolicy(sizePolicy)
        self.labelWavenumber.setMinimumSize(QtCore.QSize(120, 20))
        self.labelWavenumber.setMaximumSize(QtCore.QSize(1000, 20))
        self.labelWavenumber.setTextFormat(QtCore.Qt.AutoText)
        self.labelWavenumber.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWavenumber.setObjectName("labelWavenumber")
        self.verticalLayout_2.addWidget(self.labelWavenumber, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1691, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        self.menuPiece_wise_NRB = QtWidgets.QMenu(self.menuImport)
        self.menuPiece_wise_NRB.setEnabled(False)
        self.menuPiece_wise_NRB.setObjectName("menuPiece_wise_NRB")
        self.menuPre_Process = QtWidgets.QMenu(self.menubar)
        self.menuPre_Process.setObjectName("menuPre_Process")
        self.menuVariance_Stabilize = QtWidgets.QMenu(self.menuPre_Process)
        self.menuVariance_Stabilize.setEnabled(True)
        self.menuVariance_Stabilize.setObjectName("menuVariance_Stabilize")
        self.menuCoherent_Raman_Imaging = QtWidgets.QMenu(self.menuPre_Process)
        self.menuCoherent_Raman_Imaging.setObjectName("menuCoherent_Raman_Imaging")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuToolbar = QtWidgets.QMenu(self.menuView)
        self.menuToolbar.setObjectName("menuToolbar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toolBar.setFont(font)
        self.toolBar.setIconSize(QtCore.QSize(20, 20))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpenHDFNIST = QtWidgets.QAction(MainWindow)
        self.actionOpenHDFNIST.setChecked(False)
        self.actionOpenHDFNIST.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/envelope-open-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenHDFNIST.setIcon(icon)
        self.actionOpenHDFNIST.setObjectName("actionOpenHDFNIST")
        self.actionLoadDark = QtWidgets.QAction(MainWindow)
        self.actionLoadDark.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/account-login-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadDark.setIcon(icon1)
        self.actionLoadDark.setObjectName("actionLoadDark")
        self.actionLoadNRB = QtWidgets.QAction(MainWindow)
        self.actionLoadNRB.setEnabled(False)
        self.actionLoadNRB.setIcon(icon1)
        self.actionLoadNRB.setObjectName("actionLoadNRB")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/envelope-closed-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/cog-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon3)
        self.actionSettings.setObjectName("actionSettings")
        self.actionDarkSubtract = QtWidgets.QAction(MainWindow)
        self.actionDarkSubtract.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/arrow-thick-bottom-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDarkSubtract.setIcon(icon4)
        self.actionDarkSubtract.setObjectName("actionDarkSubtract")
        self.actionKramersKronig = QtWidgets.QAction(MainWindow)
        self.actionKramersKronig.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/audio-spectrum-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionKramersKronig.setIcon(icon5)
        self.actionKramersKronig.setObjectName("actionKramersKronig")
        self.actionPhaseErrorCorrection = QtWidgets.QAction(MainWindow)
        self.actionPhaseErrorCorrection.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/bug-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPhaseErrorCorrection.setIcon(icon6)
        self.actionPhaseErrorCorrection.setObjectName("actionPhaseErrorCorrection")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/action-undo-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon7)
        self.actionUndo.setObjectName("actionUndo")
        self.actionDeNoise = QtWidgets.QAction(MainWindow)
        self.actionDeNoise.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/dial-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeNoise.setIcon(icon8)
        self.actionDeNoise.setObjectName("actionDeNoise")
        self.actionAnalysisToolkit = QtWidgets.QAction(MainWindow)
        self.actionAnalysisToolkit.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/bar-chart-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnalysisToolkit.setIcon(icon9)
        self.actionAnalysisToolkit.setObjectName("actionAnalysisToolkit")
        self.actionZeroFirstColumn = QtWidgets.QAction(MainWindow)
        self.actionZeroFirstColumn.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/crop-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZeroFirstColumn.setIcon(icon10)
        self.actionZeroFirstColumn.setObjectName("actionZeroFirstColumn")
        self.actionPointSpectrum = QtWidgets.QAction(MainWindow)
        self.actionPointSpectrum.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/map-marker-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPointSpectrum.setIcon(icon11)
        self.actionPointSpectrum.setObjectName("actionPointSpectrum")
        self.actionROISpectrum = QtWidgets.QAction(MainWindow)
        self.actionROISpectrum.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/map-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionROISpectrum.setIcon(icon12)
        self.actionROISpectrum.setObjectName("actionROISpectrum")
        self.actionDarkSpectrum = QtWidgets.QAction(MainWindow)
        self.actionDarkSpectrum.setEnabled(False)
        self.actionDarkSpectrum.setObjectName("actionDarkSpectrum")
        self.actionNRBSpectrum = QtWidgets.QAction(MainWindow)
        self.actionNRBSpectrum.setEnabled(False)
        self.actionNRBSpectrum.setObjectName("actionNRBSpectrum")
        self.actionFreqWindow = QtWidgets.QAction(MainWindow)
        self.actionFreqWindow.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/resize-width-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFreqWindow.setIcon(icon13)
        self.actionFreqWindow.setObjectName("actionFreqWindow")
        self.actionCalibrate = QtWidgets.QAction(MainWindow)
        self.actionCalibrate.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/check-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionCalibrate.setIcon(icon14)
        self.actionCalibrate.setObjectName("actionCalibrate")
        self.actionNRB_from_ROI = QtWidgets.QAction(MainWindow)
        self.actionNRB_from_ROI.setEnabled(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/globe-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNRB_from_ROI.setIcon(icon15)
        self.actionNRB_from_ROI.setObjectName("actionNRB_from_ROI")
        self.actionAppend_NRB_from_ROI = QtWidgets.QAction(MainWindow)
        self.actionAppend_NRB_from_ROI.setEnabled(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/paperclip-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAppend_NRB_from_ROI.setIcon(icon16)
        self.actionAppend_NRB_from_ROI.setObjectName("actionAppend_NRB_from_ROI")
        self.actionSubtractROI = QtWidgets.QAction(MainWindow)
        self.actionSubtractROI.setEnabled(False)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/collapse-down-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSubtractROI.setIcon(icon17)
        self.actionSubtractROI.setObjectName("actionSubtractROI")
        self.actionShowPlotter = QtWidgets.QAction(MainWindow)
        self.actionShowPlotter.setObjectName("actionShowPlotter")
        self.actionKKSpeedTest = QtWidgets.QAction(MainWindow)
        self.actionKKSpeedTest.setEnabled(False)
        self.actionKKSpeedTest.setObjectName("actionKKSpeedTest")
        self.actionSimpleOutlierRemoval = QtWidgets.QAction(MainWindow)
        self.actionSimpleOutlierRemoval.setEnabled(False)
        self.actionSimpleOutlierRemoval.setObjectName("actionSimpleOutlierRemoval")
        self.actionResetCalibration = QtWidgets.QAction(MainWindow)
        self.actionResetCalibration.setEnabled(False)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/x-2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionResetCalibration.setIcon(icon18)
        self.actionResetCalibration.setObjectName("actionResetCalibration")
        self.actionZeroFirstRow = QtWidgets.QAction(MainWindow)
        self.actionZeroFirstRow.setEnabled(False)
        self.actionZeroFirstRow.setIcon(icon10)
        self.actionZeroFirstRow.setObjectName("actionZeroFirstRow")
        self.actionZeroLastColumn = QtWidgets.QAction(MainWindow)
        self.actionZeroLastColumn.setEnabled(False)
        self.actionZeroLastColumn.setIcon(icon10)
        self.actionZeroLastColumn.setObjectName("actionZeroLastColumn")
        self.actionZeroLastRow = QtWidgets.QAction(MainWindow)
        self.actionZeroLastRow.setEnabled(False)
        self.actionZeroLastRow.setIcon(icon10)
        self.actionZeroLastRow.setObjectName("actionZeroLastRow")
        self.actionAnscombe = QtWidgets.QAction(MainWindow)
        self.actionAnscombe.setEnabled(False)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/vertical-align-center-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnscombe.setIcon(icon19)
        self.actionAnscombe.setObjectName("actionAnscombe")
        self.actionInverseAnscombe = QtWidgets.QAction(MainWindow)
        self.actionInverseAnscombe.setEnabled(False)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/vertical-align-bottom-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInverseAnscombe.setIcon(icon20)
        self.actionInverseAnscombe.setObjectName("actionInverseAnscombe")
        self.actionScaleErrorCorrection = QtWidgets.QAction(MainWindow)
        self.actionScaleErrorCorrection.setEnabled(False)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/bug-3x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScaleErrorCorrection.setIcon(icon21)
        self.actionScaleErrorCorrection.setObjectName("actionScaleErrorCorrection")
        self.actionResidualSubtract = QtWidgets.QAction(MainWindow)
        self.actionResidualSubtract.setEnabled(False)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/data-transfer-download-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionResidualSubtract.setIcon(icon22)
        self.actionResidualSubtract.setObjectName("actionResidualSubtract")
        self.actionAmpErrorCorrection = QtWidgets.QAction(MainWindow)
        self.actionAmpErrorCorrection.setEnabled(False)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/graph-3x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAmpErrorCorrection.setIcon(icon23)
        self.actionAmpErrorCorrection.setObjectName("actionAmpErrorCorrection")
        self.actionToolBarNIST2 = QtWidgets.QAction(MainWindow)
        self.actionToolBarNIST2.setCheckable(True)
        self.actionToolBarNIST2.setChecked(False)
        self.actionToolBarNIST2.setObjectName("actionToolBarNIST2")
        self.actionToolBarNone = QtWidgets.QAction(MainWindow)
        self.actionToolBarNone.setCheckable(True)
        self.actionToolBarNone.setObjectName("actionToolBarNone")
        self.actionOpenDLMNIST = QtWidgets.QAction(MainWindow)
        self.actionOpenDLMNIST.setIcon(icon)
        self.actionOpenDLMNIST.setObjectName("actionOpenDLMNIST")
        self.actionLoadDarkDLM = QtWidgets.QAction(MainWindow)
        self.actionLoadDarkDLM.setEnabled(False)
        self.actionLoadDarkDLM.setIcon(icon1)
        self.actionLoadDarkDLM.setObjectName("actionLoadDarkDLM")
        self.actionLoadNRBDLM = QtWidgets.QAction(MainWindow)
        self.actionLoadNRBDLM.setEnabled(False)
        self.actionLoadNRBDLM.setIcon(icon1)
        self.actionLoadNRBDLM.setObjectName("actionLoadNRBDLM")
        self.actionToolBarNIST1 = QtWidgets.QAction(MainWindow)
        self.actionToolBarNIST1.setCheckable(True)
        self.actionToolBarNIST1.setChecked(False)
        self.actionToolBarNIST1.setObjectName("actionToolBarNIST1")
        self.actionUndo_Backup_Enabled = QtWidgets.QAction(MainWindow)
        self.actionUndo_Backup_Enabled.setCheckable(True)
        self.actionUndo_Backup_Enabled.setChecked(True)
        self.actionUndo_Backup_Enabled.setObjectName("actionUndo_Backup_Enabled")
        self.actionLoad_NRB_Left_Side = QtWidgets.QAction(MainWindow)
        self.actionLoad_NRB_Left_Side.setObjectName("actionLoad_NRB_Left_Side")
        self.actionLoad_NRB_Right_Side = QtWidgets.QAction(MainWindow)
        self.actionLoad_NRB_Right_Side.setObjectName("actionLoad_NRB_Right_Side")
        self.actionNRB_from_ROI_Left_Side = QtWidgets.QAction(MainWindow)
        self.actionNRB_from_ROI_Left_Side.setObjectName("actionNRB_from_ROI_Left_Side")
        self.actionNRB_from_ROI_Right_Side = QtWidgets.QAction(MainWindow)
        self.actionNRB_from_ROI_Right_Side.setObjectName("actionNRB_from_ROI_Right_Side")
        self.actionMergeNRBs = QtWidgets.QAction(MainWindow)
        self.actionMergeNRBs.setEnabled(False)
        self.actionMergeNRBs.setObjectName("actionMergeNRBs")
        self.actionMerge_NRBs_KK_Preview = QtWidgets.QAction(MainWindow)
        self.actionMerge_NRBs_KK_Preview.setObjectName("actionMerge_NRBs_KK_Preview")
        self.actionLeftSideNRBSpect = QtWidgets.QAction(MainWindow)
        self.actionLeftSideNRBSpect.setEnabled(False)
        self.actionLeftSideNRBSpect.setObjectName("actionLeftSideNRBSpect")
        self.actionRightSideNRBSpect = QtWidgets.QAction(MainWindow)
        self.actionRightSideNRBSpect.setEnabled(False)
        self.actionRightSideNRBSpect.setObjectName("actionRightSideNRBSpect")
        self.actionDeNoiseNRB = QtWidgets.QAction(MainWindow)
        self.actionDeNoiseNRB.setObjectName("actionDeNoiseNRB")
        self.actionDeNoiseDark = QtWidgets.QAction(MainWindow)
        self.actionDeNoiseDark.setObjectName("actionDeNoiseDark")
        self.menuFile.addAction(self.actionOpenHDFNIST)
        self.menuFile.addAction(self.actionOpenDLMNIST)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuPiece_wise_NRB.addAction(self.actionMergeNRBs)
        self.menuPiece_wise_NRB.addSeparator()
        self.menuPiece_wise_NRB.addAction(self.actionLoad_NRB_Left_Side)
        self.menuPiece_wise_NRB.addAction(self.actionNRB_from_ROI_Left_Side)
        self.menuPiece_wise_NRB.addSeparator()
        self.menuPiece_wise_NRB.addAction(self.actionLoad_NRB_Right_Side)
        self.menuPiece_wise_NRB.addAction(self.actionNRB_from_ROI_Right_Side)
        self.menuImport.addAction(self.actionLoadDark)
        self.menuImport.addAction(self.actionLoadNRB)
        self.menuImport.addSeparator()
        self.menuImport.addAction(self.actionLoadDarkDLM)
        self.menuImport.addAction(self.actionLoadNRBDLM)
        self.menuImport.addSeparator()
        self.menuImport.addAction(self.actionNRB_from_ROI)
        self.menuImport.addAction(self.actionAppend_NRB_from_ROI)
        self.menuImport.addSeparator()
        self.menuImport.addAction(self.menuPiece_wise_NRB.menuAction())
        self.menuVariance_Stabilize.addAction(self.actionAnscombe)
        self.menuVariance_Stabilize.addSeparator()
        self.menuVariance_Stabilize.addAction(self.actionInverseAnscombe)
        self.menuCoherent_Raman_Imaging.addAction(self.actionDeNoiseNRB)
        self.menuCoherent_Raman_Imaging.addAction(self.actionKramersKronig)
        self.menuCoherent_Raman_Imaging.addAction(self.actionKKSpeedTest)
        self.menuCoherent_Raman_Imaging.addAction(self.actionPhaseErrorCorrection)
        self.menuCoherent_Raman_Imaging.addAction(self.actionScaleErrorCorrection)
        self.menuPre_Process.addAction(self.actionDeNoiseDark)
        self.menuPre_Process.addAction(self.actionDarkSubtract)
        self.menuPre_Process.addAction(self.actionResidualSubtract)
        self.menuPre_Process.addAction(self.menuVariance_Stabilize.menuAction())
        self.menuPre_Process.addAction(self.actionDeNoise)
        self.menuPre_Process.addAction(self.actionAmpErrorCorrection)
        self.menuPre_Process.addSeparator()
        self.menuPre_Process.addAction(self.actionSimpleOutlierRemoval)
        self.menuPre_Process.addSeparator()
        self.menuPre_Process.addAction(self.actionSubtractROI)
        self.menuPre_Process.addSeparator()
        self.menuPre_Process.addSeparator()
        self.menuPre_Process.addAction(self.menuCoherent_Raman_Imaging.menuAction())
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionZeroFirstColumn)
        self.menuEdit.addAction(self.actionZeroFirstRow)
        self.menuEdit.addAction(self.actionZeroLastColumn)
        self.menuEdit.addAction(self.actionZeroLastRow)
        self.menuEdit.addAction(self.actionFreqWindow)
        self.menuEdit.addAction(self.actionCalibrate)
        self.menuEdit.addAction(self.actionResetCalibration)
        self.menuAnalysis.addAction(self.actionAnalysisToolkit)
        self.menuToolbar.addAction(self.actionToolBarNone)
        self.menuToolbar.addAction(self.actionToolBarNIST2)
        self.menuToolbar.addAction(self.actionToolBarNIST1)
        self.menuView.addAction(self.menuToolbar.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShowPlotter)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionPointSpectrum)
        self.menuView.addAction(self.actionROISpectrum)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionDarkSpectrum)
        self.menuView.addAction(self.actionNRBSpectrum)
        self.menuView.addAction(self.actionLeftSideNRBSpect)
        self.menuView.addAction(self.actionRightSideNRBSpect)
        self.menuSettings.addAction(self.actionUndo_Backup_Enabled)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuPre_Process.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabColors.setCurrentIndex(-1)
        self.tabMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRIkit2"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab), _translate("MainWindow", "Single Frequency"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabCompositeLarge), _translate("MainWindow", "Composite"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabSettings), _translate("MainWindow", "Settings"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "This is where you enter notes....\n"
"\n"
"This will be saved to the processed file."))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_3), _translate("MainWindow", "Notes"))
        self.labelFreqPixel.setText(_translate("MainWindow", "Freq Pixel"))
        self.labelWavenumber.setText(_translate("MainWindow", "Wavenumber (cm-1)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuImport.setTitle(_translate("MainWindow", "Import/Load"))
        self.menuPiece_wise_NRB.setTitle(_translate("MainWindow", "Piece-wise NRB"))
        self.menuPre_Process.setTitle(_translate("MainWindow", "Pre-Process"))
        self.menuVariance_Stabilize.setTitle(_translate("MainWindow", "Standardize"))
        self.menuCoherent_Raman_Imaging.setTitle(_translate("MainWindow", "Coherent Raman Imaging"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuToolbar.setTitle(_translate("MainWindow", "Toolbar"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpenHDFNIST.setText(_translate("MainWindow", "Open HDF (NIST)..."))
        self.actionOpenHDFNIST.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionLoadDark.setText(_translate("MainWindow", "Load Dark (HDF)"))
        self.actionLoadNRB.setText(_translate("MainWindow", "Load NRB (HDF)"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSettings.setText(_translate("MainWindow", "Settings..."))
        self.actionDarkSubtract.setText(_translate("MainWindow", "Dark Sub..."))
        self.actionDarkSubtract.setToolTip(_translate("MainWindow", "Dark Subtraction"))
        self.actionKramersKronig.setText(_translate("MainWindow", "KK"))
        self.actionKramersKronig.setToolTip(_translate("MainWindow", "Kramers-Kronig Relation"))
        self.actionPhaseErrorCorrection.setText(_translate("MainWindow", "Phase Err..."))
        self.actionPhaseErrorCorrection.setToolTip(_translate("MainWindow", "Phase Error Correction"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionDeNoise.setText(_translate("MainWindow", "De-Noise"))
        self.actionAnalysisToolkit.setText(_translate("MainWindow", "Analysis Toolkit"))
        self.actionZeroFirstColumn.setText(_translate("MainWindow", "Zero 1st Column"))
        self.actionPointSpectrum.setText(_translate("MainWindow", "Pt Spect"))
        self.actionPointSpectrum.setToolTip(_translate("MainWindow", "Single Point Spectrum"))
        self.actionROISpectrum.setText(_translate("MainWindow", "ROI Spect"))
        self.actionROISpectrum.setToolTip(_translate("MainWindow", "ROI Spectrum"))
        self.actionDarkSpectrum.setText(_translate("MainWindow", "Dark Spect"))
        self.actionDarkSpectrum.setToolTip(_translate("MainWindow", "Dark Spectrum"))
        self.actionNRBSpectrum.setText(_translate("MainWindow", "NRB Spect"))
        self.actionNRBSpectrum.setToolTip(_translate("MainWindow", "NRB Spectrum"))
        self.actionFreqWindow.setText(_translate("MainWindow", "Freq Window"))
        self.actionFreqWindow.setToolTip(_translate("MainWindow", "Set Frequency Window"))
        self.actionCalibrate.setText(_translate("MainWindow", "Calibrate"))
        self.actionNRB_from_ROI.setText(_translate("MainWindow", "NRB from ROI"))
        self.actionAppend_NRB_from_ROI.setText(_translate("MainWindow", "Append NRB from ROI"))
        self.actionSubtractROI.setText(_translate("MainWindow", "Sub ROI"))
        self.actionSubtractROI.setToolTip(_translate("MainWindow", "Subtract ROI Spectrum"))
        self.actionShowPlotter.setText(_translate("MainWindow", "Show Plotter"))
        self.actionKKSpeedTest.setText(_translate("MainWindow", "Kramers-Kronig Speed Test"))
        self.actionSimpleOutlierRemoval.setText(_translate("MainWindow", "Simple Outlier Removal"))
        self.actionResetCalibration.setText(_translate("MainWindow", "Reset Calibration"))
        self.actionZeroFirstRow.setText(_translate("MainWindow", "Zero 1st Row"))
        self.actionZeroLastColumn.setText(_translate("MainWindow", "Zero Last Column"))
        self.actionZeroLastRow.setText(_translate("MainWindow", "Zero Last Row"))
        self.actionAnscombe.setText(_translate("MainWindow", "Anscombe"))
        self.actionInverseAnscombe.setText(_translate("MainWindow", "Inv Anscombe"))
        self.actionInverseAnscombe.setToolTip(_translate("MainWindow", "Inverse Anscombe"))
        self.actionScaleErrorCorrection.setText(_translate("MainWindow", "Scale Err..."))
        self.actionScaleErrorCorrection.setToolTip(_translate("MainWindow", "Scale Error Correction"))
        self.actionResidualSubtract.setText(_translate("MainWindow", "Residual Sub"))
        self.actionResidualSubtract.setToolTip(_translate("MainWindow", "Residual Background Subtraction"))
        self.actionAmpErrorCorrection.setText(_translate("MainWindow", "Baseline Sub"))
        self.actionAmpErrorCorrection.setToolTip(_translate("MainWindow", "Baseline Detrending"))
        self.actionToolBarNIST2.setText(_translate("MainWindow", "NIST CRI Workflow"))
        self.actionToolBarNone.setText(_translate("MainWindow", "None"))
        self.actionOpenDLMNIST.setText(_translate("MainWindow", "Open DLM (NIST)"))
        self.actionOpenDLMNIST.setToolTip(_translate("MainWindow", "Open Deliminated File (NIST)"))
        self.actionLoadDarkDLM.setText(_translate("MainWindow", "Load Dark (DLM)"))
        self.actionLoadDarkDLM.setToolTip(_translate("MainWindow", "Load Dark (DLM)"))
        self.actionLoadNRBDLM.setText(_translate("MainWindow", "Load NRB (DLM)"))
        self.actionLoadNRBDLM.setToolTip(_translate("MainWindow", "Load NRB (DLM)"))
        self.actionToolBarNIST1.setText(_translate("MainWindow", "NIST CRI Workflow (BCARS1)"))
        self.actionUndo_Backup_Enabled.setText(_translate("MainWindow", "Undo/Backup Enabled"))
        self.actionLoad_NRB_Left_Side.setText(_translate("MainWindow", "Load NRB (HDF; Left-Side)"))
        self.actionLoad_NRB_Right_Side.setText(_translate("MainWindow", "Load NRB (HDF; Right-Side)"))
        self.actionNRB_from_ROI_Left_Side.setText(_translate("MainWindow", "NRB from ROI (Left-Side)"))
        self.actionNRB_from_ROI_Right_Side.setText(_translate("MainWindow", "NRB from ROI (Right-Side)"))
        self.actionMergeNRBs.setText(_translate("MainWindow", "Merge NRBs"))
        self.actionMerge_NRBs_KK_Preview.setText(_translate("MainWindow", "Merge NRBs (KK Preview)"))
        self.actionLeftSideNRBSpect.setText(_translate("MainWindow", "Left-Side NRB Spect"))
        self.actionRightSideNRBSpect.setText(_translate("MainWindow", "Right-Side NRB Spec"))
        self.actionDeNoiseNRB.setText(_translate("MainWindow", "De-Noise NRB"))
        self.actionDeNoiseDark.setText(_translate("MainWindow", "De-Noise Dark"))

from . import icons_all_rc
