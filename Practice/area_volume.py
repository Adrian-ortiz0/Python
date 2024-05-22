def circle_area(r):
    op = 3.14*(r**2) 
    return op

def cilinder_volume(height, r):
    volume = circle_area(r) * height
    return volume
    
opt = input("Do you want to calculate area or volume: (a/v)")
if opt == "a":
  r = float(input("Type ratio: "))  
  print(circle_area(r))
elif opt == "v":
    r = float(input("Type ratio: "))
    h = float(input("Type height: "))
    print(cilinder_volume(h, r))
else:
    print("Invalid command!")