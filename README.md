# **Medicas - Service Website Application**

## Introduction:

**Medicas** is a medical service website that provides health counseling support.

This is a course project of **Web-Based Application Development - NT208.M11.ANTT** 

## Features:

**Medicas** supports real-time chat between customers and medical assistants. Customers can choose to connect with specific Medicas doctors based on specialties.

**Medicas** supports Host-side for Medicas doctors and Client-side for customers *(Require sign-in for joining chat room)*.

## Dependencies:

| Language | Framework | Database | 
| ----------- | ----------- | ----------- |
| Python, JS, HTML/CSS | Django 3.2.9 | MSSQL Server |

----
***WARNING*** </br>
By default, the configuration of Django Framework uses SQLite. Instead, Medicas uses the remote MSSQL database server. </br>
To run website, have to connect to Database Server through IP address by adding Database Server's public IP address to `'HOST': '...',` in **settings.py**.

But...THE DATABASE SERVER HAS DOWN 😭 No more connection, no more website running.   

P/s, I gotta reset the database server soon. But not sure when...😶


## References
For more information about configuring MSSQL database, you can read this: </br>
https://github.com/microsoft/mssql-django 
