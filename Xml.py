# -*- coding: utf8 -*-
from win32com.client import Dispatch
import xml.dom.minidom as minidom
from xml.dom.minidom import parse
document = 'example.xml' 
#----------------------------------------------------------------------
class Xml():
    
    def __init__(self):
        self.arvot0 = ""
        self.val = ""
        self.i = 0
        self.k = 0
        self.count = 0
        self.count2 = 0
        self.x = 1
        self.y = 1
        self.z = 1
        self.stat = 0
        #C:\Users\timo\Desktop\excel_files
        file_name =  'C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\xml_data.xls'
        #self.xlApp = win32.gencache.EnsureDispatch('Excel.Application')
        self.xlApp = Dispatch ("Excel.Application")   #Calls for Excel
        self.xlApp.Visible = 1
        self.xlWb = self.xlApp.Workbooks.Open(file_name)    #It finds the workbook
        self.xlSht = self.xlWb.Worksheets("Sheet1")
        self.xlSht.Columns.AutoFit()

    def get_rows(self): #return count of used rows
        used = self.xlApp.ActiveWorkbook.Sheets("Sheet1").UsedRange
        nrows = used.Row + used.Rows.Count - 1
        ncols = used.Column + used.Columns.Count - 1
        cells = nrows * ncols
        #print cells
        return nrows #palautetaan excel taulukossa kaytossa olevien rivien määrä

    def get_cells(self): #return count of used cells
        used = self.xlApp.ActiveWorkbook.Sheets("Sheet1").UsedRange
        nrows = used.Row + used.Rows.Count - 1
        ncols = used.Column + used.Columns.Count - 1
        cells = nrows * ncols
        #print cells
        return cells #palautetaan excel taulukossa kaytossa olevien rivien määrä

    def read_xmlExcel(self):
        #print ("read_excel %d " )% self.count2
        #self.i=0
        #rows = self.get_rows()
        row = self.get_rows()
        self.xlSht = self.xlWb.Worksheets (1)   #Goes to sheet 1
        dataList = []
        for row_ind in range (1,row+1): #It goes through the  items in A and B...
            for col in ('A','B','C','D'):
                dataList.append(self.xlSht.Cells(row_ind,col))
        #print (dataList[0])
        self.val = dataList[self.i]
            #print ("i:n arvo %d ") %self.i
            #print str(self.val)
        self.i = self.i + 1
        return str(self.val) #palautetaan excelista luettu solun arvo

    def Read_Dates(self):
        #from win32com.client import Dispatch
        #xlApp = Dispatch ("Excel.Application") #Calls for Excel
        #xlWb = xlApp.Workbooks.Open('IT.xls') #It finds the workbook
        #xlSht = xlWb.Worksheets (1) Goes to sheet 1
        row = self.get_rows()
        self.xlSht = self.xlWb.Worksheets (1)   #Goes to sheet 1
        dataList = []
        for row in range (1,row+1): #It goes through the 198 items in A and B
            for col in ('D'):
                dataList.append(self.xlSht.Cells(row,col))
        self.val = dataList[self.k]
        self.k = self.k + 1
        for item in dataList:
            print item
        return str(self.val)
    
    def getTitles(self,xml):
        """
        Print out all titles found in xml
        """
        doc = minidom.parse(xml)
        node = doc.documentElement
        books = doc.getElementsByTagName("book")

        titles = []
        genres = []
        authors = []
        for book in books:
            titleObj = book.getElementsByTagName("title")[0]
            titleObj2 = book.getElementsByTagName("genre")[0]
            titleObj3 = book.getElementsByTagName("author")[0]
            titles.append(titleObj)
            genres.append(titleObj2)
            authors.append(titleObj3)

        for author in authors:
            nodes = author.childNodes
            for node in nodes:
                if node.nodeType == node.TEXT_NODE:
                    data = node.data
                    self.write_xmlExcel(data,self.stat)
                    print node.data
        self.stat = self.stat + 1

                    
        for title in titles:
            nodes = title.childNodes
            for node in nodes:
                if node.nodeType == node.TEXT_NODE:
                    data = node.data
                    self.write_xmlExcel(data,self.stat)
                    print node.data
        self.stat = self.stat + 1

        for genre in genres:
            nodes = genre.childNodes
            for node in nodes:
                if node.nodeType == node.TEXT_NODE:
                    data = node.data
                    self.write_xmlExcel(data,self.stat)
                    print node.data

    def write_xmlExcel(self,nod,status):
        if status == 0:
            self.xlApp.Worksheets("Sheet1").Range("A%d"%self.x).Value = str(nod)
            self.x = self.x + 1
        elif status == 1:
            self.xlApp.Worksheets("Sheet1").Range("B%d"%self.y).Value = str(nod)
            self.y = self.y + 1
        elif status >= 2:
            self.xlApp.Worksheets("Sheet1").Range("C%d"%self.z).Value = str(nod)
            self.z = self.z + 1
        
    def close_xmlExcel(self): ##solve this TODO
        self.xlApp.ActiveWorkbook.Close(SaveChanges=1) # see note 1
        self.xlApp.Quit()
        self.xlApp.Visible = 0 # see note 2
        del self.xlApp

    def get_element(self,tagname,ind):
        index = int(ind)
        doc = parse('C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\example.xml')
        node = doc.getElementsByTagName(tagname)
        #for i in node: #print all values
        #    print " ".join(t.nodeValue for t in i.childNodes if t.nodeType == t.TEXT_NODE)
            
        ##print " ".join(t.nodeValue for t in my_node_list[0].childNodes if t.nodeType == t.TEXT_NODE)

        #print "with index number"
        n_node = node[index]
        my_child = n_node.firstChild
        my_text = my_child.data 
        #print my_text
        return my_text

    def replaceText(self,newText, tagname, ind):
        index = int(ind)
        doc = parse('C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\example.xml')
        node = doc.getElementsByTagName(tagname)[index]
        if node.firstChild.nodeType != node.TEXT_NODE:
            raise Exception("node does not contain text")
        node.firstChild.replaceWholeText(newText)
        print doc.toxml()

        # persist changes to save file
        xml_file = open('C:\\Users\\Timo\\Desktop\\Robot Framework\\Robot Framework\\mysql_connection\\example.xml', "w")
        doc.writexml(xml_file, encoding="utf-8")
        xml_file.close()
        
'''
    try:
        node = doc.getElementsByTagName('nodeC')[0]
        replaceText(node, "Hello World")
    except:
        print "error"
        if node.firstChild.nodeType != node.TEXT_NODE:
            raise Exception("node does not contain text")

        node.firstChild.replaceWholeText(newText)'''
        
 
#if __name__ == "__main__":
#    
#xml = Xml()
#el = xml.get_element("title",3)
#newText="New Text"
#xml.replaceText(newText,"title",3)

#print el
#rows = xml.get_rows()
#print rows
#cells = xml.get_cells()
#print cells
#xml.Read_Dates()
#xml.getTitles(document)
#xml.close_xmlExcel()

