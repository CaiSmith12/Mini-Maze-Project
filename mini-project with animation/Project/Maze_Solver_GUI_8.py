from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage 

from PIL import Image
import cv2
import numpy as np
import csv
import os
import csv
from time import sleep,monotonic
from random import choice



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 850)
        MainWindow.setStyleSheet("*{\n"
"    background:#DDEEFF;\n"
"    border:1px solid;    \n"
"    font-family: Arial, Helvetica, sans-serif;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    background-color: #7AA3CC;\n"
"    \n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    background-color: #99CCFF;\n"
"    color: rgb(0, 0, 0);\n"
"    color:black;\n"
"    font: bold italic 10pt;\n"
"    border: 1px solid;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    background-color: #7AA3CC;\n"
"    border: 1px solid;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:white;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    background: white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    font-family: Arial, Helvetica, sans-serif;\n"
"    font-size: 10pt;\n"
"    background: rgba(170, 255, 255, 0.1)\n"
"}\n"
"QSpinBox,QDoubleSpinBox,QCheckBox{\n"
"    border: 1px solid gray;\n"
"    background: white;\n"
"    border-radius: 5px;\n"
"    background: rgba(170, 255, 255, 0.1)\n"
"}\n"
"QLineEdit,QPlainTextEdit,QTableWidget{\n"
"    border: 1px solid gray;\n"
"    background: white;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    font-family: Courier New;\n"
"    font-size:10pt;\n"
"\n"
"}\n"
"QGroupBox{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                   stop: 0 rgba(0, 85, 255,0.1), stop: 1 rgba(170, 255, 255,0.1));\n"
"    border: 1px solid rgba(0, 0, 255,0.5);\n"
"\n"
"\n"
"    border-radius: 20px;\n"
"    margin-top: 1ex; \n"
"    font: bold 16pt;\n"
"    color: black;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.CB_CSVs = QtWidgets.QComboBox(self.groupBox)
        self.CB_CSVs.setObjectName("CB_CSVs")
        self.verticalLayout.addWidget(self.CB_CSVs)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Time = QtWidgets.QLabel(self.groupBox)
        self.label_Time.setMinimumSize(QtCore.QSize(120, 0))
        self.label_Time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Time.setObjectName("label_Time")
        self.horizontalLayout.addWidget(self.label_Time)
        self.SB_TimeLimit = QtWidgets.QSpinBox(self.groupBox)
        self.SB_TimeLimit.setSuffix("")
        self.SB_TimeLimit.setMaximum(999999)
        self.SB_TimeLimit.setSingleStep(1)
        self.SB_TimeLimit.setProperty("value", 60)
        self.SB_TimeLimit.setObjectName("SB_TimeLimit")
        self.horizontalLayout.addWidget(self.SB_TimeLimit)
        self.label_Steps = QtWidgets.QLabel(self.groupBox)
        self.label_Steps.setMinimumSize(QtCore.QSize(120, 0))
        self.label_Steps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Steps.setObjectName("label_Steps")
        self.horizontalLayout.addWidget(self.label_Steps)
        self.SB_StepsLimit = QtWidgets.QSpinBox(self.groupBox)
        self.SB_StepsLimit.setMaximum(999999)
        self.SB_StepsLimit.setObjectName("SB_StepsLimit")
        self.horizontalLayout.addWidget(self.SB_StepsLimit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Button_Load = QtWidgets.QPushButton(self.groupBox)
        self.Button_Load.setObjectName("Button_Load")
        self.verticalLayout_2.addWidget(self.Button_Load)
        self.Button_Run = QtWidgets.QPushButton(self.groupBox)
        self.Button_Run.setObjectName("Button_Run")
        self.verticalLayout_2.addWidget(self.Button_Run)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.Statistics_txt = QtWidgets.QPlainTextEdit(self.groupBox)
        self.Statistics_txt.setObjectName("Statistics_txt")
        self.verticalLayout_3.addWidget(self.Statistics_txt)
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.Main_Maze = QtWidgets.QWidget()
        self.Main_Maze.setObjectName("Main_Maze")
        self.gridLayout = QtWidgets.QGridLayout(self.Main_Maze)
        self.gridLayout.setObjectName("gridLayout")
        self.main_maze_img = QtWidgets.QLabel(self.Main_Maze)
        self.main_maze_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_maze_img.setText("")
        self.main_maze_img.setScaledContents(True)
        self.main_maze_img.setAlignment(QtCore.Qt.AlignCenter)
        self.main_maze_img.setObjectName("main_maze_img")
        self.gridLayout.addWidget(self.main_maze_img, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Main_Maze, "")
        self.BFS = QtWidgets.QWidget()
        self.BFS.setObjectName("BFS")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.BFS)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.BFS_maze_img = QtWidgets.QLabel(self.BFS)
        self.BFS_maze_img.setText("")
        self.BFS_maze_img.setScaledContents(True)
        self.BFS_maze_img.setAlignment(QtCore.Qt.AlignCenter)
        self.BFS_maze_img.setObjectName("BFS_maze_img")
        self.verticalLayout_5.addWidget(self.BFS_maze_img)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Button_Animate_2 = QtWidgets.QPushButton(self.BFS)
        self.Button_Animate_2.setObjectName("Button_Animate_2")
        self.horizontalLayout_4.addWidget(self.Button_Animate_2)
        self.Button_Cancel_2 = QtWidgets.QPushButton(self.BFS)
        self.Button_Cancel_2.setObjectName("Button_Cancel_2")
        self.horizontalLayout_4.addWidget(self.Button_Cancel_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.BFS, "")
        self.DFS = QtWidgets.QWidget()
        self.DFS.setObjectName("DFS")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.DFS)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.DFS_maze_img = QtWidgets.QLabel(self.DFS)
        self.DFS_maze_img.setText("")
        self.DFS_maze_img.setScaledContents(True)
        self.DFS_maze_img.setAlignment(QtCore.Qt.AlignCenter)
        self.DFS_maze_img.setObjectName("DFS_maze_img")
        self.gridLayout_4.addWidget(self.DFS_maze_img, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Button_Animate_3 = QtWidgets.QPushButton(self.DFS)
        self.Button_Animate_3.setObjectName("Button_Animate_3")
        self.horizontalLayout_5.addWidget(self.Button_Animate_3)
        self.Button_Cancel_3 = QtWidgets.QPushButton(self.DFS)
        self.Button_Cancel_3.setObjectName("Button_Cancel_3")
        self.horizontalLayout_5.addWidget(self.Button_Cancel_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.tabWidget.addTab(self.DFS, "")
        self.HOTW = QtWidgets.QWidget()
        self.HOTW.setObjectName("HOTW")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.HOTW)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.HOTW_maze_img = QtWidgets.QLabel(self.HOTW)
        self.HOTW_maze_img.setText("")
        self.HOTW_maze_img.setScaledContents(True)
        self.HOTW_maze_img.setAlignment(QtCore.Qt.AlignCenter)
        self.HOTW_maze_img.setObjectName("HOTW_maze_img")
        self.gridLayout_5.addWidget(self.HOTW_maze_img, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Button_Animate_4 = QtWidgets.QPushButton(self.HOTW)
        self.Button_Animate_4.setObjectName("Button_Animate_4")
        self.horizontalLayout_6.addWidget(self.Button_Animate_4)
        self.Button_Cancel_4 = QtWidgets.QPushButton(self.HOTW)
        self.Button_Cancel_4.setObjectName("Button_Cancel_4")
        self.horizontalLayout_6.addWidget(self.Button_Cancel_4)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.tabWidget.addTab(self.HOTW, "")
        self.RND = QtWidgets.QWidget()
        self.RND.setObjectName("RND")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.RND)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.RAND_maze_img = QtWidgets.QLabel(self.RND)
        self.RAND_maze_img.setText("")
        self.RAND_maze_img.setScaledContents(True)
        self.RAND_maze_img.setAlignment(QtCore.Qt.AlignCenter)
        self.RAND_maze_img.setObjectName("RAND_maze_img")
        self.gridLayout_6.addWidget(self.RAND_maze_img, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Button_Animate_5 = QtWidgets.QPushButton(self.RND)
        self.Button_Animate_5.setObjectName("Button_Animate_5")
        self.horizontalLayout_7.addWidget(self.Button_Animate_5)
        self.Button_Cancel_5 = QtWidgets.QPushButton(self.RND)
        self.Button_Cancel_5.setObjectName("Button_Cancel_5")
        self.horizontalLayout_7.addWidget(self.Button_Cancel_5)
        self.gridLayout_6.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.tabWidget.addTab(self.RND, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.Button_Export = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Export.setObjectName("Button_Export")
        self.verticalLayout_4.addWidget(self.Button_Export)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.get_ready()

        self.paners = [self.main_maze_img,self.BFS_maze_img,self.DFS_maze_img,self.HOTW_maze_img,self.RAND_maze_img]
        self.paner = self.paners[0]
        self.animation = []

        self.Button_Run.clicked.connect(self.RUN)
        self.Button_Load.clicked.connect(self.LOAD)
        self.Button_Export.clicked.connect(self.EXPORT)

        self.Button_Animate_2.clicked.connect(lambda x:self.Animate(i=1))
        self.Button_Animate_3.clicked.connect(lambda x:self.Animate(i=2))
        self.Button_Animate_4.clicked.connect(lambda x:self.Animate(i=3))
        self.Button_Animate_5.clicked.connect(lambda x:self.Animate(i=4))

        self.Button_Cancel_2.clicked.connect(lambda x:self.Cancel_Animate(i=1))
        self.Button_Cancel_3.clicked.connect(lambda x:self.Cancel_Animate(i=2))
        self.Button_Cancel_4.clicked.connect(lambda x:self.Cancel_Animate(i=3))
        self.Button_Cancel_5.clicked.connect(lambda x:self.Cancel_Animate(i=4))


        self.Maze_Solver = MAZE_SOLVER()
        self.images = []
        self.images_labels = ['maze','BFS','DFS','HOTW','RAND']
        
        self.worker = Animation_Worker()
        self.worker.ImageUpdate.connect(self.ImageUpdateSlot)


    def ImageUpdateSlot(self, Image):
        self.paner.setPixmap(QPixmap.fromImage(Image))


    def get_ready(self):
        '''Getting the current working path
        and check for the INPUT & OUTPUT folders if not exist make them'''
        if getattr(sys, 'frozen', False):
            self.application_path = os.path.dirname(sys.executable)
            self.app_name = os.path.basename(sys.executable)            

        elif __file__:
            self.application_path = os.path.dirname(__file__)
            self.app_name = os.path.basename(__file__) 


        self.INPUT_PATH = os.path.join(self.application_path, 'INPUT')
        if os.path.exists(self.INPUT_PATH):
                pass
        else :
            os.mkdir(self.INPUT_PATH)

        self.OUTPUT_PATH = os.path.join(self.application_path, 'OUTPUT')
        if os.path.exists(self.OUTPUT_PATH):
                pass
        else :
            os.mkdir(self.OUTPUT_PATH)
            
    def LOAD(self):
        '''Search the INPUT folder for CSV files
        append the file name to the combobox text to be visiable to the user
        and append the file path to the combobox data to be used later to access the file'''
        self.input_CSVs = []
        self.CSVs_name = []
        
        if os.path.exists(self.INPUT_PATH):
            for d,sd,f in os.walk(self.INPUT_PATH):
                for file_name in f:
                    temp = file_name.split('.')
                    if temp[-1] in ('CSV','csv') and file_name[0] != '~':
                        self.input_CSVs.append(os.path.join(d,file_name))
                        self.CSVs_name.append(file_name)
        else:
            self.Error = 'Input Path is not exist'


        self.CB_CSVs.clear()
        for index,file in enumerate(self.input_CSVs):
            self.CB_CSVs.addItem(self.CSVs_name[index], self.input_CSVs[index])

    def RUN(self):
        '''Read the CSV file and start the operation of solving the maze accourding to the 4 algorithms
        then display the images and the comparison txt'''
        if self.CB_CSVs.currentData() != '':
            if int(self.SB_TimeLimit.value()) == 0:
                time = None
            else:
                time = int(self.SB_TimeLimit.value())

            if int(self.SB_StepsLimit.value()) == 0:
                steps = None
            else:
                steps = int(self.SB_StepsLimit.value())

            comparison,imgs,maze_steps = self.Maze_Solver.operate(maze_file = self.CB_CSVs.currentData(), time_out=time, steps_out=steps,spacing=20)

            self.Statistics_txt.setPlainText(comparison)
            
            self.images = [img for img in imgs]
            self.animation = [item for item in maze_steps]

            for i, img in enumerate(imgs):
                self.display(image=img,paner=self.paners[i])

    
    def display(self,image,paner):
        '''Display the image into the paner area'''
        qformat = QImage.Format_RGB888
        qimage = QImage(image, image.shape[1], image.shape[0],qformat)                                                                                                                                                 

        pixmap = QPixmap(qimage)                                                                                                                                                                               
        #pixmap = pixmap.scaled(640,400, Qt.KeepAspectRatio)                                                                                                                                                    
        paner.setPixmap(pixmap)  


    def EXPORT(self):
        print(1)
        '''Export all the images into the OUTPUT folder with the name of the algorithm and in png format'''
        if self.images != []:
            for index,image in enumerate(self.images):
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                path = os.path.join(self.OUTPUT_PATH, f'{self.images_labels[index]}.png')
                cv2.imwrite(path,image)


    def Animate(self,i:int):
        '''Animating the solving path'''

        self.paner = self.paners[i]
        maze = self.Maze_Solver.copy_maze(self.animation[0])
        
        self.worker.maze = maze
        self.worker.steps = self.animation[i][0]
        self.worker.path = self.animation[i][1]
        self.worker.enable = True
        self.worker.start()


    def Cancel_Animate(self,i:int):
        '''Canceling the animation'''
        self.worker.stop()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Maze Configurations "))
        self.label_Time.setText(_translate("MainWindow", "Time Limit (s)"))
        self.label_Steps.setText(_translate("MainWindow", "Steps Limit"))
        self.Button_Load.setText(_translate("MainWindow", "Load Files"))
        self.Button_Run.setText(_translate("MainWindow", "Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main_Maze), _translate("MainWindow", "Maze"))
        self.Button_Animate_2.setText(_translate("MainWindow", "Animate"))
        self.Button_Cancel_2.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BFS), _translate("MainWindow", "Breadth First Search "))
        self.Button_Animate_3.setText(_translate("MainWindow", "Animate"))
        self.Button_Cancel_3.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DFS), _translate("MainWindow", "Depth First Search "))
        self.Button_Animate_4.setText(_translate("MainWindow", "Animate"))
        self.Button_Cancel_4.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HOTW), _translate("MainWindow", "Hand On The Wall "))
        self.Button_Animate_5.setText(_translate("MainWindow", "Animate"))
        self.Button_Cancel_5.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RND), _translate("MainWindow", "Random"))
        self.Button_Export.setText(_translate("MainWindow", "Export"))



class Animation_Worker(QThread):
    '''The Animation Thread as it can not be done in the main Thread'''
    ImageUpdate = pyqtSignal(QImage)

    steps = []
    path = []
    maze = []

    enable = False
    def run(self):
        '''The Animation Start function'''
        if self.enable:
            for cell in self.steps:
                if self.enable:
                    self.maze[cell[0]][cell[1]] = '*'

                    image = self.maze_image(self.maze)
                    qformat = QImage.Format_RGB888
                    qimage = QImage(image, image.shape[1], image.shape[0],qformat)                                                                                                                                                 
                    #pixmap = QPixmap(qimage)
                    pixmap = qimage.scaled(640,480,Qt.KeepAspectRatio)

                    self.ImageUpdate.emit(pixmap)

            for cell in self.path: 
                if self.enable:
                    self.maze[cell[0]][cell[1]] = '-'

                    image = self.maze_image(self.maze)
                    qformat = QImage.Format_RGB888
                    qimage = QImage(image, image.shape[1], image.shape[0],qformat)                                                                                                                                                 
                    #pixmap = QPixmap(qimage)
                    pixmap = qimage.scaled(640,480,Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(pixmap)
            self.enable = False

    def stop(self):
        '''Stop the animation and exit the thread'''
        self.enable = False
        self.quit()

    def maze_image(self,maze:list, width:int=720, height:int=480):
        '''Converting the Maze Matrix into a numpy pixmap (image)'''
        w, h = len(maze[0]), len(maze)
        maze_image = np.zeros((h, w, 3), dtype=np.uint8)

        for i,row in enumerate(maze):
            for j,col in enumerate(row):
                #RGB
                #represent the blocked cells with black
                if col == '#':
                    maze_image[i][j] = [0,0,0]
                #represent the free cells with white
                elif col == ' ':
                    maze_image[i][j] = [255,255,255]
                #represent the step-cells with red (the cells of solving (exclude the path cells))
                elif col == '*':
                    maze_image[i][j] = [255,0,0]
                #represent the path cells with green
                elif col == '-':
                    maze_image[i][j] = [0,255,0]
                #represent the others with blue
                else:
                    maze_image[i][j] = [0,0,255]
                    
        #scale the image up
        up_width = width
        up_height = height
        up_points = (up_width, up_height)
        maze_image = cv2.resize(maze_image, up_points, interpolation= cv2.INTER_LINEAR)
        return maze_image

    def display(self,image,paner):
        '''Display the image into the paner area'''
        qformat = QImage.Format_RGB888
        qimage = QImage(image, image.shape[1], image.shape[0],qformat)                                                                                                                                                 

        pixmap = QPixmap(qimage)                                                                                                                                                                               
        #pixmap = pixmap.scaled(640,400, Qt.KeepAspectRatio)                                                                                                                                                    
        paner.setPixmap(pixmap)

class MAZE_SOLVER:
    def __init__(self) -> None:
        '''the Maze solver class
        containing the 4 searching algorithms (BFS-BFS-HTOW-RAND)
        and reading maze from CSVs
        and converting the output to an image'''
        pass

    def createMaze(self):
        '''Create a simple maze matrix'''
        maze = []
        maze.append(['#','#','#','#','#','O','#','#','#'])
        maze.append(['#',' ',' ',' ',' ',' ',' ',' ','#'])
        maze.append(['#',' ','#','#',' ','#','#',' ','#'])
        maze.append(['#',' ','#',' ',' ',' ','#',' ','#'])
        maze.append(['#',' ','#',' ','#',' ','#',' ','#'])
        maze.append(['#',' ','#',' ','#',' ','#',' ','#'])
        maze.append(['#',' ','#',' ','#',' ','#','#','#'])
        maze.append(['#',' ','#',' ','#',' ',' ',' ','#'])
        maze.append(['#','#','#','#','#','#','#','X','#'])

        return maze
    
    def Read_Maze(self, file:str):
        '''Read the Maze from CSV file'''
        maze_file = file
        with open(maze_file, mode ='r')as file:
            csvFile = csv.reader(file)
            Maze = [] 
            for lines in csvFile:
                row = []
                for col in lines:
                    #the 0 or # represents the blocks 
                    if col in ['0','#']:
                        row.append('#')
                    #the 1 or space represents the free cell
                    elif col in ['1',' ']:
                        row.append(' ')
                    #the O or S represents the start point
                    elif col in ['S','O']:
                        row.append('O')
                    #the X or G represents the Goal point
                    elif col in ['G','X']:
                        row.append('X')
                Maze.append(row)

        return Maze

    def copy_maze(self,maze:list):
        '''Copy the Maze to avoid editing the original maze'''
        copy = []
        for i,row in enumerate(maze):
            copy.append([])
            for j,col in enumerate(row):
                copy[i].append(maze[i][j])

        return(copy)

    def printMaze(self, maze:list) -> None:
        '''Printing the maze into the terminal in a good shape'''
        maze_txt = ''
        for j, row in enumerate(maze):
            for i, col in enumerate(row):
                maze_txt += f'{col} '
            maze_txt += '\n'    
        print(maze_txt)

    def find_SG(self,maze:list) -> [tuple,tuple]:
        '''Finding the Start and Goal Points'''
        start, goal = None,None
        for i,row in enumerate(maze):
            for j,col in enumerate(row):
                if col == 'O':
                    start = (i,j)
                elif col == 'X':
                    goal = (i,j)

                if start is not None and goal is not None:
                    break
        return start,goal

    def directions(self,maze:list, Point:list, direction:str) -> tuple:
        '''Check the cell neighbours
        takes the maze and the cell as well as the direction of the neighbour
        returns the neighbour cell value if it's free cell or None if it's a blocked cell'''
        Y = len(maze)
        X = len(maze[0])

        x = Point[1]
        y = Point[0]

        if direction =='E':
            if x+1 in range(X):
                if maze[y][x+1] == '#':
                    return None
                else:
                    return (y,x+1)
            else: return None

        elif direction =='W':
            if x-1 in range(X):
                if maze[y][x-1] == '#':
                    return None
                else:
                    return (y,x-1)
            else: return None

        elif direction =='N':
            if y-1 in range(Y):
                if maze[y-1][x] == '#':
                    return None
                else:
                    return (y-1,x)
            else: return None

        elif direction =='S':
            if y+1 in range(Y):
                if maze[y+1][x] == '#':
                    return None
                else:
                    return (y+1,x)
            else: return None

    def maze_image(self,maze:list, width:int=720, height:int=480):
        '''Converting the Maze Matrix into a numpy pixmap (image)'''
        w, h = len(maze[0]), len(maze)
        maze_image = np.zeros((h, w, 3), dtype=np.uint8)

        for i,row in enumerate(maze):
            for j,col in enumerate(row):
                #RGB
                #represent the blocked cells with black
                if col == '#':
                    maze_image[i][j] = [0,0,0]
                #represent the free cells with white
                elif col == ' ':
                    maze_image[i][j] = [255,255,255]
                #represent the step-cells with red (the cells of solving (exclude the path cells))
                elif col == '*':
                    maze_image[i][j] = [255,0,0]
                #represent the path cells with green
                elif col == '-':
                    maze_image[i][j] = [0,255,0]
                #represent the others with blue
                else:
                    maze_image[i][j] = [0,0,255]
                    
        #scale the image up
        up_width = width
        up_height = height
        up_points = (up_width, up_height)
        maze_image = cv2.resize(maze_image, up_points, interpolation= cv2.INTER_LINEAR)
        return maze_image

    def DFS(self,maze,time_out=60,steps_out=None):
        '''Depth Fist Search Function
        Searching all the cells from the Left child to the Right
        It operats according to the LIFO'''
        start,goal = self.find_SG(maze)
        
        passed_points = 0 

        if time_out is not None:
            end_time = monotonic() + time_out   

        dfspath = dict()
        explored = [start]
        frontier = [start]

        path_found = False
        total_path = []
        while len(frontier)>0:
            #get cell according to LIFO
            currCell = frontier.pop()
            #if goal is reached break
            if currCell == goal:
                path_found = True
                break
            #if time limit is reached break
            if time_out is not None:
                if monotonic() >= end_time:
                    path_found = False
                    break
            #if step limit is reached break
            if steps_out is not None:
                if passed_points >= steps_out:
                    path_found = False  
                    break
            #get the cell neighbours
            for direction in ['E','S','N','W']:
                childcell = self.directions(maze,Point=currCell,direction=direction)
                if childcell is not None:
                    passed_points +=1
                    total_path.append(childcell)
                    if childcell in explored:
                        continue
                    else:
                        explored.append(childcell)
                        frontier.append(childcell)
                        dfspath[childcell] = currCell
        
        path = [start]

        for point in total_path:
            maze[point[0]][point[1]] = '*'

        if path_found:
            reverce = dict()
            #dfspath
            path = []
            cell = (goal[0],goal[1])
            while cell != start:
                reverce[dfspath[cell]] = cell
                path.append(cell)
                cell = dfspath[cell]
            
            if path[-1] != start:
                path.append(start)

            path = path[::-1]

            for point in path:
                maze[point[0]][point[1]] = '-'

        return path,passed_points,total_path,path_found,maze

    def BFS(self,maze,time_out=60,steps_out=None):
        '''Breadth Fist Search Function
        Searching all the cells in levels
        It operats according to the FIFO'''
        start,goal=self.find_SG(maze)
        passed_points = 0

        if time_out is not None:
            end_time = monotonic() + time_out   

        bfspath = dict()
        explored = [start]
        frontier = [start]
        path_found = False

        total_path = []

        while len(frontier)>0:
            #get cell according to FIFO
            currCell = frontier.pop(0)
            #if goal is reached break
            if currCell == goal:
                path_found = True
                break
            #if time limit is reached break
            if time_out is not None:
                if monotonic() >= end_time:
                    path_found = False
                    break
            #if step limit is reached break
            if steps_out is not None:
                if passed_points >= steps_out:
                    path_found = False  
                    break
            #get the cell neighbours
            for direction in ['E','S','N','W']:
                childcell = self.directions(maze,Point=currCell,direction=direction)
                if childcell is not None:
                    passed_points +=1

                    total_path.append(childcell)
                    if childcell in explored:
                        continue
                    else:
                        explored.append(childcell)
                        frontier.append(childcell)
                        bfspath[childcell] = currCell
        
        path = [start]

        for point in total_path:
            maze[point[0]][point[1]] = '*'

        if path_found:
            reverce = dict()

            path = []
            cell = (goal[0],goal[1])
            while cell != start:
                reverce[bfspath[cell]] = cell
                path.append(cell)
                cell = bfspath[cell]
            
            if path[-1] != start:
                path.append(start)

            path = path[::-1]

            for point in path:
                maze[point[0]][point[1]] = '-'

        return path,passed_points,total_path,path_found,maze


    def HOTW(self,maze,time_out=60,steps_out=None):
        '''Hand On The Wall Function
        Searching all the cells according to moving with the left wall'''
        start,goal=self.find_SG(maze)
        passed_points = 0 

        if time_out is not None:
            end_time = monotonic() + time_out   

        #define the initial heading ==> the heading will change in case of rotation
        heading = {'forward':'N','left':'W','back':'S','right':'E'}

        #rotate Clock Wise & Conter Clock Wise ==> change the heading dict
        RCW = lambda heading: dict(zip(list(heading.keys()),[list(heading.values())[-1]]+list(heading.values())[:-1]))
        RCCW = lambda heading: dict(zip(list(heading.keys()),list(heading.values())[1:]+[list(heading.values())[0]]))

        path = []
        hotw_path = []

        currCell = start
        heading['forward']
        points_path = []

        path_dir = ''
        path_found = False

        while True:
            #if goal is reached break
            if currCell == goal:
                path_found = True
                break
            #if time limit is reached break
            if time_out is not None:
                if monotonic() >= end_time:
                    path_found = False
                    break
            #if steps limit is reached break
            if steps_out is not None:
                if passed_points >= steps_out:
                    path_found = False  
                    break

            if self.directions(maze,Point=currCell,direction=heading['left']) is None:
                childcell = self.directions(maze,Point=currCell,direction=heading['forward'])
                if childcell is None:
                    heading = RCW(heading)
                else:
                    passed_points +=1
                    path_dir += heading['forward']
                    hotw_path.append(childcell)
                    currCell = childcell
            else:
                heading = RCCW(heading)
                childcell = self.directions(maze,Point=currCell,direction=heading['forward'])
                passed_points +=1
                path_dir += heading['forward']
                hotw_path.append(childcell)
                currCell = childcell

            points_path.append(currCell)

        path = [start]

        for point in hotw_path:
                maze[point[0]][point[1]] = '*'

        if path_found:  
            while 'EW' in path_dir or 'WE' in path_dir or 'SN' in path_dir or 'NS' in path_dir:
                path_dir = path_dir.replace('EW','')
                path_dir = path_dir.replace('WE','')
                path_dir = path_dir.replace('SN','')
                path_dir = path_dir.replace('NS','')
            
            currCell = start
            for direction in path_dir:
                childcell = self.directions(maze,Point=currCell,direction=direction)
                path.append(childcell)
                currCell = childcell

            for point in path:
                maze[point[0]][point[1]] = '-'

        return path,passed_points,hotw_path,path_found,maze


    def RAND(self, maze:list, time_out:str=60, steps_out:int=None):
        '''Random search algorithm 
        in this algorithm the movement occurs randomly accourding to move forward or left or right, and rotation
        ''' 
        start,goal=self.find_SG(maze)
        passed_points = 0 

        if time_out is not None:
            end_time = monotonic() + time_out   
        #define the initial heading ==> the heading will change in case of rotation
        heading = {'forward':'N','left':'W','back':'S','right':'E'}
        #rotate Clock Wise & Conter Clock Wise ==> change the heading dict
        RCW = lambda heading: dict(zip(list(heading.keys()),[list(heading.values())[-1]]+list(heading.values())[:-1]))
        RCCW = lambda heading: dict(zip(list(heading.keys()),list(heading.values())[1:]+[list(heading.values())[0]]))


        path = []
        rand_path = []

        currCell = start
        heading['forward']
        points_path = []

        path_dir = ''
        path_found = False

        rotations = ['CW','CCW']
        while True:
            if currCell == goal:
                path_found = True
                break

            if time_out is not None:
                if monotonic() >= end_time:
                    path_found = False
                    break

            if steps_out is not None:
                if passed_points >= steps_out:
                    path_found = False  
                    break

            direction = choice(['forward','right','left'])

            childcell = self.directions(maze,Point=currCell,direction=heading[direction])
            if childcell is not None:
                passed_points +=1
                path_dir += heading[direction]
                rand_path.append(childcell)
                currCell = childcell

            elif direction != 'forward':
                direction = 'forward'
                childcell = self.directions(maze,Point=currCell,direction=heading[direction])
                if childcell is not None:
                    passed_points +=1
                    path_dir += heading[direction]
                    rand_path.append(childcell)
                    currCell = childcell

            else:
                rotation = choice(rotations)
                if rotation == 'CW':
                    heading = RCW(heading)

                elif rotation == 'CCW': 
                    heading = RCCW(heading)

        path = [start]
        for point in rand_path:
                maze[point[0]][point[1]] = '*'

        if path_found:
            while 'EW' in path_dir or 'WE' in path_dir or 'SN' in path_dir or 'NS' in path_dir:
                path_dir = path_dir.replace('EW','')
                path_dir = path_dir.replace('WE','')
                path_dir = path_dir.replace('SN','')
                path_dir = path_dir.replace('NS','')
            currCell = start
            for direction in path_dir:
                childcell = self.directions(maze,Point=currCell,direction=direction)
                path.append(childcell)
                currCell = childcell

            for point in path:
                maze[point[0]][point[1]] = '-'

        return path,passed_points,rand_path,path_found,maze


    def operate(self, maze_file:str= 'Maze.csv', time_out:int=60, steps_out:int=None, spacing:int=20) -> [str,list,list]:
        '''Full Operation function 
        takes the Maze
        solves it with (BFS-DFS-HTOW-RAND) methods
        and return the comparison data and the solving images'''

        original_maze = self.Read_Maze(maze_file) 
        start,goal = self.find_SG(original_maze)

        if start is None or goal is None:
            print('Maze has no start or no goal')
        else:

            comparison = [['Method','Maze Solved','Path Steps','Total Steps']]

            #============Breadth-first-search============
            MAZE_copy = self.copy_maze(original_maze)

            bfs_final_path, steps, bfs_total_steps, path_found, bfs_maze = self.BFS(MAZE_copy,time_out=time_out,steps_out=steps_out)
            if path_found:
                comparison.append(['BFS','True',f'{len(bfs_final_path)}',f'{steps}'])
            else:
                comparison.append(['BFS','False','-',f'{steps}'])
            #============================================

            #=============Depth-first-search=============
            MAZE_copy = self.copy_maze(original_maze)
            dfs_final_path, steps, dfs_total_steps, path_found, dfs_maze = self.DFS(MAZE_copy,time_out=time_out,steps_out=steps_out)
            
            if path_found:
                comparison.append(['DFS','True',f'{len(dfs_final_path)}',f'{steps}'])
            else:
                comparison.append(['DFS','False','-',f'{steps}'])
            #============================================


            #==============Hand-On-The-Wall==============
            MAZE_copy = self.copy_maze(original_maze)
            hotw_final_path, steps, hotw_total_steps, path_found, hotw_maze = self.HOTW(MAZE_copy,time_out=time_out,steps_out=steps_out)
            if path_found:
                comparison.append(['HOTW','True',f'{len(hotw_final_path)}',f'{steps}'])
            else:
                comparison.append(['HOTW','False','-',f'{steps}'])
            #============================================

            #====================RAND====================
            MAZE_copy = self.copy_maze(original_maze)
            rand_final_path, steps, rand_total_steps, path_found, rand_maze = self.RAND(MAZE_copy,time_out=time_out,steps_out=steps_out)
            if path_found:
                comparison.append(['RAND','True',f'{len(rand_final_path)}',f'{steps}'])
            else:
                comparison.append(['RAND','False','-',f'{steps}'])
            #============================================

            COMP_TXT = ''
            for row in comparison:
                for col in row:
                    COMP_TXT += f'{col}{" "*(spacing-len(col))}'
                COMP_TXT += '\n'

            original_img = self.maze_image(original_maze)
            dfs_img = self.maze_image(dfs_maze)
            bfs_img = self.maze_image(bfs_maze)
            hotw_img = self.maze_image(hotw_maze)
            rand_img = self.maze_image(rand_maze)


            return COMP_TXT, [original_img, bfs_img, dfs_img, hotw_img, rand_img], [original_maze, [bfs_total_steps,bfs_final_path], [dfs_total_steps,dfs_final_path], [hotw_total_steps,hotw_final_path], [rand_total_steps,rand_final_path]]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
