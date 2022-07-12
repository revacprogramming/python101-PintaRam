
def get_str():
  """get string input"""
  name=input("Enter the name:")
  return name

def str_to_dict(str):
  """convert connect string to a dictionary"""
  l=[]
  t=tuple()
  str=str.split(';')
  for i in str:
    t=tuple(i.split('='))
    l.append(t)
    dict={wrd[0]:wrd[1] for wrd in l}
    ''' for wrd in l:
    dict={wrd[0]:wrd[1]}
    l.append((dict.items))
    print(list)'''
  #print(dict)
  return dict

def dict_to_str(d):
  """convert a dictionary to connect string"""
  str=''
  for k,v in d.items():
    str+=k+'='+v+';'
  return str
  
def main():
   n=get_str()
   dictionary=str_to_dict(n)
   print(dictionary)
   string=dict_to_str(dictionary)
   print(string)
  

if __name__ == '__main__':
    main()

'''s="a=b;c=d;e=f;g=h"
>>> {(a:=i.split("="))[0]:a[1] for i in s.split(";")}
{'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'}'''