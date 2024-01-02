#match statement ,which is equals to switch case
x=int(input("Give me a number : "))
match x:
          case 0:
                print("x is 0")
          case 1:
                print("x is 1")
          case 2:
              print("X is 2")
          case 4:
              print("X is 4")
          case _ if (x!=90):
               print(x," Is not 90")