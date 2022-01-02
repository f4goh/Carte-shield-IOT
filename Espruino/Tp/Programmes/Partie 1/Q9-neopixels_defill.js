var np = new Uint8ClampedArray(4*3);
var npPin = 14;
var etape=0;

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
    var i;
    for (i=0;i<4;i++){
      if (i==etape){
         setLed(i,16, 16, 0);
      }
      else{
        setLed(i,0, 0, 0);
      }
    }
    etape=(etape+1)%4;
    require("neopixel").write(npPin, np);
}

function onInit() {
      clearLed();
      setInterval(start,100);
}


