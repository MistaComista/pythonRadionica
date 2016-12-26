class fib:
	def __init__(self):
		self.prev = 0
		self.curr = 1
	
	def __iter__(self):
		print("poziva se iter")
		return self
	
	def __next__(self):
		value = self.curr
		self.curr += self.prev
		self.prev = value
		return value
		
def fibonacci():
    prev, curr = 0, 1
    print("call fibonacci")
    while True:
        print("pre yielda")
        yield curr
        print("posle yielda")
        prev, curr = curr, prev + curr
