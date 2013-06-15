#include <Adafruit_NeoPixel.h>
#include <SoftwareSerial.h>
#include <serLCD.h>
#include <math.h>

const int TOTAL_DIGITAL_PINS = 13;
const int WIDTH = 24;
const int HEIGHT = 20;

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
}

void loop() {
    
}

void serialEvent() {
    String incomingString;
    while (Serial.available() > 0) {
        // read the incoming byte:
        delay(2);
        char incomingByte = Serial.read();
        incomingString += (char)incomingByte;
    }
    String currentLight = "";
    for (int x=0; x < incomingString.length(); x++) {
        if (incomingString == ":")
            break;
        currentLight += incomingString[x];
    }
    int curLight = currentLight.toInt();
    int curX = ceil((float)curLight / (float)WIDTH);
    int curY = curLight % HEIGHT;
    Serial.println(currentLight);
    Serial.println(curX);
    Serial.println(curY);
    strips[curX].setPixelColor(curY, strips[curX].Color(255, 255, 255));
    strips[curX].show();
}
