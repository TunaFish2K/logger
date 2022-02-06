def _def(args:tuple,code:str):
    scope={}
    build="def _f("+",".join(args)+"):\n"+code
    exec(build,scope)
    return scope["_f"]