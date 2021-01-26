from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

answer = int(input('問你右邊要放什麼方塊:'))
mc.setBlock(x+1,y,z,answer)
