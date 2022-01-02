var np = new Uint8ClampedArray(4*3);
var npPin = 14;

function setLed(n,r,v,b){
  np[n*3]=v;
  np[n*3+1]=r;
  np[n*3+2]=b;  
}

function clearLed() {
  for (var i=0;i<np.length;i++) {
    np[i]=0;
  }
  require("neopixel").write(npPin, np);
}

function start() {
    clearLed();
    setLed(0,0, 16, 0);
    setLed(1,0, 32, 32);
    setLed(2,16, 0, 16);
    setLed(3,16, 16, 16);
    require("neopixel").write(npPin, np);
}
