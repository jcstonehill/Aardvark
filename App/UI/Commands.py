from App.UI.UI import UI

from configparser import ConfigParser
import os

from PyQt5 import QtWidgets, QtCore

from App.MeshReader.MeshReader import ReadMesh
import pyqtgraph.opengl as gl
from App.UI.ColorHelper import colorDict
import numpy as np
import datetime

class Commands:
  cwd: str
  ui: UI

  def __init__(self, cwd: str, ui: UI):
    self.cwd = cwd
    self.ui = ui

    self.ClearLog()
    self.AppendInfoToLog("Application successfully launched.")

    self.ReadAppConfig()

  def SaveAppConfig(self):
    config = ConfigParser()

    caseName = self.ui.caseName
    config["DEFAULT"]["lastCase"] = caseName

    filePath = self.cwd + "/App/config.ini"

    with open(filePath, "w") as file:
      config.write(file)

  def ApplyCaseConfig(self):
    config = ConfigParser()

    filePath = self.cwd + "/Cases/" + self.ui.caseName + "/config.ini"
    config.read(filePath)

    try:
      regionsColorIndexes = config.get("MeshUI", "regionsColorIndexes")
      regionsColorIndexes = [int(colorIndexString) for colorIndexString in regionsColorIndexes.split(", ")]
      boundariesColorIndexes = config.get("MeshUI", "boundariesColorIndexes")
      boundariesColorIndexes = [int(colorIndexString) for colorIndexString in boundariesColorIndexes.split(", ")]

      table = self.ui.meshUI.physicalVolumesTable
      for i in range(table.rowCount()):
        table.cellWidget(i,1).setCurrentIndex(regionsColorIndexes[i])
      table = self.ui.meshUI.physicalBoundariesTable
      for i in range(table.rowCount()):
        table.cellWidget(i,1).setCurrentIndex(boundariesColorIndexes[i])

      self.ui.neutronicsUI.nOfParticlesLabel.setText(config.get("NeutronicsUI", "nOfParticles"))
      self.ui.neutronicsUI.nOfActiveBatchesLabel.setText(config.get("NeutronicsUI", "nOfActiveBatches"))
      self.ui.neutronicsUI.criticalityCriteriaLabel.setText(config.get("NeutronicsUI", "criticalityConvergenceCriteria"))
      self.ui.neutronicsUI.shannonEntropyCriteriaLabel.setText(config.get("NeutronicsUI", "shannonEntropyConvergenceCriteria"))

      neutronicsBCs = config.get("NeutronicsUI", "neutronicsBCs")
      neutronicsBCs = [int(colorIndexString) for colorIndexString in neutronicsBCs.split(", ")]

      table = self.ui.neutronicsUI.BCTable
      for i in range(table.rowCount()):
        table.cellWidget(i,1).setCurrentIndex(neutronicsBCs[i])
    except:
      print("Error while reading case config.")

  def SaveCaseConfig(self):
    config = ConfigParser()
    
    regionsColorIndexes = ""
    table = self.ui.meshUI.physicalVolumesTable
    for i in range(table.rowCount()-1):
      regionsColorIndexes = regionsColorIndexes +  str(table.cellWidget(i,1).currentIndex()) + ", "
    regionsColorIndexes = regionsColorIndexes + str(table.cellWidget(table.rowCount()-1,1).currentIndex())

    boundariesColorIndexes = ""
    table = self.ui.meshUI.physicalBoundariesTable
    for i in range(table.rowCount()-1):
      boundariesColorIndexes = boundariesColorIndexes +  str(table.cellWidget(i,1).currentIndex()) + ", "
    boundariesColorIndexes = boundariesColorIndexes + str(table.cellWidget(table.rowCount()-1,1).currentIndex())

    config.add_section("MeshUI")
    config.set("MeshUI", "regionsColorIndexes", regionsColorIndexes)
    config.set("MeshUI", "boundariesColorIndexes", boundariesColorIndexes)
    
    nOfParticles = str(self.ui.neutronicsUI.nOfParticlesLabel.text())
    nOfActiveBatches = str(self.ui.neutronicsUI.nOfActiveBatchesLabel.text())
    criticalityConvergenceCriteria = str(self.ui.neutronicsUI.criticalityCriteriaLabel.text())
    shannonEntropyConvergenceCriteria = str(self.ui.neutronicsUI.shannonEntropyCriteriaLabel.text())

    neutronicsBCs = ""
    table = self.ui.neutronicsUI.BCTable
    for i in range(table.rowCount()-1):
      neutronicsBCs = neutronicsBCs +  str(table.cellWidget(i,1).currentIndex()) + ", "
    neutronicsBCs = neutronicsBCs + str(table.cellWidget(table.rowCount()-1,1).currentIndex())

    config.add_section("NeutronicsUI")
    config.set("NeutronicsUI", "nOfParticles", nOfParticles)
    config.set("NeutronicsUI", "nOfActiveBatches", nOfActiveBatches)
    config.set("NeutronicsUI", "criticalityConvergenceCriteria", criticalityConvergenceCriteria)
    config.set("NeutronicsUI", "shannonEntropyConvergenceCriteria", shannonEntropyConvergenceCriteria)
    config.set("NeutronicsUI", "neutronicsBCs", neutronicsBCs)

    
    filePath = self.cwd + "/Cases/" + self.ui.caseName + "/config.ini"

    with open(filePath, "w+") as file:
      config.write(file)

  def ClearLog(self):
    textBrowser = self.ui.logTextBrowser
    textBrowser.setPlainText("")

  def AppendInfoToLog(self, message: str):
    textBrowser = self.ui.logTextBrowser

    currentTime = datetime.datetime.now()
    currentTime = currentTime.strftime("%H.%M.%S")

    line = "App" + " : " + currentTime + " : " + "INFO" + " : " + message + "\n"

    textBrowser.insertPlainText(line)

  def AppendWarningToLog(self, message: str):
    textBrowser = self.ui.logTextBrowser

    currentTime = datetime.datetime.now()
    currentTime = currentTime.strftime("%H.%M.%S")

    line = "App" + " : " + currentTime + " : " + "WARNING" + " : " + message + "\n"

    textBrowser.insertPlainText(line)

  def AppendErrorToLog(self, message: str):
    textBrowser = self.ui.logTextBrowser

    currentTime = datetime.datetime.now()
    currentTime = currentTime.strftime("%H.%M.%S")

    line = "\nApp" + " : " + currentTime + " : " + "ERROR" + " : " + message + "\n\n"
    textBrowser.insertPlainText(line)

  def ReadAppConfig(self):
    cases = os.listdir(self.cwd + "/Cases/")
    
    config = ConfigParser()

    config.read(self.cwd + "/App/config.ini")
    
    try:
      lastCase = config["DEFAULT"]["lastCase"]

      if(lastCase in cases):
        self.LoadCase(self.cwd + "/Cases/" + lastCase)

    except KeyError:
      self.AppendErrorToLog("Error loading the case from the previous session.")
      lastCase = None

  def RebuildRegionsInTables(self):

    table = self.ui.meshUI.physicalVolumesTable
    for physicalVolume in self.ui.mesh.physicalVolumes:

      name = physicalVolume.name

      table.insertRow(table.rowCount())
      rowIndex = table.rowCount() - 1

      item = QtWidgets.QTableWidgetItem()
      item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      item.setText(str(name))
      table.setItem(rowIndex, 0, item)

      item = QtWidgets.QTableWidgetItem()
      item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      table.setItem(rowIndex, 1, item)
      widget = QtWidgets.QComboBox()
      widget.addItems(list(colorDict.keys()))
      table.setCellWidget(rowIndex, 1, widget)
      table.cellWidget(rowIndex, 1).currentTextChanged.connect(self.OnMeshTableColorChanged)

      item = QtWidgets.QTableWidgetItem()
      item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      table.setItem(rowIndex, 2, item)
      widget = QtWidgets.QCheckBox()
      widget.setChecked(True)
      widget.setStyleSheet("margin-left:45%; margin-right:55%;")
      widget.stateChanged.connect(self.OnMeshTableDisplayChanged)
      table.setCellWidget(rowIndex, 2, widget)

  def RebuildBoundariesInTables(self):
    table = self.ui.meshUI.physicalBoundariesTable
    for physicalBoundary in self.ui.mesh.physicalSurfaces:

      name = physicalBoundary.name

      table.insertRow(table.rowCount())
      rowIndex = table.rowCount() - 1

      item = QtWidgets.QTableWidgetItem()
      item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      item.setText(str(name))
      table.setItem(rowIndex, 0, item)

      item = QtWidgets.QTableWidgetItem()
      item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      table.setItem(rowIndex, 1, item)
      widget = QtWidgets.QComboBox()
      widget.addItems(list(colorDict.keys()))
      table.setCellWidget(rowIndex, 1, widget)
      table.cellWidget(rowIndex, 1).currentTextChanged.connect(self.OnMeshTableColorChanged)

      item = QtWidgets.QTableWidgetItem()
      item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      table.setItem(rowIndex, 2, item)
      widget = QtWidgets.QCheckBox()
      widget.setChecked(False)
      widget.setStyleSheet("margin-left:45%; margin-right:55%;")
      widget.stateChanged.connect(self.OnMeshTableDisplayChanged)
      table.setCellWidget(rowIndex, 2, widget)

    table = self.ui.neutronicsUI.BCTable
    for physicalBoundary in self.ui.mesh.physicalSurfaces:

      name = physicalBoundary.name

      table.insertRow(table.rowCount())
      rowIndex = table.rowCount() - 1

      item = QtWidgets.QTableWidgetItem()
      item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      item.setText(str(name))
      table.setItem(rowIndex, 0, item)

      item = QtWidgets.QTableWidgetItem()
      item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      table.setItem(rowIndex, 1, item)
      widget = QtWidgets.QComboBox()
      widget.addItems(self.ui.neutronicsBCs)
      table.setCellWidget(rowIndex, 1, widget)
      table.cellWidget(rowIndex, 1).currentTextChanged.connect(self.OnNeutronicsBCChanged)

  def OnNeutronicsBCChanged(self):
    self.SaveCaseConfig()

  def OnMeshTableColorChanged(self):
    self.SaveCaseConfig()
    self.UpdateMeshPlot()

  def OnMeshTableDisplayChanged(self):
    self.UpdateMeshPlot()

  def UpdateMeshPlot(self):
    plotWidget = self.ui.meshUI.graph
    plotWidget.clear()

    table = self.ui.meshUI.physicalBoundariesTable
    
    for i in range(table.rowCount()):

      if(table.cellWidget(i, 2).isChecked()):
        vertexes = []
        faces = []

        name = table.item(i,0).text()
        faceIndex = 0

        for elementSurface in self.ui.mesh.GetPhysicalSurface(name).elementSurfaces:
          faces.append([faceIndex, faceIndex+1, faceIndex+2])
          for node in elementSurface.nodes:
            vertexes.append([node.x, node.y, node.z])
            
            faceIndex = faceIndex + 1

        faces = np.array(faces)
        vertexes = np.array(vertexes) 

        meshData = gl.MeshData(vertexes=vertexes, faces=faces)
        
        plotItem = gl.GLMeshItem(meshdata=meshData, color=colorDict[table.cellWidget(i,1).currentText()], edgeColor = [0, 0, 0, 1], computeNormals=False, drawEdges=True)
        plotWidget.addItem(plotItem)


    table = self.ui.meshUI.physicalVolumesTable

    for i in range(table.rowCount()):

      if(table.cellWidget(i, 2).isChecked()):
        vertexes = []
        faces = []

        name = table.item(i,0).text()
        faceIndex = 0

        for element in self.ui.mesh.GetPhysicalVolume(name).elements:
          for elementSurface in element.elementSurfaces:
            faces.append([faceIndex, faceIndex+1, faceIndex+2])
            for node in elementSurface.nodes:
              vertexes.append([node.x, node.y, node.z])
              
              faceIndex = faceIndex + 1

        faces = np.array(faces)
        vertexes = np.array(vertexes) 

        meshData = gl.MeshData(vertexes=vertexes, faces=faces)
        
        plotItem = gl.GLMeshItem(meshdata=meshData, color=colorDict[table.cellWidget(i,1).currentText()], edgeColor = [0, 0, 0, 1], computeNormals=False, drawEdges=True)
        plotWidget.addItem(plotItem)
       
  def LoadCase(self, path: str):
    caseName = path.split("Cases/")[-1]

    self.ui.caseName = caseName
    meshFilePath = path + "/mesh.msh"

    if(not os.path.isfile(meshFilePath)):
      return
      
    newMesh = ReadMesh(meshFilePath)
    
    self.ui.mesh = newMesh
    self.ClearAllTables()
    self.RebuildRegionsInTables()
    self.RebuildBoundariesInTables()
    self.UpdateMeshPlot()
    self.ApplyCaseConfig()

    limits = [self.ui.mesh.xMax, self.ui.mesh.yMax, self.ui.mesh.zMax, self.ui.mesh.xMin, self.ui.mesh.yMin, self.ui.mesh.zMin]
    limits = [abs(limit) for limit in limits]

    newDistance = 3*1.5*max(limits)
    self.ui.meshUI.graph.setCameraPosition(distance=newDistance)
    self.AppendInfoToLog("New mesh has been created.")

    self.ui.loadedCaseLabel.setText(path)
    self.SaveAppConfig()
    self.AppendInfoToLog("Case successfully loaded from " + path + ".")

  def ClearAllTables(self):
    table = self.ui.meshUI.physicalVolumesTable

    while(table.rowCount() > 0):
      table.removeRow(table.rowCount()-1)

    table = self.ui.meshUI.physicalBoundariesTable

    while(table.rowCount() > 0):
      table.removeRow(table.rowCount()-1)

    table = self.ui.neutronicsUI.BCTable

    while(table.rowCount() > 0):
      table.removeRow(table.rowCount()-1)

  def ShowAllVolumes(self):
    table = self.ui.meshUI.physicalVolumesTable

    for i in range(table.rowCount()):
      checkBox = table.cellWidget(i, 2)
      checkBox.setChecked(True)

  def HideAllVolumes(self):
    table = self.ui.meshUI.physicalVolumesTable

    for i in range(table.rowCount()):
      checkBox = table.cellWidget(i, 2)
      checkBox.setChecked(False)

  def ShowAllBoundaries(self):
    table = self.ui.meshUI.physicalBoundariesTable

    for i in range(table.rowCount()):
      checkBox = table.cellWidget(i, 2)
      checkBox.setChecked(True)

  def HideAllBoundaries(self):
    table = self.ui.meshUI.physicalBoundariesTable

    for i in range(table.rowCount()):
      checkBox = table.cellWidget(i, 2)
      checkBox.setChecked(False)

  def HandleNeutronicsParameterButtons(self, button: QtWidgets.QPushButton, lineEdit: QtWidgets.QLineEdit, label: QtWidgets.QLabel):
    buttonText = button.text()
    
    if(buttonText == "Edit"):
      lineEdit.setText(label.text())
      button.setText("Save")
      
      label.setText("---")
      lineEdit.show()

    elif(buttonText == "Save"):
      label.setText(lineEdit.text())
      button.setText("Edit")

      lineEdit.hide()

      self.SaveCaseConfig()

class InputHandler:
  commands: Commands
  cwd: str
  ui: UI

  def __init__(self, cwd: str, ui: UI):
    self.cwd = cwd
    self.ui = ui

    self.commands = Commands(cwd, ui)

    self.Connect()

  def Connect(self):
    self.ui.loadCaseBrowseButton.clicked.connect(self.OnLoadCaseBrowseButtonPressed)
    self.ui.logClearButton.clicked.connect(self.OnClearButtonPressed)

    self.ui.meshUI.regionsDisplayAllButton.clicked.connect(self.OnRegionsDisplayAllButtonPressed)
    self.ui.meshUI.boundariesDisplayAllButton.clicked.connect(self.OnBoundariesDisplayAllButtonPressed)

    self.ui.neutronicsUI.nOfParticlesButton.clicked.connect(self.OnNOfParticlesButtonPressed)
    self.ui.neutronicsUI.nOfActiveBatchesButton.clicked.connect(self.OnNOfActiveBatchesButtonPressed)
    self.ui.neutronicsUI.criticalityCriteriaButton.clicked.connect(self.OnCriticalityCriteriaButtonPressed)
    self.ui.neutronicsUI.shannonEntropyCriteriaButton.clicked.connect(self.OnShannonEntropyButtonPressed)

  def OnClearButtonPressed(self):
    self.commands.ClearLog()

  def OnNOfParticlesButtonPressed(self):
    button = self.ui.neutronicsUI.nOfParticlesButton
    lineEdit = self.ui.neutronicsUI.nOfParticlesLineEdit
    label = self.ui.neutronicsUI.nOfParticlesLabel

    self.commands.HandleNeutronicsParameterButtons(button, lineEdit, label)

  def OnNOfActiveBatchesButtonPressed(self):
    button = self.ui.neutronicsUI.nOfActiveBatchesButton
    lineEdit = self.ui.neutronicsUI.nOfActiveBatchesLineEdit
    label = self.ui.neutronicsUI.nOfActiveBatchesLabel

    self.commands.HandleNeutronicsParameterButtons(button, lineEdit, label)

  def OnCriticalityCriteriaButtonPressed(self):
    button = self.ui.neutronicsUI.criticalityCriteriaButton
    lineEdit = self.ui.neutronicsUI.criticalityCriteriaLineEdit
    label = self.ui.neutronicsUI.criticalityCriteriaLabel

    self.commands.HandleNeutronicsParameterButtons(button, lineEdit, label)

  def OnShannonEntropyButtonPressed(self):
    button = self.ui.neutronicsUI.shannonEntropyCriteriaButton
    lineEdit = self.ui.neutronicsUI.shannonEntropyCriteriaLineEdit
    label = self.ui.neutronicsUI.shannonEntropyCriteriaLabel

    self.commands.HandleNeutronicsParameterButtons(button, lineEdit, label)

  def OnLoadCaseBrowseButtonPressed(self):

    dirName = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QWidget(), "Select a Directory", self.cwd + "/Cases/")

    if(dirName):
      self.commands.LoadCase(dirName)

  def OnRegionsDisplayAllButtonPressed(self):
    button = self.ui.meshUI.regionsDisplayAllButton
    currentButtonText = button.text()

    if(currentButtonText == "Show All"):
      self.commands.ShowAllVolumes()
      button.setText("Hide All")
    elif(currentButtonText == "Hide All"):
      self.commands.HideAllVolumes()
      button.setText("Show All")

    self.commands.UpdateMeshPlot(1)

  def OnBoundariesDisplayAllButtonPressed(self):

    button = self.ui.meshUI.boundariesDisplayAllButton
    currentButtonText = button.text()

    if(currentButtonText == "Show All"):
      self.commands.ShowAllBoundaries()
      button.setText("Hide All")
    elif(currentButtonText == "Hide All"):
      self.commands.HideAllBoundaries()
      button.setText("Show All")

    self.commands.UpdateMeshPlot(1)