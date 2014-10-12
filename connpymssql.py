# -*- coding: utf-8 -*-
import pyodbc


def mssql(query,find):
    CONNECTION_STRING="""
    Driver={SQL Server Native Client 11.0};
    Server=localhost\sqlexpress;
    Database=DemoDataBase;
    Trusted_Connection=yes;
    """
    f = int(find)
    db = pyodbc.connect(CONNECTION_STRING)
    c = db.cursor()
    c.execute (query)
    rs = c.fetchall()
    for r in rs:
        #print "id %d fname %s lname %s "%(r[0],r[1],r[2])
        if r[0] == f:
            db.close()
            return r

#print mssql("select *from rows",3)
