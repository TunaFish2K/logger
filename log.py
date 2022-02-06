import datetime,py_lambda
from types import FunctionType

class LogWarn(Exception):
    pass

class LogLevel:
    def __init__(self,name,do_raise=False):
        self.name=name
        self.do_raise=do_raise
    def raise_log(self):
        if self.do_raise:
            raise LogWarn("log level {name} raise".format(name=self.name))

default_levels={
            "info":LogLevel("INFO"),
            "warning":LogLevel("WARNING"),
            "error":LogLevel("ERROR",True)
        }

class Logger:
    def __init__(self,pattern:str="[{time}/{type}]: {log}") -> None:
        self.pattern=pattern
        self.log_stream=[]
        self.favour={}
    def add_stream(self,stream):
        self.log_stream.append(stream)
    def remove_stream(self,stream):
        self.log_stream.remove(stream)
    def list_stream(self):
        return self.log_stream
    def remove_all_stream(self):
        self.log_stream.clear()
    def log(self,log:str,level:LogLevel=default_levels["info"]):
        time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        format_favour={}
        for k,v in self.favour.items():
            format_favour[k]=v()
        log_text=self.pattern.format(time=time,type=level.name,log=log,**format_favour)
        for i in self.log_stream:
            i.write(log_text+"\n")
            i.flush()
               
        level.raise_log()
    def __setitem__(self,key:str,value):
        if not type(value)==FunctionType:
            value=py_lambda.main._def([],"""
    return"""+" "+repr(value))
        self.favour[key]=value
    def __getitem__(self,key:str):
        return self.favour[key]()
    def clear_favour(self):
        self.favour.clear()