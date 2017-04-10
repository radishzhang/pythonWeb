#-*- encoding=UTF-8 -*-

def log(level,*args, **kvargs):
    def inner(func):

        '''
        *args,    有名参数
        **kvargs 无名参数
        '''
        def wrapper(*args, **kvargs):
            print 'before calling',func.__name__
            func(*args, **kvargs)
            print 'end calling',func.__name__
        return wrapper
    return inner

@log(level='INFO')
def hello(name):
    print 'hello',name

if __name__ == '__main__':
    hello('zjf')