class rectangle:
    def __init__(self):
        self.x1 = float(input("enter the cordinates : "));
        self.y2 = float(input("enter the cordinates : "));
        self.x2 = float(input("enter the cordinates : "));
        self.y2 = float(input("enter the cordinates : "));
        self.x3 = float(input("enter the cordinates : "));
        self.y3 = float(input("enter the cordinates : "));
        
    def calculate(self):
        self.x4 = self.x1;
        self.y4 = self.y3;
        self.a = self.x1 *(self.y2 -self.y4);
        self.b = self.y2* (self.x2 -self.x4);
        self.c = self.x2*self.y4 -self.y2*self.x4;
        self.ar  = 0.5 *(self.a - self.b + self.c);
        self.area  = 2*self.ar;
        
    def output(self):
        print("area of rectangle" , self.area);

ob = rectangle()
#ob.input();
ob.calculate();
ob.output();