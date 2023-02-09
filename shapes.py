

class Shape:
    def __init__(self, shape, width, length, color):
        self.shape= shape
        self.width= width
        self.length= length
        self.color=color

    print("success")



class Area(Shape):
    def __init__(self, shape, width, length, color):
        super().__init__(shape, width, length, color)

        if self.shape=="rectangle":
            print("Area=", self.shape, self.length*self.width)
       
        elif self.shape=="square":
            print("Area=", self.shape, self.length*self.length)

        print("success2")

class Color(Shape):
    def __init__(self, shape, width, length, color):
        super().__init__(shape,width, length, color)

        print("Color of shape is ",self.color)

        print("success 3")


shape= input("Enter the shape: ")
width= int(input("enter value width or 0: "))
length= int(input("enter value of length or 0: "))
color= input("Enter the color of shape: ")

# obj= Shape(shape, width, length, color)

obj1=Area(shape,width, length, color)
obj2=Color(shape, width, length,color)




