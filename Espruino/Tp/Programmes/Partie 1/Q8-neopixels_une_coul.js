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
    var i;
    for (i=0;i<4;i++){
      setLed(i,16, 16, 0);
    }
    require("neopixel").write(npPin, np);
}
