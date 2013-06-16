#include <Adafruit_NeoPixel.h>
#include <SoftwareSerial.h>
#include <serLCD.h>
#include <math.h>

const int TOTAL_DIGITAL_PINS = 13;
const int WIDTH = 24;
const int HEIGHT = 20;

const int internalLED = 13;

Adafruit_NeoPixel strips[(int)WIDTH];

void setup() {
    Serial.begin(9600);
    for (int x=0; x<WIDTH; x++) {
        strips[x] = Adafruit_NeoPixel(HEIGHT, 22 + x, NEO_GRB + NEO_KHZ800);
    }
    for (int x=0; x<WIDTH; x++) {
        strips[x].begin();
        strips[x].show();
    }
    
    pinMode(internalLED, OUTPUT);
}

void loop() {
  digitalWrite(internalLED, HIGH);
  delay(100);
  digitalWrite(internalLED, LOW);
  delay(400);
}

char msg[5];
int msgPos = 0;

void processMessage(){
  Serial.println("-");  
  int x = (int)msg[0];
  int y = (int)msg[1];
  int r = (int)msg[2];
  int g = (int)msg[3];
  int b = (int)msg[4];

  strips[x].setPixelColor(y, strips[x].Color(r, g, b));

//  Serial.print("X:");
//  Serial.println(x);
//  Serial.print("Y:");
//  Serial.println(y);
//  Serial.print("R:");
//  Serial.println(r);
//  Serial.print("G:");
//  Serial.println(g);
//  Serial.print("B:");
//  Serial.println(b);
}

void serialEvent() {
 
    while (Serial.available() > 0) {
        Serial.print(".");
        msg[msgPos++] = Serial.read();
        if (msgPos == 5){
          msgPos = 0;
          processMessage();
        }
    }
}

//void serialEvent() {
//    String incomingString;
//    while (Serial.available() > 0) {
//        // read the incoming byte:
//        delay(2);
//        char incomingByte = Serial.read();
//        incomingString += (char)incomingByte;
//    }
//    String currentLight = "";
//    for (int x=0; x < incomingString.length(); x++) {
//        if (incomingString == ":")
//            break;
//        currentLight += incomingString[x];
//    }
//    int curLight = currentLight.toInt();
//    int curX = ceil((float)curLight / (float)WIDTH);
//    int curY = curLight % HEIGHT;
//    Serial.println(currentLight);
//    Serial.println(curX);
//    Serial.println(curY);
//    strips[curX].setPixelColor(curY, strips[curX].Color(255, 255, 255));
//    strips[curX].show();
//}
