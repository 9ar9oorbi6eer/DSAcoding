def moveDisk(n, source, destination, aux, ind=""):
    if n == 1:
        print(f"{ind}Moving disk from peg {source} to peg {destination}")
        return
    moveDisk(n - 1, source, aux, destination, ind + "  ")
    print(f"{ind}Moving disk from peg {source} to peg {destination}")
    moveDisk(n - 1, aux, destination, source, ind + "  ")

def towersOfHanoi(num_disks):
    moveDisk(num_disks, 1, 3, 2)

def main():
    num_disks = int(input("Enter the number of disks: "))
    towersOfHanoi(num_disks)
    
main()