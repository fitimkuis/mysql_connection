# -*- coding: utf8 -*-
from datetime import date, datetime, timedelta
import time
from win32com.client import Dispatch
import MySQLdb
import subprocess
import os
import csv
class Mysql(object):

    def __init__(self):
        self.status = 0
        self.arvot0 = ""
        self.arvot1 = ""
        self.arvot2 = ""
        self.arvot3 = ""
        self.arvot4 = ""
        self.arvot5 = ""
        self.val = ""
        self.val2 = ""
        self.i = 0
        self.z = 0
        self.count = 0
        self.count2 = 0
        self.file_name =  'C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\mysql_data.xls'
        self.xlApp = Dispatch ("Excel.Application")   #Calls for Excel
        self.xlApp.Visible = 1
        self.xlWb = self.xlApp.Workbooks.Open(self.file_name)    #It finds the workbook
        
        self.file_name2 =  'C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\mysql_data2.xls'
        self.xlApp2 = Dispatch ("Excel.Application")   #Calls for Excel
        self.xlApp2.Visible = 1
        self.xlWb2 = self.xlApp2.Workbooks.Open(self.file_name2)    #It finds the workbook

        '''file_name =  'C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\mysql_data.xls'
        file_name2 =  'C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\mysql_data2.xls'
        #self.xlApp = win32.gencache.EnsureDispatch('Excel.Application')
        self.xlApp = Dispatch ("Excel.Application")   #Calls for Excel
        self.xlApp.Visible = 1
        self.xlWb = self.xlApp.Workbooks.Open(file_name)    #It finds the workbook
        
        self.xlApp2 = Dispatch ("Excel.Application")   #Calls for Excel
        self.xlApp2.Visible = 1
        self.xlWb2 = self.xlApp2.Workbooks.Open(file_name2)    #It finds the workbook'''
        #self.xlSht = self.xlWb.Worksheets("Sheet1")
        #self.xlSht.Columns.AutoFit()
        #self.xlSht.Range("E1:E36").Select()
        #self.xlSht.Cells.Range("E1:E36").Text #kasitellaan tekstina
        #self.xlApp.Selection.AutoFill(self.xlSht.Range("E1:E36"),win32.constants.xlFillDefault)
        

    def read_csv(self):
        path = 'C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\animals.csv'
        elist = []
        with open(path, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                elist.append(row)
                print row
		#f.close()
        return str(elist)

    def connect_mssql(self)
        CONNECTION_STRING="""
        Driver={SQL Server Native Client 11.0};
        Server=localhost\sqlexpress;
        Database=DemoDataBase;
        Trusted_Connection=yes;
        """

        db = pyodbc.connect(CONNECTION_STRING)
        c = db.cursor()
        c.execute ('SELECT * FROM rows')
        rs = c.fetchall()
        for r in rs:
            print "id %d fname %s lname %s "%(r[0],r[1],r[2])
        
		
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
    def open_excel(self):
        #self.xlWb = self.xlApp.Workbooks.Open(self.file_name)    #It finds the workbook
        time.sleep(3)
 
    def open_excel2(self):
        self.xlWb2 = self.xlApp2.Workbooks.Open(self.file_name2)    #It finds the workbook

    def read_excel(self):
        #print ("read_excel %d " )% self.count2
        #self.i=0
        self.xlSht = self.xlWb.Worksheets (1)   #Goes to sheet 1
        dataList = []
        for row_ind in range (1,36 + 1): #self.count2 It goes through the  items in A and B...
            for col in ('A','B','C','D','E','F'):
                if col == 'A':
                    b = self.xlSht.Cells(row_ind,col)
                    b = int(b)
                    dataList.append(b)
                elif col == 'E':
                    x = self.xlSht.Cells(row_ind,col)
                    x = time.strftime('%Y-%m-%d')
                    dataList.append(x)
                    self.status = 1
                elif col == 'F':
                    y = self.xlSht.Cells(row_ind,col)
                    c = self.convertStr(str(y))
                    dataList.append(self.convert_excel_time(c,hour24=False))
                else:
                    dataList.append(self.xlSht.Cells(row_ind,col))


        #print (dataList[0])
        self.val = dataList[self.i]
        self.val2 = self.val
            #print ("i:n arvo %d ") %self.i
            #print str(self.val)
        self.i = self.i + 1

        #print "value is {0} ".format(self.val)
        return str(self.val) #palautetaan excelista luettu solun arvo

#######################################################################
    def read_excel2(self):
        #print ("read_excel %d " )% self.count2
        #self.i=0
        self.xlSht2 = self.xlWb2.Worksheets (1)   #Goes to sheet 1
        dataList = []
        for row_ind in range (1,36 + 1): #self.count2 It goes through the  items in A and B...
            for col in ('A','B','C','D','E','F'):
                if col == 'A':
                    b = self.xlSht2.Cells(row_ind,col)
                    b = int(b)
                    dataList.append(b)
                elif col == 'E':
                    x = self.xlSht2.Cells(row_ind,col)
                    x = time.strftime('%Y-%m-%d')
                    dataList.append(x)
                    self.status = 1
                elif col == 'F':
                    y = self.xlSht2.Cells(row_ind,col)
                    c = self.convertStr(str(y))
                    dataList.append(self.convert_excel_time(c,hour24=False))
                else:
                    dataList.append(self.xlSht2.Cells(row_ind,col))


        #print (dataList[0])
        self.val2 = dataList[self.z]
            #print ("i:n arvo %d ") %self.i
            #print str(self.val)
        self.z = self.z + 1

        #print "value is {0} ".format(self.val)
        return str(self.val2) #palautetaan excelista luettu solun arvo
#######################################################################

    def close_excel_by_force(self,excel):
        import win32process
        import win32gui
        import win32api
        import win32con

        # Get the window's process id's
        hwnd = excel.Hwnd
        t, p = win32process.GetWindowThreadProcessId(hwnd)
        # Ask window nicely to close
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        # Allow some time for app to close
        time.sleep(10)
        # If the application didn't close, force close
        try:
            handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, p)
            if handle:
                win32api.TerminateProcess(handle, 0)
                win32api.CloseHandle(handle)
        except:
            pass

    def close_excel(self): ##solve this TODO
        import os
        os.system('taskkill /f /im Excel.exe')
        close_excel_by_force(self.xlApp) 

    def close_excel2(self): ##solve this TODO
        import os
        os.system('taskkill /f /im Excel.exe')
        close_excel_by_force(self.xlApp2)

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

    def register_keyword_to_run_on_failure(self, keyword):
        """Documentation here....
        """
        old_keyword = self._run_on_failure_keyword
        old_keyword_text = old_keyword if old_keyword is not None else "No keyword"

        if keyword:
            new_keyword = keyword if keyword.strip().lower() != "nothing" else None
        else:
            new_keyword = None
        new_keyword_text = new_keyword if new_keyword is not None else "No     keyword"

        self._run_on_failure_keyword = new_keyword
        self._info('%s will be run on failure.' % new_keyword_text)

        return old_keyword

    def check_length(self,arg):
        if arg == 'None':
            raise AssertionError("Expected Length to > 0 but was text %s "%arg)

    def two_values(self, val1, val2):
        if val1 == val2:
            return "Values are same {0}  {1}".format(val1,val2)
        else:
            raise AssertionError("Values doesn't match, %s is different than %s "%(val1,val2))

    def batch_file(self):
        import subprocess
        import os
        #os.system("KillExcel.bat")
        self.filepath="C:/Users/Timo/Desktop/Robot Framework/Robot Framework/mysql_connection/KillExcel.bat"
        self.p = subprocess.Popen(self.filepath, shell=True, stdout = subprocess.PIPE)
        stdout, stderr = self.p.communicate()
        print self.p.returncode # is 0 if success



OBJECT = Mysql()
#time.sleep(3)
#os.system("C:/Users/Timo/Desktop/Robot Framework/Robot Framework/mysql_connection/KillExcel.bat")
filepath="C:/Users/Timo/Desktop/Robot Framework/Robot Framework/mysql_connection/KillExcel.bat"
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
stdout, stderr = p.communicate()
print p.returncode # is 0 if success
#OBJECT.batch_file
print "Excel files are closed"
#OBJECT.close_excel2
#OBJECT.vertaa("Timo","Matti")                                
#luku = OBJECT.get_range()
#print luku
#OBJECT.connect(0) #0 excel table is done, 1 excel table generated
#OBJECT.mysql_read(0) #0 excel table is done, 1 excel table generated
#OBJECT.open_excel
#print "Excel files are open"
#time.sleep(5)
#OBJECT.open_excel2
#print "Excel file2 is open"
#time.sleep(5)
#for x in range (36-1):
#    OBJECT.read_excel()
#OBJECT.batch_file
#print "Excel files are closed"
#OBJECT.close_excel()
#DICTIONARY = { 1: 'one', 2: 'two', 3: 'three'}

#jos luokka ja module nimi on sama riittaa vain RIDE MyObject
#jos ovat eri niin module.MyObject
