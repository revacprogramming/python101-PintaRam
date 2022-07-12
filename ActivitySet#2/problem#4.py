def get_string():
    """get string input"""
    string=str(input("Enter the string :"))
    return string

def str_to_lst(str):
    """convert connected string to list of strings"""
    l=[]  #l=list()
    spt=str.split(';')
    '''if '' in spt:
      spt.remove('')'''
    for wrd in spt:
      wrd=wrd.split('=')
      t=tuple(wrd)
      l.append(t)
      #print(len(l))
    return l
  
def lst_to_str(lst):
    """convert list of strings to connected string"""
    '''str=''
    for i in lst:
      str+=i
    return str'''
  
    str=""
    l=[]
    for wrd in lst:
      l.append(wrd)
    for i in l:
      #print(i[0],i[1],i[-2])
      str+=i[0]+'='+i[1]+';'
   
    return str
  
print(f"Present Directory/__name__ == {__name__}")
def main():
    name=get_string()
    list=str_to_lst(name)
    string=lst_to_str(list)
    print(list)
    print(string)

if __name__ == '__main__':
    main()


'''for t in lot:
        if t == lot[(len(lot)-1)]:
            a = a+t[0]+'='+t[1]
            continue
        a = a+t[0]+'='+t[1]+';'
    return a'''

