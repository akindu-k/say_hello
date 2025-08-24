from greeter import Greeter
from math_utils import multiply

def main():
    g = Greeter("Akindu")
    print(g.greet())

    result = multiply(3, 4)
    print(f"3 multiplied by 4 is {result}")

if __name__ == "__main__":
    main()
