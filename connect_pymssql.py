# -*- coding: utf-8 -*-
import pyodbc


def connect_to_mssql()
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
