# import important libraries
import os
import shutil
import send2trash

# directory variables
maindir = "/xxxx/xxxxx"
docdir = "/yyyy/yyy/_docs/"
datadir = "/zzzzz/_data/"
codedir = "/wwww/wwww/_code/"
pptdir = "/aaa/aaaaaa/_presentations/"
dldir = "/bbbbbbbb/Downloads"
doc2dir = "/cccc/cccc/Documents"
dskdir = "/ddddddd/Desktop"
picdir = "/eee/eeee/Pictures/"

#---------- documents

# move document files in main folder into _documents folder

print("Moving documents in main folder into documents folder ...")

docs = ("doc", "docx", "txt", "pdf", "rtf", ".md", ".htm", ".html")

for filename in os.listdir(maindir):
    if filename.endswith(docs):
        shutil.move(os.path.join(maindir, filename), os.path.join(docdir, filename))


# move document files in downloads folder into _documents folder

print("Moving documents in downloads folder into documents folder ...")

docs = ("doc", "docx", "txt", "pdf", "rtf", ".md", ".htm", ".html")

for filename in os.listdir(dldir):
    if filename.endswith(docs):
        shutil.move(os.path.join(dldir, filename), os.path.join(docdir, filename))


# move document files in Documents folder into _documents folder

print("Moving documents in Documents into documents folder ...")

docs = ("doc", "docx", "txt", "pdf", "rtf", ".md", ".htm", ".html")

for filename in os.listdir(doc2dir):
    if filename.endswith(docs):
        shutil.move(os.path.join(doc2dir, filename), os.path.join(docdir, filename))


# move document files in Desktop folder into _documents folder

print("Moving documents in Desktop folder into documents folder ...")

docs = ("doc", "docx", "txt", "pdf", "rtf", ".md", ".htm", ".html")

for filename in os.listdir(dskdir):
    if filename.endswith(docs):
        shutil.move(os.path.join(dskdir, filename), os.path.join(docdir, filename))

print("\n")
print("DOCUMENT CLEANUP COMPLETE!")
print("\n")

#---------- data

# move data files from main folder to data folder

print("Moving csv, xls, xlsx files in main folder into data folder ...")

data = ("csv", "xls", "xlsx")

for filename in os.listdir(maindir):
    if filename.endswith(data):
        shutil.move(os.path.join(maindir, filename), os.path.join(datadir, filename))


# move data files from Desktop into data folder

print("Moving csv, xls, xlsx files in Desktop folder into data folder ...")

data = ("csv", "xls", "xlsx")

for filename in os.listdir(dskdir):
    if filename.endswith(data):
        shutil.move(os.path.join(dskdir, filename), os.path.join(datadir, filename))


# move data files from download folder to data folder

print("Moving csv, xls, xlsx files in Downloads folder into data folder ...")

data = ("csv", "xls", "xlsx")

for filename in os.listdir(dldir):
    if filename.endswith(data):
        shutil.move(os.path.join(dldir, filename), os.path.join(datadir, filename))


# move data files from Documents to data folder

print("Moving csv, xls, xlsx files in Documents folder into data folder ...")

data = ("csv", "xls", "xlsx")

for filename in os.listdir(doc2dir):
    if filename.endswith(data):
        shutil.move(os.path.join(doc2dir, filename), os.path.join(datadir, filename))

print("\n")
print("DATA CLEANUP COMPLETE!")
print("\n")

#---------- pictures

# move picture files from Desktop into pics folder

print("Moving png, jpg, jpeg in Desktop folder into pics folder ...")

pics = (".png", ".jpg", ".jpeg", ".gif")

for filename in os.listdir(dskdir):
    if filename.endswith(pics):
        shutil.move(os.path.join(dskdir, filename), os.path.join(picdir, filename))


# move picture files from main folder to pics folder

print("Moving png, jpg, jpeg in main folder into pics folder ...")

pics = (".png", ".jpg", ".jpeg", ".gif")

for filename in os.listdir(maindir):
    if filename.endswith(pics):
        shutil.move(os.path.join(maindir, filename), os.path.join(picdir, filename))


# move picture files from Downloads into pics folder

print("Moving png, jpg, jpeg in Downloads folder into pics folder ...")

pics = (".png", ".jpg", ".jpeg", ".gif")

for filename in os.listdir(dldir):
    if filename.endswith(pics):
        shutil.move(os.path.join(dldir, filename), os.path.join(picdir, filename))


# move picture files from Documents into pics folder

print("Moving png, jpg, jpeg in Documents folder into pics folder ...")

pics = (".png", ".jpg", ".jpeg", ".gif")

for filename in os.listdir(doc2dir):
    if filename.endswith(pics):
        shutil.move(os.path.join(doc2dir, filename), os.path.join(picdir, filename))

print("\n")
print("PICTURE CLEANUP COMPLETE!")
print("\n")

#---------- presentations

# move ppt files from main folder into presentations folder

print("Moving ppt, pptx, pps files in main folder into presentations folder ...")

ppt = ("ppt", "pptx", "pps")

for filename in os.listdir(maindir):
    if filename.endswith(ppt):
        shutil.move(os.path.join(maindir, filename), os.path.join(pptdir, filename))


# move ppt files from desktop into presentations folder

print("Moving ppt, pptx, pps files in Desktop folder into presentations folder ...")

ppt = ("ppt", "pptx", "pps")

for filename in os.listdir(dskdir):
    if filename.endswith(ppt):
        shutil.move(os.path.join(dskdir, filename), os.path.join(pptdir, filename))


# move ppt files from downloads into presentations folder

print("Moving ppt, pptx, pps files in Downloads folder into presentations folder ...")

ppt = ("ppt", "pptx", "pps")

for filename in os.listdir(dldir):
    if filename.endswith(ppt):
        shutil.move(os.path.join(dldir, filename), os.path.join(pptdir, filename))


# move ppt files from documents into presentations folder

print("Moving ppt, pptx, pps files in Documents folder into presentations folder ...")

ppt = ("ppt", "pptx", "pps")

for filename in os.listdir(doc2dir):
    if filename.endswith(ppt):
        shutil.move(os.path.join(doc2dir, filename), os.path.join(pptdir, filename))

print("\n")
print("PRESENTATION CLEANUP COMPLETE!")
print("\n")

#---------- code

# code to move analytic files in main folder into coding folder (.r, .py, .ipynb)

print("Moving .r, .rmd, .py, .ipynb files in main folder into code folder ...")

ppt = (".r", ".R", ".Rmd", ".py", ".ipynb")

for filename in os.listdir(maindir):
    if filename.endswith(ppt):
        shutil.move(os.path.join(maindir, filename), os.path.join(codedir, filename))


# code to move analytic files in Desktop folder into coding folder (.r, .py, .ipynb)

print("Moving .r, .rmd, .py, .ipynb files in Desktop folder into code folder ...")

ppt = (".r", ".R", ".Rmd", ".py", ".ipynb")

for filename in os.listdir(dskdir):
    if filename.endswith(ppt):
        shutil.move(os.path.join(dskdir, filename), os.path.join(codedir, filename))

print("\n")
print("CODE CLEANUP COMPLETE!")
print("\n")

#---------- trash

# code to move zip files to the trash folder

# move zip, dmg, gz, tgz, ica, pkg files in download folder to the trash folder

print("Moving .zip, .dmg, .gz, .tgz, .ica, .pkg files in Downloads folder into trash folder ...")

dnl = (".zip", ".dmg", ".gz", ".tgz", ".ica", ".pkg")

for filename in os.listdir(dldir):
    if filename.endswith(dnl):
        send2trash.send2trash(os.path.join(dldir, filename))

print("\n")
print("APP/PACKAGE DOWNLOADS CLEANUP COMPLETE!")
print("\n")
