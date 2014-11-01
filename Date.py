# -*- coding: utf8 -*-
from win32com.client import Dispatch
import MySQLdb
class Date(object):

    def __init__(self):
        self.arvot0 = ""
        self.arvot1 = ""
        self.arvot2 = ""
        self.arvot3 = ""
        self.arvot4 = ""
        self.arvot5 = ""
        self.val = ""
        self.nrows = 0
        self.i = 0
        self.count = 0
        self.count2 = 0
        file_name =  'C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\date.xls'
        self.xlApp = Dispatch ("Excel.Application")   #Calls for Excel
        self.xlApp.Visible = 1
        self.xlWb = self.xlApp.Workbooks.Open(file_name)    #It finds the workbook
        #self.xlSht.Cells.Range("A1:A36").Text #kasitellaan tekstina
        

    def connect_date(self,a): #jos a saa arvon niin yhteys kantaan
        if a:
            self.db=MySQLdb.connect(host="localhost",user="root",passwd="root",db="lotto")
            self.c=self.db.cursor()
            self.count = self.c.execute("select id, name, line, Weekday, Date, Time from rivit_new ORDER BY Date DESC")
            print self.count
            self.count2 = self.count
            return self.count2 #palautetaan rivien maara
        else:
            self.db=MySQLdb.connect(host="localhost",user="root",passwd="root",db="lotto")
            self.c=self.db.cursor()
            self.count = self.c.execute("select id, name, line, Weekday, Date, Time from rivit_new ORDER BY Date DESC")
            print self.count
            self.count2 = self.count
            self.db.close()
            return self.count2 #palautetaan rivien maara

    def get_rows(self): #return count of used rows
        used = self.xlApp.ActiveWorkbook.Sheets("date").UsedRange
        self.nrows = used.Row + used.Rows.Count - 1
        ncols = used.Column + used.Columns.Count - 1
        cells = self.nrows * ncols
        #print cells
        return self.nrows #palautetaan excel taulukossa käytöss olevien solujen määrä
        #return self.xlApp.ActiveWorkbook.Sheets("Sheet1").UsedRange()
        
    def mysql_date(self,a): #jos a saa arvon luodaan uusi excel kannassa olevilla tiedoilla
        if a:
            row = self.c.fetchone()
            #while row is not None:
            while self.count != 0:
                #print "%s %s %s %s %s %s" % (row[0], row[1], row[2], row[3], row[4], row[5])
                #print row[1]
                #print row
                #self.arvot = "".join([self.arvot,row[1],'_',row[3],'=',str(row[4]),'&'])
                self.arvot0 = row[0]
                self.arvot1 = row[1]
                self.arvot2 = row[2]
                self.arvot3 = row[3]
                self.arvot4 = row[4]
                self.arvot5 = row[5]
                self.xlApp.Worksheets("Sheet1").Range("A%s"%self.count).Value = str(self.arvot0)
                self.xlApp.Worksheets("Sheet1").Range("B%s"%self.count).Value = str(self.arvot1)
                self.xlApp.Worksheets("Sheet1").Range("C%s"%self.count).Value = str(self.arvot2)
                self.xlApp.Worksheets("Sheet1").Range("D%s"%self.count).Value = str(self.arvot3)
                self.xlApp.Worksheets("Sheet1").Range("E%s"%self.count).Value = str(self.arvot4)
                self.xlApp.Worksheets("Sheet1").Range("F%s"%self.count).Value = str(self.arvot5)
                row = self.c.fetchone()
                #eka = row[0]
                self.count = self.count - 1
        else:
            return #poistutaan funktiosta jos a saanut arvon 0
        #return str(self.arvot1)

    def read_date(self):
        xlSht = self.xlWb.Worksheets (1)   #Goes to sheet 1
        dataList = []
        for row_ind in range (1,self.nrows+1): #It goes through the  items in A and B...
            for col in ('A'):
                dataList.append(xlSht.Cells(row_ind,col))
        self.val = dataList[self.i]
        self.i = self.i + 1
        return str(self.val),self.i #palautetaan excelista luettu solun arvo ja kohta

    def close_date(self): ##solve this TODO
        self.xlApp.ActiveWorkbook.Close(SaveChanges=1) # see note 1
        self.xlApp.Quit()
        self.xlApp.Visible = 0 # see note 2
        del self.xlApp


OBJECT = Date()
#OBJECT.get_rows()
#OBJECT.read_date()

#luku = OBJECT.get_range()
#print luku
#OBJECT.connect(0) #0 excel table is done, 1 excel table generated
#OBJECT.mysql_read(0) #0 excel table is done, 1 excel table generated
#OBJECT.read_excel()
#OBJECT.close_excel()
#DICTIONARY = { 1: 'one', 2: 'two', 3: 'three'}

#jos luokka ja module nimi on sama riittaa vain RIDE MyObject
#jos ovat eri niin module.MyObject
