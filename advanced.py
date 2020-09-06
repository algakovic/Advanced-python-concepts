'''Getting to grips with VS Code and Python'''
import math

class geometry_solver(object):
    @staticmethod
    def area_of_circle(radius):
        return(math.pi * radius**2)

    @staticmethod
    def area_of_rect(width, length):
        ans = width * length
        return (ans)
    
    @staticmethod
    def volume_of_box(width, length, depth):
        area = width*length
        vol = area + depth
        return (vol)


# Main function
# Entry point for the program
# prints a simple menu- you make the choice and supply the values

def main():
    running = True
    while (running):
        # Print menu
        print() # blank line
        print("Welcome to the Geometry solver V2")
        print("---------------------------------")
        print("1) Area of a circle")
        print("2) Area of a rectangle")
        print("3) Volume of a box")
        print("X) Exit")

        # process user input
        choice = input("Your choice?")
        if choice == "X":
            print(Goodbye!)
            running = False
        elif choice =="1":
            response = input("Radius? ")
            r = float(response)
            ans = geometry_solver.area_of_circle(r)
            print(f"Area of circle with radius {r} is {ans}")
        elif choice == "2":
            response == input("Width? ")
            w = float(response)
            response = input("Length? ")
            l = float(response)
            ans = geometry_solver.area_of_rect(w, l)
            print(f"Area of Recatngle with width {w} and length {l} is {ans}")
        elif choice == "3":
            response == input("")

'''system module'''
