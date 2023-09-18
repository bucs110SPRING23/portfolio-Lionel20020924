**This project is a simple flying chess game.**            
assets/ Media (images, music, etc.) must go into a separate assets folder.    
src/  All your source code (.py files) except for ‘main.py’ should go into the src folder.     
etc/ Anything else, additional documents you want to keep in your repo, should go here.    
    
The main files are divided into 3 parts.    
The main file is the launcher of the whole program.    
The board module sets up the game window.    
incident, a collection of utility classes.    

How to modify some properties such as background music, background image, and airplane style?
You can modify the path of your custom background music in this section of the main module.    
'''    
bgm = pygame.mixer.music.load('./etc/the diva dance.mp3')    
'''    
You can modify the default values of weight and height in the __init__ function of the Checkerboard class in the board module to change the size of the game window.    
To modify the style of the planes, you can replace the corresponding plane image in the assets folder with the image you like, but remember not to change the name of the image.    

**Some Class Descriptions:**    
Checkerboard:sets the dimensions of the interface, background image and reads the flight path.    
Plane:load plane image,sets the Plane type,Plane position  and other status.    
Event:events encountered in the game, such as rolling the dice, plane collision, jumping, and so on.    
Others:Some constant information. 