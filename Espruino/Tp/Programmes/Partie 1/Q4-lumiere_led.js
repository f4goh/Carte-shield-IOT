var ldr;

function start() {
    ldr=analogRead(A0);
    console.log(ldr);
    if (ldr>0.5){
      digitalWrite(D0, true);
    }
    else
    {
      digitalWrite(D0, false);
    }
}

function onInit() {
      setInterval(start,1000);
}

