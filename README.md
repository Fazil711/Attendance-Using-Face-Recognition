# Attendance-Using-Face-Recognition

Advance face recognition attendance dashboard for teachers

### Description:

This software is python based and has login form, registeration form and dashboard connected with MySQL server for data waremining

when you run the application a login form appears

![Login](https://user-images.githubusercontent.com/44942652/136942465-f1a2427c-f0c4-4587-9dac-1f7972acb5e5.PNG)

and to use Login you have to register first by clicking on `new user?`

then new form would appear

![Register](https://user-images.githubusercontent.com/44942652/136942756-1fa4bae9-ab48-43bd-9657-fb890151a3ac.PNG)

after registering your info on mysql database from here you can now login from the previous form

and after successfully logging a new dashboard would appear

![Dashboard](https://user-images.githubusercontent.com/44942652/136942966-58752190-c3bc-42d7-bd31-4b82951fee8a.PNG)

Here now you can access the Management system

for managing students click on `student details`

a new form would open

![Student details](https://user-images.githubusercontent.com/44942652/136943352-711155fe-5346-4e54-b4a6-9d6cfee70b23.PNG)

Here you have details of all the students registered and connected to mysql server from here you can include and edit students 
and take their photo by clicking on `take photo` button which would take 100 photos of the student and save it in desired folder 

later to trian the data click on `database` on dashboard then `train` which would train the data and save it in a .xml file

and for taking attendence click on `detect face` which would open webcam and take the info and mark attendence

![detect](https://user-images.githubusercontent.com/44942652/136943988-9b4eb1bf-ee57-426b-a3dd-7515c9a5cc96.PNG)

after marking attendance the file is stored in a .csv file and to import the data from there click on `attendence`

which would run the attendance management window

![Attendance](https://user-images.githubusercontent.com/44942652/136944195-8ce5dd3d-7ad9-4f75-9710-44cbf407d03e.PNG)

from here you can import the .csv file and check, edit attendence

now next is teacher portal for info on teacher's data in mysql 

![Teacher details](https://user-images.githubusercontent.com/44942652/136944457-9b25a47d-3745-4d23-aa8b-72ce345f12ec.PNG)

from here you can see what teachers are there and you can remove or add them based on the system

#### &#128161; Techs & Tools
![](https://img.shields.io/badge/TextEditor-SublimeTxt3-informational?style=flat&logo=data:image/svg%2bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+U3VibGltZSBUZXh0IGljb248L3RpdGxlPjxwYXRoIGQ9Ik0yMS4yNCwxMi4wNmEuNzIuNzIsMCwwLDAtLjQ2LS42NUwxMy40LDkuMDdsNy4zNy0yLjM0YS43My43MywwLDAsMCwuNDctLjY2Vi4zOEEuMzUuMzUsMCwwLDAsMjAuNzcsMEwzLjIzLDUuNThhLjY4LjY4LDAsMCwwLS40Ny42NHY1LjdhLjY1LjY1LDAsMCwwLC40Ni42Mmw3LjQ2LDIuMzdMMy4yMiwxNy4yN2EuNzMuNzMsMCwwLDAtLjQ2LjY2djUuNjlhLjM0LjM0LDAsMCwwLC40Ni4zNmwxNy41Ni01LjU3YS42NS42NSwwLDAsMCwuNDYtLjYyWiIvPjwvc3ZnPg==)
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=data:image/svg%2bxml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgcm9sZT0iaW1nIj48dGl0bGU+UHl0aG9uIGljb248L3RpdGxlPjxwYXRoIGQ9Ik0xNC4zMS4xOGwuOS4yLjczLjI2LjU5LjMuNDUuMzIuMzQuMzQuMjUuMzQuMTYuMzMuMS4zLjA0LjI2LjAyLjItLjAxLjEzVjguNWwtLjA1LjYzLS4xMy41NS0uMjEuNDYtLjI2LjM4LS4zLjMxLS4zMy4yNS0uMzUuMTktLjM1LjE0LS4zMy4xLS4zLjA3LS4yNi4wNC0uMjEuMDJIOC44M2wtLjY5LjA1LS41OS4xNC0uNS4yMi0uNDEuMjctLjMzLjMyLS4yNy4zNS0uMi4zNi0uMTUuMzctLjEuMzUtLjA3LjMyLS4wNC4yNy0uMDIuMjF2My4wNkgzLjIzbC0uMjEtLjAzLS4yOC0uMDctLjMyLS4xMi0uMzUtLjE4LS4zNi0uMjYtLjM2LS4zNi0uMzUtLjQ2LS4zMi0uNTktLjI4LS43My0uMjEtLjg4LS4xNC0xLjA1TDAgMTEuOTdsLjA2LTEuMjIuMTYtMS4wNC4yNC0uODcuMzItLjcxLjM2LS41Ny40LS40NC40Mi0uMzMuNDItLjI0LjQtLjE2LjM2LS4xLjMyLS4wNS4yNC0uMDFoLjE2bC4wNi4wMWg4LjE2di0uODNINi4yNGwtLjAxLTIuNzUtLjAyLS4zNy4wNS0uMzQuMTEtLjMxLjE3LS4yOC4yNS0uMjYuMzEtLjIzLjM4LS4yLjQ0LS4xOC41MS0uMTUuNTgtLjEyLjY0LS4xLjcxLS4wNi43Ny0uMDQuODQtLjAyIDEuMjcuMDUgMS4wNy4xM3ptLTYuMyAxLjk4bC0uMjMuMzMtLjA4LjQxLjA4LjQxLjIzLjM0LjMzLjIyLjQxLjA5LjQxLS4wOS4zMy0uMjIuMjMtLjM0LjA4LS40MS0uMDgtLjQxLS4yMy0uMzMtLjMzLS4yMi0uNDEtLjA5LS40MS4wOS0uMzMuMjJ6TTIxLjEgNi4xMWwuMjguMDYuMzIuMTIuMzUuMTguMzYuMjcuMzYuMzUuMzUuNDcuMzIuNTkuMjguNzMuMjEuODguMTQgMS4wNC4wNSAxLjIzLS4wNiAxLjIzLS4xNiAxLjA0LS4yNC44Ni0uMzIuNzEtLjM2LjU3LS40LjQ1LS40Mi4zMy0uNDIuMjQtLjQuMTYtLjM2LjA5LS4zMi4wNS0uMjQuMDItLjE2LS4wMWgtOC4yMnYuODJoNS44NGwuMDEgMi43Ni4wMi4zNi0uMDUuMzQtLjExLjMxLS4xNy4yOS0uMjUuMjUtLjMxLjI0LS4zOC4yLS40NC4xNy0uNTEuMTUtLjU4LjEzLS42NC4wOS0uNzEuMDctLjc3LjA0LS44NC4wMS0xLjI3LS4wNC0xLjA3LS4xNC0uOS0uMi0uNzMtLjI1LS41OS0uMy0uNDUtLjMzLS4zNC0uMzQtLjI1LS4zNC0uMTYtLjMzLS4xLS4zLS4wNC0uMjUtLjAyLS4yLjAxLS4xM3YtNS4zNGwuMDUtLjY0LjEzLS41NC4yMS0uNDYuMjYtLjM4LjMtLjMyLjMzLS4yNC4zNS0uMi4zNS0uMTQuMzMtLjEuMy0uMDYuMjYtLjA0LjIxLS4wMi4xMy0uMDFoNS44NGwuNjktLjA1LjU5LS4xNC41LS4yMS40MS0uMjguMzMtLjMyLjI3LS4zNS4yLS4zNi4xNS0uMzYuMS0uMzUuMDctLjMyLjA0LS4yOC4wMi0uMjFWNi4wN2gyLjA5bC4xNC4wMS4yMS4wM3ptLTYuNDcgMTQuMjVsLS4yMy4zMy0uMDguNDEuMDguNDEuMjMuMzMuMzMuMjMuNDEuMDguNDEtLjA4LjMzLS4yMy4yMy0uMzMuMDgtLjQxLS4wOC0uNDEtLjIzLS4zMy0uMzMtLjIzLS40MS0uMDgtLjQxLjA4LS4zMy4yM3oiLz48L3N2Zz4=)

![](https://img.shields.io/badge/Library-Tkinter-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Library-mySQL.connector-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Library-Open_CV-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Library-PIL-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Library-CSV-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Library-Open_contrib_CV-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Library-ttk-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)
