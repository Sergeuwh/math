import math
b = 0
xf = -999
xs = -999
while True:
    choice = input(("1/2 "))
    inp = input("a x + b x + c ") #-10 x - 3 x - 89
    if int(choice) == int(2):
        print("Свойства квадратичной функции:")
        a = float(str(inp[0:str(inp).find("x")]).replace(" ", ""))
        #print("a:", a) #
        b = float(str(inp[str(inp).find("x")+2: str(inp).rfind("x")]).replace(" ", ""))
        #print("b:",b) #
        c = float(inp[str(inp).rfind("x")+1::].replace(" ", ""))
        #print("c:",c) #
        #print("1. D(y) = R")
        xv = -1 * (b/ (2 * a))
        znak_f = inp[inp.find("x")+2: inp.find("x")+3]
        znak_s = inp[inp.rfind("x")+2: inp.rfind("x")+3]
        print("xv:",xv)
        yv = (a*(xv**2))+(b*xv)+c
        print("yv:",yv)
        if a > 0:
            vv = "[" + str(yv) + "; " + "+" + "∞" + ")"
            print("2. E(y) = ", vv)
            print("Ветви параболы направлены- вверх; т.к. а > 0")
            print("3. yнаим = ", yv)
        else:
            vv = "(" + "-∞" + "; " + str(yv) + "]"
            print("2. E(y) = ", vv)
            print("Ветви параболы направлены- вниз; т.к. а < 0")
            print("3. yнаиб = ", yv)
        print("4. Нули функции:")
        d = (b ** 2) - 4*a*c
        print("d:", d)
        if d > 0:
            xf = (-1 * (b) - math.sqrt(d)) / (2 * a)
            print("xf:", xf)
            xs = (-1 * (b) + math.sqrt(d)) / (2 * a)
            print("xs:", xs)
        elif d == 0:
            xf = xv
            print("xf:", xf)
        else:
            print("Не имеет корней")
        if a > 0:
            if xf != -999:
                if xf < xs:
                    print("5. y > 0 при x ∈(-∞;", xf, ") ∪ (", xs, ";+∞)")
                    print("5. y < 0 при x ∈(", xf, ";", xs, ")")
                else:
                    print("5. y > 0 при x ∈(-∞;", xs, ") ∪ (", xf, ";+∞)")
                    print("5. y < 0 при x ∈(", xs, ";", xf, ")")
            else:
                print("5. y > 0 при x ∈(-∞;+∞)")
        else:
            if xf != -999:
                if xf < xs:
                    print("5. y > 0 при x ∈(", xf, ";", xs, ")")
                    print("5. y < 0 при x ∈(-∞;", xf, ") ∪ (", xs, ";+∞)")
                else:
                    print("5. y > 0 при x ∈(", xs, ";", xf, ")")
                    print("5. y < 0 при x ∈(-∞;", xs, ") ∪ (", xf, ";+∞)")
            else:
                print("5. y < 0 при x ∈(-∞;+∞)")
    else:
        a = float(str(inp[0:str(inp).find("x")]).replace(" ", ""))
        # print("a:", a) #
        b = float(str(inp[str(inp).find("x") + 2: str(inp).rfind("x")]).replace(" ", ""))
        # print("b:",b) #
        c = float(inp[str(inp).rfind("x") + 1::].replace(" ", ""))
        if a > 0:
            print("1. Ветви параболы направленны- вверх; т.к. а > 0")
        else:
            print("1. Ветви параболы направленны- вниз; т.к. а < 0")
        print("2.")
        xv = -1 * (b / (2 * a))
        print("xv:", xv)
        yv = (a * (xv ** 2)) + (b * xv) + c
        print("yv:", yv)
        print("(", xv, ";", yv, ")-координаты точки вершины параболы")
        print("3. Ось симметрии: x =", xv)
        print("4. Нули функции: y = 0")
        d = (b ** 2) - 4 * a * c
        print("D=",d)
        if d > 0:
            xf = (-1 * (b) - math.sqrt(d)) / (2 * a)
            print("x1:", xf)
            xs = (-1 * (b) + math.sqrt(d)) / (2 * a)
            print("x2:", xs)
        elif d == 0:
            xf = xv
            print("x1:", xf)
        else:
            print("Не имеет корней")
        print("5. Точка пересечения графика функции с осью оу:")
        print("x = 0.0 \ny =", (a*0)+(b*0)+c)
        print("(0.0;", (a*0)+(b*0)+c, ")-координаты точки пересечения с осью оу")
        print("(", 2*xv, ";", (a*0)+(b*0)+c, ")-координаты точки сииметричной данной")


    break
