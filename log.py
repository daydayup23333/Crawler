import time
import sys
class Log(object):
    def __init__(self,path: str):
        try:
            self.f=open(path, 'w')
        finally:
            pass
    def Wlog(self,text:str,funcname:str):
        try:
            text+=time.asctime(time.localtime(time.time()) )
            funcname+=text
            self.f.write(funcname)
        finally:
            self.f.close()


#封装为此函数，方便调用
def log_run(path,text,funcname):
    L = Log(path)
    L.Wlog(text, funcname)
    return True


if __name__=='__main__':
    L=Log('F:\daydayup\Crawler\\test_log.txt')
    L.Wlog("helloword",sys._getframe().f_code.co_name)