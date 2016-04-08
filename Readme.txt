You Can Run this app by following steps:

Windows:

1.python2.7(32bit) Download from python.org
2.mysql sever (32bit) Download from mysql website
3.pip download from website(after install pip,you can easy use 'pip install projectname' to install)
4.Django   'pip install django'
5.django-suit     'pip install django-suit'
6.django-filer    'pip install django-filer'
7.mysql-python and numpy   'pip install mysql-python numpy'(this step will get error if you not install MySQL-python-1.2.4b4.win32-py2.7.exe)
8.install MySQL-python-1.2.4b4.win32-py2.7.exe

TIP:Because the python-win depends on the C++ complier , and you should install the VS2010 EXPRESS(or vs2008) for useing the python2.7
And some others configure below：
Edit the system EvironmentVarible
new VS90COMNTOOLS ,and the value is  %VS100COMNTOOLS%
or simple go to cmd line input :
SET VS90COMNTOOLS=%VS100COMNTOOLS%

Finally you should change the zhengzihui/setting.py the databaseinfo which match to your own setting
(change the psw of connecting the mysql and create the zhengzihui_test_second DATABASE if not exist)

then 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver