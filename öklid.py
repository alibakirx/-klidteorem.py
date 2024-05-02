import math

def euclideanDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def main():
    x1 = int(input("x1 değerini giriniz: "))
    x2 = int(input("x2 değerini giriniz: "))
    y1 = int(input("y1 değerini giriniz: "))
    y2 = int(input("y2 değerini giriniz: "))

    distance = euclideanDistance(x1, y1, x2, y2)

    print("İki nokta arasındaki mesafe:", distance)

if __name__ == "__main__":
    main()
