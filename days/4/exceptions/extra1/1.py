class MyError(Exception):
    def __init__(self, value):
        self.value = value
    
def main():
    try:
        raise MyError(10)
    except MyError as e:
        print 'MyError: value = ', e.value

main()


