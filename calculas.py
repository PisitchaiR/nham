"""cal"""
# bottom 4.5 12 55


def calAlAndDi(resultprice, bottle, dict_result):
    print(":::::::alcohol and DI.:::::::")
    result2=0
    name2=""
    while(True):
        name=input("name: ")
        if(name == "end"):
            break
        price=float(input("bath/ml: "))
        number=int(input("number of ml: "))
        result2 += price*number
        name2 += name+" : "+str(price*number)+" bath "+str(number) + " ml"+"\n"
    result="{:.2f}".format((resultprice/3)+bottle+result2)
    print(dict_result+name2+"%s Bath" % result)


def main():
    dict_result=""
    # count = 0
    bottle=55/12
    resultprice=0.0
    while(True):
        name=input("name: ")
        if(name == "end"):
            break
        price=float(input("bath/ml: "))
        number=int(input("number of drop: "))
        cal="{:.2f}".format((price/20)*number)
        dict_result += name+" : "+cal+" bath "+str(number)+" drop"+"\n"
        resultprice += (price/20)*number
    calAlAndDi(resultprice, bottle, dict_result)


main()
