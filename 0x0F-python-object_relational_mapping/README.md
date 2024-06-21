# Python - Object-relational mapping - ORM
ORMs help us automate the transfer of data stored in relational database tables into objects that are more commonly used in applications.

This directory contains script files that shows how that is done in Python.

## FEATURES
The following are different actions performed on RDB using ORMs:
* retrieving data from the tables
 * retrieving specific value
 * retrieving data the matches a pattern
 * retrieving based on cities, states 
* SQL injection
* retrieving data using SQLAlchemy
* updating data
* deleting data
* inserting data

## How to Run
* Install the needed packages - ubuntu users
  * Python virtual environment
  ``` bash
    $ sudo apt update
    $ sudo apt-get install python3-venv
    $ python3 -m venv <venv_name>
    $ source <venv_name>/bin/activate
  ```
  * Install MySQLdb module
  ``` bash
    $ sudo apt-get install python3-dev
    $ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
  ```
  * Install SQLAlchemy module
  ```
    $ install pip
    $ sudo pip3 install SQLAlchemy
  ```
* create and execute your database script:  `cat <your_script>.sql | mysql -u <user> -p`
* `./0-select_states.py <user> <password> hbtn_0e_0_usa`
