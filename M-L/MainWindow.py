from MainMenu2 import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox,QTableWidgetItem
import mysql.connector
import time
import numpy as np
import pandas as pd
import csv
from graph import Mat
from kmeansexp import Kmeans1
from dbscan2 import dbexp







class myApp(QtWidgets.QMainWindow):
    connetion=mysql.connector.connect(
    host="localhost", #192.23.45.56
    user="root",
    password="58021169282",
    database="epl")
    connetion=connetion
    cursor=connetion.cursor(dictionary=True)
    def __init__(self):
        super(myApp,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnVeriOku.clicked.connect(self.getVeri)
        self.ui.btnTop.clicked.connect(self.graph1)
        self.ui.btnKmeans.clicked.connect(self.km)
        self.ui.pushButton.clicked.connect(self.db)
        self.ui.btnAvg.clicked.connect(self.avg)
        

        
        #self.ui.btnAvg.clicked.connect(self.)

    def getVeri(self):
        
        
        self.cursor=self.connetion.cursor(dictionary=True)
        self.cursor.execute("Select * From epl_20_21")
        result=self.cursor.fetchall()
        self.futbolcular=[]
        for i in result:
            self.futbolcular.append(i)



       
        
        
        
       
        
        self.ui.tableWidget.setRowCount(len(self.futbolcular))
        self.ui.tableWidget.setColumnCount(18)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Name','Club','Nationality','Position','Age','Matches',"Starts","Mins","Goals","Assists","Passes_Attempted","Perc_Passes_Completed","Penalty_Goals","Penalty_Attempted","xG","xA","Yellow_Cards","Red_Cards"))
        rowIndex=0
        for i in self.futbolcular:
            self.ui.tableWidget.setItem(rowIndex,0,QTableWidgetItem(i["Name"]))
            self.ui.tableWidget.setItem(rowIndex,1,QTableWidgetItem(i["Club"]))
            self.ui.tableWidget.setItem(rowIndex,2,QTableWidgetItem(i["Nationality"]))
            self.ui.tableWidget.setItem(rowIndex,3,QTableWidgetItem(i["Position"]))
            self.ui.tableWidget.setItem(rowIndex,4,QTableWidgetItem((i["Age"])))
            self.ui.tableWidget.setItem(rowIndex,5,QTableWidgetItem((i["Matches"])))
            self.ui.tableWidget.setItem(rowIndex,6,QTableWidgetItem((i["Starts"])))
            self.ui.tableWidget.setItem(rowIndex,7,QTableWidgetItem((i["Mins"])))
            self.ui.tableWidget.setItem(rowIndex,8,QTableWidgetItem((i["Goals"])))
            self.ui.tableWidget.setItem(rowIndex,9,QTableWidgetItem((i["Assists"])))
            self.ui.tableWidget.setItem(rowIndex,10,QTableWidgetItem((i["Passes_Attempted"])))
            self.ui.tableWidget.setItem(rowIndex,11,QTableWidgetItem((i["Perc_Passes_Completed"])))
            self.ui.tableWidget.setItem(rowIndex,12,QTableWidgetItem((i["Penalty_Goals"])))
            self.ui.tableWidget.setItem(rowIndex,13,QTableWidgetItem((i["Penalty_Attempted"])))
            self.ui.tableWidget.setItem(rowIndex,14,QTableWidgetItem((i["xG"])))
            self.ui.tableWidget.setItem(rowIndex,15,QTableWidgetItem((i["xA"])))
            self.ui.tableWidget.setItem(rowIndex,16,QTableWidgetItem((i["Yellow_Cards"])))
            self.ui.tableWidget.setItem(rowIndex,17,QTableWidgetItem((i["Red_Cards"])))

            rowIndex+=1
    def graph1(self):
        self.t=Mat()
        self.t.Top()
    def km(self):
        self.t=Kmeans1()
        self.t.Alg()
    def db(self):
        self.t=dbexp()
        self.t.dbs1()
    def avg(self):
        self.dataset=pd.read_csv('EPL_20_21.csv')
        self.result=self.dataset[(self.dataset["Goals"].max())==self.dataset["Goals"]][["Name","Goals"]].head(1)
        self.result2=self.dataset[(self.dataset["Matches"].max())==self.dataset["Matches"]][["Name","Matches"]].head(1)
        self.result1=self.dataset[(self.dataset["Assists"].max())==self.dataset["Assists"]][["Name","Assists"]].head(1)
        
        self.ui.listWidget.addItem("Top Scored Player\n"+str(self.result))
        self.ui.listWidget.addItem("Top Scored Assists\n"+str(self.result1))
        self.ui.listWidget.addItem("Top Matches Played\n"+str(self.result2))
      
       
       
        
       
             
      
        

        
        


          









 




def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())


app()

