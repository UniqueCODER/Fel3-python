import math


def rad():
    r = int(input("Input radius: "))
    return r


def ab():
    a = int(input("1st value"))
    b = int(input("2nd value"))
    return a, b


def circle():
    r = rad()
    a = math.pi * r ** 2
    sa = 4 * a
    print('Area of Circle:', a, '\nSurface Area:', sa, '\nDiameter:', r * 2)


def rightTriangle():
    a = ab()
    c = math.sqrt(a[0] ** 2 + a[1] ** 2)
    print('a² = ', a[0], '\nb² =', a[1])
    print('Hypotenuse of a Right triangle ', c)




def triangle():
    t = ab()
    at = .5 * (t[0] * t[1])
    print('base: ', t[0], '\nheight: ', t[1])
    print("Area of Triangle", at)


def cylinder():
    cy = ab()
    r = cy[0] ** 2
    h = cy[1]
    volume = math.pi * r * h
    print('radius:', cy[0], '\nheight', h)
    print('Volume of Cylinder:', volume)


def sphere():
    sp = rad()
    volume = float(4 / 3 * math.pi * (sp ** 3))
    print("radius:", sp)
    print('Volume of sphere:', volume)


def pyramid():
    py = ab()
    a = py[0]
    h = py[1]
    surface = (a**2)+(a*2)*math.sqrt(((a**2)/4)+h**2)
    print('area:', a, '\nheight: ', h)
    print('Surface area of right pyramid:', surface)


def calculation(val):
    switcher = {
        1: circle,
        2: rightTriangle,
        3: triangle,
        4: cylinder,
        5: sphere,
        6: pyramid

    }
    func = switcher.get(val, lambda: 'Invalid')
    return func()


print("Jarilla, Ellysa Kaye Q. | BSCS GARDNER,CAINTA")
calculation(
    int(input("1:Circle\n2:Right Triangle hypothenuse\n3:Triangle\n4:Cylinder\n5:Sphere\n6:Right Pyramid\n Choice:")))
