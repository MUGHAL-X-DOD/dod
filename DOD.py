import os,platform
os.system('git pull')

dod=platform.architecture()[0]
if dod=="32bit":
    print('Sorry 32 Bit Not Saported...')
elif dod=="64bit":
    __import__("xd")
