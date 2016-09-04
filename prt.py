import run_prt as rp
import sys
if __name__ == "__main__":
    prospect = input("Prospect URL? ")
    comp1 = input("First competitor? ")
    comp2 = input("Second competitor? ")
    rp.run_prt(sys.argv[1], prospect, comp1, comp2)
    print("Completed")
