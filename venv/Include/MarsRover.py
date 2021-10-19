class Rover:
    def __init__(self,locX,locY,direction,steps):
        self.locX=locX
        self.locY=locY
        self.direction=direction
        self.steps=steps

    def TurnLeft(self,moveDirection):
        switcher = {
            "N": "W",
            "S": "E",
            "W": "S",
            "E": "N",
        }
        self.direction = switcher.get(moveDirection, "")

    def TurnRight(self,moveDirection):
        switcher = {
            "N": "E",
            "S": "W",
            "W": "N",
            "E": "S",
        }
        self.direction = switcher.get(moveDirection, "")

    def Move(self,moveX,moveY,moveDirection):
        if(moveDirection == "N"):
            self.locY += 1
        if(moveDirection == "S"):
            self.locY -= 1
        if(moveDirection == "W"):
            self.locX -= 1
        if(moveDirection == "E"):
            self.locX += 1

    def RoverLocation(self):
        stepList = list(self.steps)
        for step in stepList:
            if (step == "L"):
                self.TurnLeft(self.direction)
            if(step == "R"):
                self.TurnRight(self.direction)
            else:
                self.Move(self.locX,self.locY,self.direction)
        return "{} {} {}".format(self.locX, self.locY, self.direction)

rover = Rover(1,2,"N","LMLMLMLMM")#Gezginin iniş yaptığı konum (1,2) ve yön (N) + gezgin için belirlenen ilerleme kodu (LMLMLMLMM)
result = rover.RoverLocation()
print(result)
