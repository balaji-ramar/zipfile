import os, time, datetime

file = "samples.zip"
print("name:",file)
f=open("samples.zip")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="Directory"
print("file extension:",exten)


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




file = "__MACOSX/samples/utilities/checkpoint/options/table/cuckoo/tools/block_cache_analyzer/logging/java/jmh/src/main/java/org/rocksdb/jmh/memory/include/rocksdb/utilities/lua/test_util/option_change_migration/memtable/._hash_skiplist_rep.cc                                                                                            "
print("name:",file)
f=open("__MACOSX/samples/utilities/checkpoint/options/table/cuckoo/tools/block_cache_analyzer/logging/java/jmh/src/main/java/org/rocksdb/jmh/memory/include/rocksdb/utilities/lua/test_util/option_change_migration/memtable/._hash_skiplist_rep.cc                                                                                            ")
print(os.getcwd())
modified = os.path.getmtime(file)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
print("last modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
created = os.path.getctime(file)
print("Data created:  %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
exten="cc"
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






file = "__MACOSX/samples/._stereor.jpg                                                                                               "
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

























#
#
#
# f.close()

