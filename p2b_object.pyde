# John Ho
# Animation Example to draw Red/Blue Joycons clicking onto a Nintendo Switch
# My instantiated objects are 3 blue joycons and 2 red joycons, made of 8 objects each

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    global bg 
    global bg2
    bg = loadImage("switchbg.png") #First BG Image
    bg2 = loadImage("switchbg2.png") #Second BG Image

    
def draw():
    
    global time
    global time2
    time += 0.01
    if time == 0.01:
        time2 = 0
    
    background (bg)  #Upload first BG image
    
    # create a directional light source
    ambientLight(75, 75, 75);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    
    camera (0, -100, 100, 0, -100, 0, 0,  1, 0)  # position the virtual camera
    
    #Set up first animation scene
    if time < 6: 
        
        pushMatrix()
        if time < 1:
            translate(0,-100,0)
        elif time > 1 and time < 3:
            camera (-100, -100, 100, -40, -100, 0, 0, 1, 0)  #Animate Blue Joycon spinning
            translate(0,-100,0)
            rotateX(-time*2)
        blueJoyCon() #Instantiating one custom object
        popMatrix()
        
        if time > 1 and time < 3:
            pushMatrix()
            translate(80,-100,0)
            rotateX(-time*2)
            blueJoyCon() #Instantiating one custom object
            popMatrix()

            pushMatrix()
            translate(0,-100,0)
            rotateX(-time*2)
            blueJoyCon() #Instantiating one custom object
            popMatrix()

    
        pushMatrix()
        if time < 1:
            translate(0,-100,0)
        elif time > 3 and time < 6:
            camera (-100, -100, 100, 0, -100, 0, 0, 1, 0)  #Animate Red Joycon Rotating
            translate(0,-100,0)
            rotateY(-time*2)
        redJoyCon() #Instantiating second custom object
        popMatrix()
   
        if time > 3 and time < 6:
            pushMatrix()
            translate(0,-100,0)
            rotateZ(-time*2 + 250)
            redJoyCon() #Instantiating second custom object
            popMatrix()
   
   
   #Set up next animation scene
    if time > 6:

        if time > 12:
            time2 += 0.01
        
        #While Joycons are translating down, switch cam angles every sec
        if time > 6 and time < 12.5:
            camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  
        elif time > 12.5 and time < 13.5:
            camera (80, 0, 100, 0, 0, 0, 0,  1, 0)  
        elif time > 13.5 and time < 14.5:
            camera (-80, 0, 100, 0, 0, 0, 0,  1, 0)  
        elif time > 14.5 and time < 15.5:
            camera (0, -50, -100, 0, 0, 0, 0,  1, 0) 
        else:
            camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  
            
        #Once translation is done, switch the background!
        if time > 16.25:
            background(bg2)
            camera (0, 0, 100, 0, 15, 0, 0,  1, 0)  # position final cam scene 
        
        
        #Original Project 2A Object
        pushMatrix()
        if time > 6 and time < 12.5:
            rotateX (-time)
        switchBody()
        popMatrix()
        
        
        pushMatrix()
        if time2 < 4:
            translate(0,-100,0)
            translate(0,time2 * 25,0) #Animate Blue Joycon transitioning down
        blueJoyCon()
        popMatrix()
        
        
        pushMatrix()
        if time2 < 4:
            translate(0,-100,0)
            translate(0,time2 * 25,0) #Animate Red Joycon transitioning down
        redJoyCon()
        popMatrix()
        

    
#Project 2A Object
def switchBody():
    # Black Switch Body
    fill (0, 0, 0)
    pushMatrix()
    translate (0, 0, 0)
    scale (3.5, 2, 0.41)
    box(20)
    popMatrix()

    # Grey Switch screen
    fill (77, 77, 77)
    pushMatrix()
    scale (3., 1.75, 0.41)
    translate (0, 0, 0.1)
    box(20)
    popMatrix()
    
    # Rotated Diamond logo on back
    fill (22, 22, 22)
    pushMatrix()
    scale (1, 1, 0.4)
    translate (0, 0, -1)
    rotate(PI/4)
    box(20)
    popMatrix()


def blueJoyCon():
    # Blue Joycon Body
    fill (0, 200, 255)
    pushMatrix()
    translate (-41, 0, 0)
    scale (0.6, 1.7, 0.4)
    box(20)
    popMatrix()
    
    # Blue Joycon Bump
    pushMatrix()
    translate (-41,0,0)
    scale(0.6,0.5,0.5)
    translate(0,-29.8,-4)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()
    
    # Blue Joycon Rounded Top
    pushMatrix()
    translate (-45.5, -24.5, 10)
    scale (6, 2.9, 4)
    translate(0.755,2.525,-2.5)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate (-45.5, -22.2, 10)
    scale (1.5, 2, 2)
    translate(5,3.05,-5)
    box(4)
    popMatrix()
    
    # Blue Joycon Rounded Bottom
    pushMatrix()
    translate (-45.5, 10, 10)
    scale (6, 2.9, 4)
    translate(0.755,2.475,-2.5)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate (-45.5, 10, 10)
    scale (1.5, 2, 2)
    translate(5,3.05,-5)
    box(4)
    popMatrix()
    
    #Blue Joycon Thumbstick
    fill (0, 0, 0)
    pushMatrix()
    translate (-40, 0, 0)
    scale (2, 2, 2)
    translate(0,-5,1.5)
    cylinder()
    popMatrix()
    
    #Blue88 Joycon Thumbpads
    fill (0, 0, 0)
    pushMatrix()
    translate (-40, 0, 0)
    scale (2.5, 2.5, 2)
    translate(-0.1,-4.25,2.75)
    cylinder()
    popMatrix()
    

def redJoyCon():
    # Red Joycon Body
    fill (255,40,50)
    pushMatrix()
    translate (41, 0, 0)
    scale (0.6, 1.7, 0.4)
    box(20)
    popMatrix()

    # Red Joycon Bump
    pushMatrix()
    translate (41,0,0)
    scale(0.6,0.5,0.5)
    translate(0,-29.8,-4)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()

    # Red Joycon Rounded Top
    pushMatrix()
    translate (30.5, -24.5, 10)
    scale (6, 2.9, 4)
    translate(1.75,2.525,-2.5)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate (30.5, -22.2, 10)
    scale (1.5, 2, 2)
    translate(5,3.05,-5)
    box(4)
    popMatrix()
    
    # Red Joycon Rounded Bottom
    pushMatrix()
    translate (45.5, 10, 10)
    scale (6, 2.9, 4)
    translate(-0.75,2.48,-2.5)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate (-45.5, 10, 10)
    scale (1.5, 2, 2)
    translate(55.65,3.05,-5)
    box(4)
    popMatrix()
    
    # Red Joycon Thumbsticks 
    fill (0, 0, 0)
    pushMatrix()
    translate (40, 0, 0)
    scale (2, 2, 2)
    translate(0,5,1.5)
    cylinder()
    popMatrix()
    
    # Red Joycon Thumbpads
    fill (0, 0, 0)
    pushMatrix()
    translate (40, 0, 0)
    scale (2.5, 2.5, 2)
    translate(0.1,4.25,2.75)
    cylinder()
    popMatrix()

    

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2