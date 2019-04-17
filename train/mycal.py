class mycal(object):
    def __init__ (self):
        self.result = 0
        self.t = 0
        
    def add(self, num):
        self.t = self.result
        self.result += num
        print("%d + %d = %d" % (self.t,num,self.result) )
        return self.result
    
    def sub(self, num):
        self.t = self.result
        self.result -= num
        print("%d - %d = %d" % (self.t,num,self.result) )
        return self.result
    
    def mul(self, num):
        self.t = self.result
        self.result *= num
        print("%d - %d = %d" % (self.t,num,self.result) )
        return self.result
    
    def div(self, num):
        xxxx = self.result
        self.t = self.result
        self.result /= num
        print("%d - %d = %d" % (xxxx,num,self.result) )
        return self.result
    
    def prt(self):
        print("result= %d" % self.result)
        
    
    def cal(self, x,y):
        self.add = x + y 
        self.sub = x - y  
        self.mul = x * y 
        self.div = x / y  
        return self.add, self.sub, self.mul, self.div  
    
    
c1 = mycal()
c1.add(100)
c1.sub(10)
c1.mul(24)
c1.div(8)

c1.prt()

print ( c1.cal(100,200) )


