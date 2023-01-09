from App.UI.qtUI import Ui_MainWindow
from App.MeshReader.Mesh import Mesh

from PyQt5 import QtWidgets
from dataclasses import dataclass
import pyqtgraph.opengl as gl

@dataclass
class MeshUI:
  physicalVolumesTable: QtWidgets.QTableWidget
  physicalBoundariesTable: QtWidgets.QTableWidget
  regionsDisplayAllButton: QtWidgets.QPushButton
  boundariesDisplayAllButton: QtWidgets.QPushButton
  graph: gl.GLViewWidget

@dataclass
class NeutronicsUI:
  nOfParticlesLabel: QtWidgets.QLabel
  nOfParticlesLineEdit: QtWidgets.QLineEdit
  nOfParticlesButton: QtWidgets.QPushButton
  nOfActiveBatchesLabel: QtWidgets.QLabel
  nOfActiveBatchesLineEdit: QtWidgets.QLineEdit
  nOfActiveBatchesButton: QtWidgets.QPushButton
  criticalityCriteriaLabel: QtWidgets.QLabel
  criticalityCriteriaLineEdit: QtWidgets.QLineEdit
  criticalityCriteriaButton: QtWidgets.QPushButton
  shannonEntropyCriteriaLabel: QtWidgets.QLabel
  shannonEntropyCriteriaLineEdit: QtWidgets.QLineEdit
  shannonEntropyCriteriaButton: QtWidgets.QPushButton
  BCTable: QtWidgets.QTableWidget

@dataclass
class SolverUI:
  nOfProccesesSpinBox: QtWidgets.QSpinBox
  checkButton: QtWidgets.QPushButton
  runButton: QtWidgets.QPushButton

class UI:
  caseName: str
  qt: Ui_MainWindow

  mainWindow: QtWidgets.QMainWindow
  loadedCaseLabel: QtWidgets.QLabel
  loadCaseBrowseButton: QtWidgets.QPushButton

  logClearButton: QtWidgets.QPushButton
  logTextBrowser: QtWidgets.QTextBrowser

  mesh: Mesh

  neutronicsBCs: list[str] = ["Void", "Transport To Neighbor", "Reflective"]

  def __init__(self, qt: Ui_MainWindow, mainWindow: QtWidgets.QMainWindow):
    self.qt = qt
    self.mainWindow = mainWindow
    self.loadedCaseLabel = self.qt.loadedCaseLabel
    self.loadCaseBrowseButton = self.qt.loadCaseBrowseButton
    
    self.logClearButton = self.qt.logClearButton
    self.logTextBrowser = self.qt.logTextBrowser

    self.meshUI = MeshUI(qt.meshPhysicalVolumesTable, qt.meshPhysicalBoundariesTable, qt.meshRegionsDisplayAllButton, qt.meshBoundarioesDisplayAllButton, qt.meshGraph)
    self.neutronicsUI = NeutronicsUI(qt.neutronicsNOfParticlesLabel, qt.neutronicsNOfParticlesLineEdit, qt.neutronicsNOfParticlesButton, qt.neutronicsNOfActiveBatchesLabel, qt.neutronicsNOfActiveBatchesLineEdit, qt.neutronicsNOfActiveBatchesButton, qt.neutronicsCriticalityConvergenceLabel, qt.neutronicsCriticalityConvergenceLineEdit, qt.neutronicsCriticalityConvergenceButton, qt.neutronicsShannonConvergenceCriteriaLabel, qt.neutronicsShannonConvergenceCriteriaLineEdit, qt.neutronicsShannonConvergenceCriteriaButton, qt.neutronicsBCTable)
    self.solverUI = SolverUI(qt.solverNOfProcessesSpinBox, qt.solverCheckButton, qt.solverRunButton)

    self.meshUI.physicalVolumesTable.setStyleSheet("QHeaderView::section { background-color:#cccccc }")
    self.meshUI.physicalBoundariesTable.setStyleSheet("QHeaderView::section { background-color:#cccccc }")
    self.neutronicsUI.BCTable.setStyleSheet("QHeaderView::section { background-color:#cccccc }")

    self.neutronicsUI.nOfParticlesLineEdit.hide()
    self.neutronicsUI.nOfActiveBatchesLineEdit.hide()
    self.neutronicsUI.criticalityCriteriaLineEdit.hide()
    self.neutronicsUI.shannonEntropyCriteriaLineEdit.hide()
  
  def SetMeshObject(self, mesh: Mesh):
    self.mesh = mesh