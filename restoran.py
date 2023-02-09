from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import sys
import os
os.system("cls")
class dastur(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMaximumSize(1500,800)
        self.setMinimumSize(1500,800)
        self.setFont(QFont("calibri",20))

        self.milly=QLabel("Milliy taomlar: ",self)
        self.milly.setGeometry(50,30,250,50)
        self.mil=QComboBox(self)
        self.mil.setGeometry(283,30,350,50)
        self.mil.setStyleSheet("""
        background-color: rgb(255,165,0)""")
        self.mil.addItems(["","Osh 30000","Mastava 27000","Shorva 20000","Dimlama 50000","Manti 10000"])

        self.millysoni=QLabel("Soni: ",self)
        self.millysoni.setGeometry(650,30,150,50)
        self.milsoni=QComboBox(self)
        self.milsoni.setGeometry(750,30,70,50)
        self.milsoni.setStyleSheet("""
        background-color: rgb(128,128,128)""")
        self.milsoni.addItems(["0","1","2","3","4","5","6","7","8","9","10"])
        

        self.fast=QLabel("Fast foodlar: ",self)
        self.fast.setGeometry(50,90,250,50)
        self.fa=QComboBox(self)
        self.fa.setGeometry(283,90,350,50)
        self.fa.setStyleSheet("""
        background-color: rgb(255,165,0)""")
        self.fa.addItems(["","Lavash 25000","Sendvich 27000","Gamburger 21000","Pitsa 78000","Hot-Dog 20000","Fri 16000"])

        self.fastsoni=QLabel("Soni: ",self)
        self.fastsoni.setGeometry(650,90,150,50)
        self.fasoni=QComboBox(self)
        self.fasoni.setGeometry(750,90,70,50)
        self.fasoni.setStyleSheet("""
        background-color: rgb(128,128,128)""")
        self.fasoni.addItems(["0","1","2","3","4","5","6","7","8","9","10"])
        
        self.cola=QLabel("Ichimliklar: ",self)
        self.cola.setGeometry(50,150,250,50)
        self.co=QComboBox(self)
        self.co.setGeometry(283,150,350,50)
        self.co.setStyleSheet("""
        background-color: rgb(255,165,0)""")
        self.co.addItems(["","Coca-Cola 12000","Pepsi 14000","Choy 5000","Sharbat 10000"])

        self.colasoni=QLabel("Soni: ",self)
        self.colasoni.setGeometry(650,150,150,50)
        self.cosoni=QComboBox(self)
        self.cosoni.setGeometry(750,150,70,50)
        self.cosoni.setStyleSheet("""
        background-color: rgb(128,128,128)""")
        self.cosoni.addItems(["0","1","2","3","4","5","6","7","8","9","10"])
        
        self.dav=QLabel("Disertlar: ",self)
        self.dav.setGeometry(50,210,250,50)
        self.la=QComboBox(self)
        self.la.setGeometry(283,210,350,50)
        self.la.setStyleSheet("""
        background-color: rgb(255,165,0)""")
        self.la.addItems(["","Peramida 30000","Napalyon 25000"])

        self.davsoni=QLabel("Soni: ",self)
        self.davsoni.setGeometry(650,210,150,50)
        self.lasoni=QComboBox(self)
        self.lasoni.setGeometry(750,210,70,50)
        self.lasoni.setStyleSheet("""
        background-color: rgb(128,128,128)""")
        self.lasoni.addItems(["0","1","2","3","4","5","6","7","8","9","10"])
       

        self.bat=QPushButton("Chek",self)
        self.bat.setGeometry(283,300,150,50)
        self.bat.setStyleSheet("""
        color: rgb(50,205,50);
        background-color: rgb(0,0,0);
        border-color: rgb(50,205,50);
        border-width: 3px;
        border-radius: 20px;
        border-style: outset;""")
        self.bat.clicked.connect(self.natija) 

        self.milly1=QLabel("Milliy taomlar: ",self)
        self.milly1.setGeometry(50,360,250,50)
        self.mil1=QLineEdit(self)
        self.mil1.setGeometry(283,360,350,50)
        self.mil1.setStyleSheet("""
        background-color: rgb(50,205,50)""")

        self.milly1soni=QLabel(self)
        self.milly1soni.setGeometry(650,360,150,50)
        self.mil1soni=QLineEdit(self)
        self.mil1soni.setGeometry(750,360,50,50)
        self.mil1soni.setStyleSheet("""
        background-color: rgb(128,128,128)""")
    

        self.fast1=QLabel("Fast foodlar: ",self)
        self.fast1.setGeometry(50,420,250,50)
        self.fa1=QLineEdit(self)
        self.fa1.setGeometry(283,420,350,50)
        self.fa1.setStyleSheet("""
        background-color: rgb(50,205,50)""")

        self.fast1soni=QLabel(self)
        self.fast1soni.setGeometry(650,420,150,50)
        self.fa1soni=QLineEdit(self)
        self.fa1soni.setGeometry(750,420,50,50)
        self.fa1soni.setStyleSheet("""
        background-color: rgb(128,128,128)""")
                
        self.cola1=QLabel("Ichimliklar: ",self)
        self.cola1.setGeometry(50,480,250,50)
        self.co1=QLineEdit(self)
        self.co1.setGeometry(283,480,350,50)
        self.co1.setStyleSheet("""
        background-color: rgb(50,205,50)""")

        self.cola1soni=QLabel(self)
        self.cola1soni.setGeometry(650,480,150,50)
        self.co1soni=QLineEdit(self)
        self.co1soni.setGeometry(750,480,50,50)
        self.co1soni.setStyleSheet("""
        background-color: rgb(128,128,128)""")
        

        self.dav1=QLabel("Disertlar: ",self)
        self.dav1.setGeometry(50,540,250,50)
        self.la1=QLineEdit(self)
        self.la1.setGeometry(283,540,350,50)
        self.la1.setStyleSheet("""
        background-color: rgb(50,205,50)""")

        self.dav1soni=QLabel(self)
        self.dav1soni.setGeometry(650,540,150,50)
        self.la1soni=QLineEdit(self)
        self.la1soni.setGeometry(750,540,50,50)
        self.la1soni.setStyleSheet("""
        background-color: rgb(128,128,128)""")

        

        self.sum=QLabel("Umumiy narx: ",self)
        self.sum.setGeometry(50,600,250,50)
        self.su=QLineEdit(self)
        #self.su.setText()
        self.su.setGeometry(283,600,350,50)
        self.su.setStyleSheet("""
        background-color: rgb(128,128,128)""")


        
        
    
    def natija(self):
        self.summa=0

        self.milly.hide()
        self.mil.hide()
        self.fast.hide()
        self.fa.hide()
        self.cola.hide()
        self.co.hide()
        self.dav.hide()
        self.la.hide()

        self.millysoni.hide()
        self.milsoni.hide()
        self.fastsoni.hide()
        self.fasoni.hide()
        self.colasoni.hide()
        self.cosoni.hide()
        self.davsoni.hide()
        self.lasoni.hide()
        
        self.mil1.setText(self.mil.currentText())
        self.mil1soni.setText(self.milsoni.currentText())

        self.fa1.setText(self.fa.currentText())
        self.fa1soni.setText(self.fasoni.currentText())

        self.co1.setText(self.co.currentText())
        self.co1soni.setText(self.cosoni.currentText())

        self.la1.setText(self.la.currentText())
        self.la1soni.setText(self.lasoni.currentText())

        self.mil=self.mil.currentText().split()
        self.fa=self.fa.currentText().split()
        self.co=self.co.currentText().split()
        self.la=self.la.currentText().split()

        if self.milsoni.currentText()!='0':
           self.summa+=(int(self.mil[1])*int(self.milsoni.currentText()))
        print()
        if self.fasoni.currentText()!='0':
           self.summa+=(int(self.fa[1])*int(self.fasoni.currentText()))
        if self.cosoni.currentText()!='0':
           self.summa+=(int(self.co[1])*int(self.cosoni.currentText()))
        if self.lasoni.currentText()!='0':
           self.summa+=(int(self.la[1])*int(self.lasoni.currentText()))
        self.su.setText(str(self.summa))

ap=QApplication(sys.argv)
loy=dastur()
loy.show()
sys.exit(ap.exec())      