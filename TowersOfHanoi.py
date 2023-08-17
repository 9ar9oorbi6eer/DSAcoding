def moveDisk(n, source, destination, aux, ind=""):
    print(f"{ind}Recursion Level={n}")
    if n == 1:
        print(f"{ind}Moving Disk {n} from Source {source} to Destination {destination}")
        print(f"{ind}n={n}, src={source}, dest={destination}")
        
        return
    moveDisk(n - 1, source, aux, destination, ind + "    ")
    print(f"{ind}Moving Disk {n} from Source {source} to Destination {destination}")
    print(f"{ind}n={n}, src={source}, dest={destination}")
    
    moveDisk(n - 1, aux, destination, source, ind + "    ")

def towersOfHanoi(num_disks):
    print(f"Number of disks on the starting tower: {num_disks}")
    print(f"towers({num_disks},1,3)")
    
    moveDisk(num_disks, 1, 3, 2)

def main():
    num_disks = int(input("Enter the number of disks: "))
    towersOfHanoi(num_disks)
    
main()
