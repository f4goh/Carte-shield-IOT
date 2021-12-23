
class Nunchuck():
    def __init__(self, i2c, addr=0x52):
        self.i2c = i2c
        self.addr = addr
        self.buffer = bytearray(6)
        self.i2c.start()
        self.i2c.writeto(self.addr, b'\xF0\x55')
        self.i2c.stop()
        self.i2c.start()
        self.i2c.writeto(self.addr, b'\xFB\x00')
        self.i2c.stop()
    
    def rescale(self,valeur, in_min, in_max, out_min, out_max):
        return int((valeur - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def read(self,scale=0):
        self.i2c.start()
        self.i2c.writeto(self.addr, b'\x00')
        self.i2c.stop()
        self.i2c.start()
        self.buffer=self.i2c.readfrom(self.addr, 6)
        self.i2c.stop()
        joyX=self.buffer[0]
        joyY=self.buffer[1]
        accX = (self.buffer[2] * 4) + ((self.buffer[5] // 4) & 3)
        accY = (self.buffer[3] * 4) + ((self.buffer[5] // 16) & 3)
        accZ = (self.buffer[4] * 4) + ((self.buffer[5] // 64) & 3)
        btC = (self.buffer[5] // 2 ) & 1
        btZ = self.buffer[5] & 1
        if scale==1:
            accX=self.rescale (accX, 256, 768,0, 255)
            accY=self.rescale (accY, 256, 768,0, 255)
            accZ=self.rescale (accZ, 256, 768,0, 255)
            if accX>255:
                accX=255 
            if accX<0:
                accX=0 
            if accY>255:
                accY=255 
            if accY<0:
                accY=0 
            if accZ>255:
                accZ=255 
            if accZ<0:
                accZ=0 
        return(accX,accX,accZ,joyX,joyY,btC,btZ)
    