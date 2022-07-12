def get_cs():
  name =input("enter the string : ");
  return name;


def cs_to_lot(cs):
    split=  cs.split(';')
    list = [];
    for x in split:
      if(x not in list):
           wrd=x.split('=')
           t=tuple(wrd)
           list.append(t);
    return list;


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main() 



 