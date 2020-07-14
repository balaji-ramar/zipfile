from zipfile import ZipFile
import os, time, datetime
file_name="samples.zip"
z=ZipFile(file_name)

for file in z.infolist():
    print(file,file.file_size,os.getcwd(),os.path.getmtime(file_name),os.path.getctime(file_name),)


#
#
file = "samples.zip"
print("name:",file)
f=open("samples.zip")
print("full path",os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
# #
# #
# #









file = "file.py"
print("name:",file)
f=open("samples.zip")
print("full path",os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))



















import os, time, datetime

file = "samples.zip"
print("name:",file)
f=open("samples.zip")
print("full path",os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))



#
file = "__MACOSX/._samples  "
print("name:",file)
f=open("__MACOSX/._samples  ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)



file = "samples/Gray Wedge 15.tif            "
print("name:",file)
f=open("samples/Gray Wedge 15.tif            ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)

#
#
#
file = "__MACOSX/samples/._Gray Wedge 15.tif     "
print("name:",file)
f=open("__MACOSX/samples/._Gray Wedge 15.tif     ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)



file = "__MACOSX/samples/._ONETOONE.JPG"
print("name:",file)
f=open("__MACOSX/samples/._ONETOONE.JPG                 ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)
#
#
#
#
#
file = "__MACOSX/samples/._.DS_Store                    "
print("name:",file)
f=open("__MACOSX/samples/._.DS_Store                   ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)




file = "__MACOSX/samples/._rhino.jpg                       "
print("name:",file)
f=open("__MACOSX/samples/._rhino.jpg                      ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)




file = "__MACOSX/samples/._Elephants.lyt                          "
print("name:",file)
f=open("__MACOSX/samples/._Elephants.lyt                         ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)

#
#
file = "samples/MTRCYCLE.JPG                                                     "
print("name:",file)
f=open("samples/MTRCYCLE.JPG                                                    ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)





file = "__MACOSX/samples/._MTRCYCLE.JPG                                                       "
print("name:",file)
f=open("__MACOSX/samples/._MTRCYCLE.JPG                                                      ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)




file = "samples/blob_file.cc                                                                                  "
print("name:",file)
f=open("samples/blob_file.cc                                                                                 ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)





file = "samples/leafmask.jpg                                                                                      "
print("name:",file)
f=open("samples/leafmask.jpg                                                                                     ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)





file = "samples/ROAD.JPG                                                                                       "
print("name:",file)
f=open("samples/ROAD.JPG                                                                                      ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)




file = "__MACOSX/samples/._ROAD.JPG                                                                                          "
print("name:",file)
f=open("__MACOSX/samples/._ROAD.JPG                                                                                         ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)




file = "samples/Fisheye.jpg                                                                                           "
print("name:",file)
f=open("samples/Fisheye.jpg                                                                                           ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)




file = "samples/Bottles.jpg                                                                                           "
print("name:",file)
f=open("samples/Bottles.jpg                                                                                           ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)




file = "__MACOSX/samples/tools/._CMakeLists.txt                                                                                            "
print("name:",file)
f=open("__MACOSX/samples/tools/._CMakeLists.txt                                                                                            ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="txt"
print("file extension:",exten)




file = "__MACOSX/samples/._rhino.jpg                                                                                             "
print("name:",file)
f=open("__MACOSX/samples/._rhino.jpg                                                                                             ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)






file = "__MACOSX/samples/._MTRCYCLE.JPG                                                                                              "
print("name:",file)
f=open("__MACOSX/samples/._MTRCYCLE.JPG                                                                                              ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)


#
#
#
#
file = "__MACOSX/samples/._stereor.jpg                                                                                           "
print("name:",file)
f=open("__MACOSX/samples/._stereor.jpg                                                                                               ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)




file = "__MACOSX/samples/._PRPLFLWR.JPG                                                                                                "
print("name:",file)
f=open("__MACOSX/samples/._PRPLFLWR.JPG                                                                                                ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)





file = "__MACOSX/samples/._bird.jpeg                                                                                                 "
print("name:",file)
f=open("__MACOSX/samples/._bird.jpeg                                                                                                 ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpeg"
print("file extension:",exten)




file = "__MACOSX/samples/._TOWER.JPG                                                                                                  "
print("name:",file)
f=open("__MACOSX/samples/._TOWER.JPG                                                                                                  ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpeg"
print("file extension:",exten)




file = "__MACOSX/samples/._utilities                                                                                                   "
print("name:",file)
f=open("__MACOSX/samples/._utilities                                                                                                   ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpeg"
print("file extension:",exten)




file = "__MACOSX/samples/._PYRAMID.JPG                                                                                                    "
print("name:",file)
f=open("__MACOSX/samples/._PYRAMID.JPG                                                                                                    ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="JPG"
print("file extension:",exten)




file = "__MACOSX/samples/util/._status.cc                                                                                                     "
print("name:",file)
f=open("__MACOSX/samples/util/._status.cc                                                                                                     ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="JPG"
print("file extension:",exten)



file = "__MACOSX/samples/util/._concurrent_task_limiter_impl.h                                                                                                    "
print("name:",file)
f=open("__MACOSX/samples/util/._concurrent_task_limiter_impl.h                                                                                                     ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="h"
print("file extension:",exten)








file = "__MACOSX/samples/util/._concurrent_task_limiter_impl.h                                                                                                    "
print("name:",file)
f=open("__MACOSX/samples/util/._concurrent_task_limiter_impl.h                                                                                                     ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="JPG"
print("file extension:",exten)





file = "samples/Macbeth Chrome 2000 D50.TIF                                                                                                      "
print("name:",file)
f=open("samples/Macbeth Chrome 2000 D50.TIF                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="TIF"
print("file extension:",exten)






file = "samples/blob_db_listener.h                                                                                                     "
print("name:",file)
f=open("samples/blob_db_listener.h                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="h"
print("file extension:",exten)




file = "samples/blob_db_listener.h                                                                                                     "
print("name:",file)
f=open("samples/blob_db_listener.h                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="h"
print("file extension:",exten)








file = "__MACOSX/samples/._bird.jpeg                                                                                                "
print("name:",file)
f=open("__MACOSX/samples/._bird.jpeg                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpeg"
print("file extension:",exten)





file = "samples/ARCHMASK.JPG                                                                                                "
print("name:",file)
f=open("samples/ARCHMASK.JPG                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="JPG"
print("file extension:",exten)




file = "samples/stereol.jpg                                                                                                "
print("name:",file)
f=open("samples/stereol.jpg                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="jpg"
print("file extension:",exten)




file = "__MACOSX/samples/tools/._write_external_sst.sh                                                                                                "
print("name:",file)
f=open("__MACOSX/samples/tools/._write_external_sst.sh                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="sh"
print("file extension:",exten)




file = "__MACOSX/samples/tools/._ldb_tool.cc                                                                                                "
print("name:",file)
f=open("__MACOSX/samples/tools/._ldb_tool.cc                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="cc"
print("file extension:",exten)




file = "__MACOSX/samples/tools/._check_all_python.py                                                                                                "
print("name:",file)
f=open("__MACOSX/samples/tools/._check_all_python.py                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="py"
print("file extension:",exten)






file = "samples/util/xxhash.cc                                                                                               "
print("name:",file)
f=open("samples/util/xxhash.cc                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="cc"
print("file extension:",exten)




































































































file="__MACOSX/samples/util/._hash_map.h"
print("name:",file)
f=open("__MACOSX/samples/util/._hash_map.h                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="h"
print("file extension:",exten)





file="samples/util/thread_list_test.cc"
print("name:",file)
f=open("samples/util/thread_list_test.cc                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="cc"
print("file extension:",exten)


file="__MACOSX/samples/util/._work_queue_test.cc"
print("name:",file)
f=open("__MACOSX/samples/util/._work_queue_test.cc                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="cc"
print("file extension:",exten)





file="samples/util/string_util.h"
print("name:",file)
f=open("samples/util/string_util.h                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="h"
print("file extension:",exten)





file="samples/utilities/checkpoint/memtable/memtablerep_bench.cc"
print("name:",file)
f=open("samples/utilities/checkpoint/memtable/memtablerep_bench.cc                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="cc"
print("file extension:",exten)



file="samples/utilities/checkpoint/memtable/skiplist.h"
print("name:",file)
f=open("samples/utilities/checkpoint/memtable/skiplist.h                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="cc"
print("file extension:",exten)



#
file="__MACOSX/samples/utilities/checkpoint/memtable/._vectorrep.cc"
print("name:",file)
f=open("__MACOSX/samples/utilities/checkpoint/memtable/._vectorrep.cc                                                                                                        ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="cc"
print("file extension:",exten)








# f.close()

