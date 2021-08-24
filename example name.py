#python one.py
print('hello')


def func():
    print('FUNC() IN ONE.PY')


def func1():
    pass


def func2():
    pass


print('TOP LEVEL IN ONE.PY')

if __name__ == "__main__": # If __name__ = '__main__' then I'm running this directly
    print('ONE.PY  is being run directly!')
    # RUN THE SCRIPT!
    func1()
    func2()
else:
    print('ONE.PY has been imported!')

