#include <Adafruit_NeoPixel.h>
#include <serLCD.h>

const int TOTAL_DIGITAL_PINS = 13;
const int WIDTH = 22;
const int HEIGHT = 20;

Adafruit_NeoPixel strips[(int)WIDTH];
Adafruit_NeoPixel strip;

void setup() {
    Serial.begin(9600);
    for (int x=0; x<WIDTH; x++) {
        strips[x] = Adafruit_NeoPixel(HEIGHT, 22 + x, NEO_GRB + NEO_KHZ800);
    }
    for (int x=0; x<WIDTH; x++) {
        strips[x].begin();
        strips[x].show();
    }
}

int incrementLoop = 0;
void loop() {
  strips[incrementLoop++].show();
  if (incrementLoop > WIDTH)
    incrementLoop = 0;
  delay(5);
}

char msg[5];
int msgPos = 0;

void processMessage(){
  int x = (int)msg[0];
  int y = (int)msg[1];
  int r = (int)msg[2];
  int g = (int)msg[3];
  int b = (int)msg[4];
  
  if (x == 11)
    y--;

  strips[x].setPixelColor(y, strips[x].Color(r, g, b));
}

void serialEvent() {
 
    while (Serial.available() > 0) {
        msg[msgPos++] = Serial.read();
        if (msgPos == 5){
          msgPos = 0;
          processMessage();
        }
    }
}
