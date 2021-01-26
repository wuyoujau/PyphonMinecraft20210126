from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos() 

long = 10
big = 8
high = 7

block = 46
air = 0

mc.setBlocks(x,y,z,x+long,y+high,z+big,block)
mc.setBlocks(x+1,y+1,z+1,x+long-1,y+high-1,z+big-1,air)