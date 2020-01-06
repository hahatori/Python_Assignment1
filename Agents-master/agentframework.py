import random

# Build the Agent class.
class Agent:
    
    # Define the initialization method to assign values of x and y.
    def __init__(self):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        
    # Define the "move" method to change x and y randomly. 
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100 
            
       print("y= %s, x= %s" % (self.y, self.x)) # Test random numbers.
            
# Creat objects, test the output random numbers y and x.             
a = Agent()
print(a)# Display a hexadecimal address.
print(a.y, a.x) # Display random numbers of y and x.

a.move() #The output of x and y is the same as the following line.
print("y= %s, x= %s" % (a.y, a.x))



