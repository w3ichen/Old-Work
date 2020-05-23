/* NOTE
1) Press the ultra sonic distance sensor at top left
2) Move the dot in range to trigger the alarm
3) Enter 123ABC in the touchpad to disable the alarm
*/
/* This arduino triggers an alarm if someone is sensed
in front of the ultrasonic sensor, to disable the alarm,
the password must be entered in the keypad */

#include <Keypad.h>
#include<Arduino.h>

using namespace std;

// constants
#define SIGNAL 11
#define ALARM 13
#define RED_LIGHTS 12

void setup(){
	init();
	Serial.begin(9600);
	pinMode(ALARM,OUTPUT);
  	pinMode(RED_LIGHTS,OUTPUT);
}

int main(){
	setup();
  
	int time,distance;
	// setting up the keypad
	const byte ROWS = 4; //four rows
	const byte COLS = 4; //four columns

	char keys[ROWS][COLS] = {
	  {'1','2','3','A'},
	  {'4','5','6','B'},
	  {'7','8','9','C'},
	  {'*','0','#','D'}
	};
	byte rowPins[ROWS] = {9, 8, 7, 6}; //connect to the row pinouts of the keypad
	byte colPins[COLS] = {5, 4, 3, 2}; //connect to the column pinouts of the keypad
	Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

  	// password to stop alarm
    char password[]= "123ABC";
    int pw_length = 6;
    int counter = 0;
	
  	while(true){
      	// to get distance to ultrasound distance sensor
		pinMode(SIGNAL,OUTPUT);
		digitalWrite (SIGNAL, LOW);
	    delayMicroseconds (2);
	    digitalWrite(SIGNAL, HIGH);
	    delayMicroseconds(5);
      	digitalWrite(SIGNAL,LOW);
      	pinMode(SIGNAL, INPUT);
      	time = pulseIn(SIGNAL, HIGH);
	    distance = (time * 0.034) / 2;

		if (distance <= 300 && distance>=0){
			// someone in front of sensor
			digitalWrite(ALARM,HIGH);
			digitalWrite(RED_LIGHTS,HIGH);
			
          // keypad inputs
   		  char key = keypad.getKey();
  		  if (key){
            Serial.print(key);
            if (key == password[counter]){
              counter++;
              if (counter == pw_length){
                Serial.println(" ");
                Serial.println("ALARM DISABLED");
                digitalWrite(ALARM, LOW);
                digitalWrite(RED_LIGHTS, LOW);
                break;
              }

            }else{
              counter = 0; //reset
            }
  		  }
		}else{
			digitalWrite(ALARM,LOW);
			digitalWrite(RED_LIGHTS,LOW);
		}
	}
}
