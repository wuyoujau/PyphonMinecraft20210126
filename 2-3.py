from mcpi.minecraft import Minecraft

mc = Minecraft.create()

import random,time
while True:
    x,y,z = mc.player.getTilePos()
    
    color = random.randrange(0,16)
    mc.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,95,color)
    time.sleep(0.01)           





