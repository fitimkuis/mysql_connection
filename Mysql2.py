# -*- coding: utf8 -*-
from datetime import date, datetime, timedelta
import time
from win32com.client import Dispatch
##import win32com.client as win32
import MySQLdb
class Mysql(object):

    def __init__(self):
        self.arvot0 = ""
        self.arvot1 = ""
        self.arvot2 = ""
        self.arvot3 = ""
        self.arvot4 = ""
        self.arvot5 = ""
        self.val = ""
        self.i = 0
        self.count = 0
        self.count2 = 0
        file_name =  'C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\mysql_data.xls'
        #self.xlApp = win32.gencache.EnsureDispatch('Excel.Application')
        self.xlApp = Dispatch ("Excel.Application")   #Calls for Excel
        self.xlApp.Visible = 1
        self.xlWb = self.xlApp.Workbooks.Open(file_name)    #It finds the workbook
        #self.xlSht = self.xlWb.Worksheets("Sheet1")
        #self.xlSht.Columns.AutoFit()
        #self.xlSht.Range("E1:E36").Select()
        #self.xlSht.Cells.Range("E1:E36").Text #kasitellaan tekstina
        #self.xlApp.Selection.AutoFill(self.xlSht.Range("E1:E36"),win32.constants.xlFillDefault)
        

    def connect(self,a): #jos a saa arvon niin yhteys kantaan
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

    def get_range(self): #return count of used cells
        used = self.xlApp.ActiveWorkbook.Sheets("Sheet1").UsedRange
        nrows = used.Row + used.Rows.Count - 1
        ncols = used.Column + used.Columns.Count - 1
        cells = nrows * ncols
        print cells
        return cells #palautetaan excel taulukossa käytöss olevien solujen määrä
        #return self.xlApp.ActiveWorkbook.Sheets("Sheet1").UsedRange()
        
    def mysql_read(self,a): #jos a saa arvon luodaan uusi excel kannassa olevilla tiedoilla
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

    def read_excel(self):
        #print ("read_excel %d " )% self.count2
        #self.i=0
        self.xlSht = self.xlWb.Worksheets (1)   #Goes to sheet 1
        dataList = []
        for row_ind in range (1,36 + 1): #self.count2 It goes through the  items in A and B...
            for col in ('A','B','C','D','E','F'):
                dataList.append(self.xlSht.Cells(row_ind,col))
        #print (dataList[0])
        self.val = dataList[self.i]
            #print ("i:n arvo %d ") %self.i
            #print str(self.val)
        self.i = self.i + 1

        if self.i % 5 == 0:
            x = self.val  ##TODO
            time.strptime(str(x),"%d-%m-%Y %H:%M:%S")
            #x = x.split()[0]
            #from1900to1970 = datetime(1970,1,1) - datetime(1900,1,1) + timedelta(days=2)
            #x = date.fromtimestamp( int(x) * 86400) - from1900to1970
            #x = time.strftime('%d, %m %Y')
            print "date is %s "% x
            return str(x)
        
        elif self.i % 6 == 0:
            #today = datetime.date.today()
            #print today.strftime('We are the %d, %m %Y')
            x = self.val # a float
            #print "X value is %s " % x
            c = self.convertStr(str(x))
            #print "C value is %s " % c
            print self.convert_excel_time(c,hour24=False)
            return str(self.convert_excel_time(c,hour24=False))
            #print convert_excel_time(0.400983796)
            #print convert_excel_time(0.900983796, hour24=False)
            #print convert_excel_time(0.4006944444444)
            #print convert_excel_time(1.4006944444444)
            #print self.convert_excel_time(x)
        else:
            print "val value is %s " % str(self.val)
            return str(self.val) #palautetaan excelista luettu solun arvo

    def close_excel(self): ##solve this TODO
        self.xlApp.ActiveWorkbook.Close(SaveChanges=1) # see note 1
        self.xlApp.Quit()
        self.xlApp.Visible = 0 # see note 2
        del self.xlApp

    def write_to_excel():
        self.xlApp.Worksheets("Sheet1").Range("A5").Value = "Pasi"
        self.xlApp.Worksheets("Sheet1").Range("B5").Value = "Nurmi"
        self.xlApp.Worksheets("Sheet1").Range("C5").Value = "Turku"

    def convertStr(self,s):
        """Convert string to either int or float."""
        try:
            ret = int(s)
        except ValueError:
            #Try float.
            ret = float(s)
        return ret

    def convert_excel_time(self,t, hour24=True):
        if t > 1:
            t = t%1
        seconds = round(t*86400)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hour24:
            if hours > 12:
                hours -= 12
                return "%d:%d:%d PM" % (hours, minutes, seconds)
            else:
                return "%d:%d:%d AM" % (hours, minutes, seconds)
        return "%d:%d:%d" % (hours, minutes, seconds)

#OBJECT = Mysql()
#luku = OBJECT.get_range()
#print luku
#OBJECT.connect(0) #0 excel table is done, 1 excel table generated
#OBJECT.mysql_read(0) #0 excel table is done, 1 excel table generated
#for x in range (36-1):
#    OBJECT.read_excel()
#OBJECT.close_excel()
#DICTIONARY = { 1: 'one', 2: 'two', 3: 'three'}

#jos luokka ja module nimi on sama riittaa vain RIDE MyObject
#jos ovat eri niin module.MyObject
