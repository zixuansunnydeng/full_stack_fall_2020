def call_twice(fn):
  def wrapper():
    fn()
    fn()
  return wrapper

def hello():
  print('hello')

call_twice(hello)()


@call_twice
def hello2():
  print('helloo')

hello2()

def call_twice_args(fn):
  def wrapper(*args, **kwargs):
    fn(*args, **kwargs)
    fn(*args, **kwargs)
  return wrapper

@call_twice_args
def hello3(name):
  print('hello ' + name)

hello3('sheldon')