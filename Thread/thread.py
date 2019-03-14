import threading
from time import ctime,sleep

def AddThead(threads,funcname,funcele):
    threads=[]
    t = threading.Thread(target=funcname,args=(funcele))
    threads.appeand(t)