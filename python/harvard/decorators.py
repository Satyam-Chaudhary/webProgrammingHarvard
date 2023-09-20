def announce(f):
    def wrapper():
        print('About to run the function...')
        f()
        print('Done with function')
    return wrapper


@announce  # hello function is wrapped inside announce decorator
def hello():
    print('Hello world')

hello()