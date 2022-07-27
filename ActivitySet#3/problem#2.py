class student:
    def __init__(self , dict , n):
        self.dict = dict;
        self.n =n;
        #i = 1;
        #while(i<n):
        for i in range(1,n+1):
            self.name = input(f"enter the name of students{i}  : ");
            self.height = float(input(f"enter the  height of {self.name} : "));
            self.age = int(input(f"enter the age of {self.name} : "));
            dict.update({self.name : self.height});
            #i+=1;
        
class section(student):
    def __init__(self ,n  , dict):
        self.n = n;
        self.dict =dict;
    
    def find_tallest(self,dict):
        self.big = 0;
        for self.i in dict.values():
            if  self.i > self.big:
                self.big = self.i ;
        
    def find_index_of_list(self,dict):
        self.index = list(dict.values()).index(self.big)
        
            
    def output(self ,lst):
        self.lst = lst;
        print(f"The name of the tallest student among all  the students in a section  is {self.lst[self.index]} whose height is {(self.big)} ");
         
        
def main():        
    n =int(input("enter the no of students: "));
    dict = {}
    obj = student(dict , n);
    lst = list(dict.keys())
    obj2 = section(n , dict);
    obj2.find_tallest(dict);
    obj2.find_index_of_list(dict)
    obj2.output(lst)
main ()



