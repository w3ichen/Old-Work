#include <Arduino.h>
#include <IRremote.h>
#include <LiquidCrystal.h>

#define redPin A0
#define bluePin A1
#define greenPin A2
#define redBtn 10
#define greenBtn 9
#define blueBtn 8
#define led 36
int RECV_PIN = 11;

IRrecv receiver(RECV_PIN);
decode_results results;

LiquidCrystal lcd(12, 13, 5, 4, 3, 2);

void setup(){
  init();
  Serial.begin(9600);
  pinMode(redPin,OUTPUT);
  pinMode(greenPin,OUTPUT);
  pinMode(bluePin,OUTPUT);
  pinMode(redBtn,INPUT_PULLUP);
  pinMode(greenBtn,INPUT_PULLUP);
  pinMode(blueBtn,INPUT_PULLUP);
  lcd.begin(16, 2);
  receiver.enableIRIn(); 
  // set light to white
  analogWrite(redPin,255);
  analogWrite(bluePin,255);
  analogWrite(greenPin,255);
  
  lcd.setCursor(0,0);
  lcd.print("RED");
  lcd.setCursor(5,0);
  lcd.print("GREEN");
  lcd.setCursor(12,0);
  lcd.print("BLUE");
  
  lcd.setCursor(0,1);
  lcd.print("255");
  lcd.setCursor(6,1);
  lcd.print("255");
  lcd.setCursor(12,1);
  lcd.print("255");
}


double cursorColor = 0; // 0 is red, 1 is green, 2 is blue
int wordLength = 0; // should not exceed 3
int new_rgb = 0;

void remoteRGB(int number){
    lcd.setCursor((cursorColor*6)+wordLength,1);
    lcd.print(number);
    if (wordLength == 0){
      // 100th
      new_rgb += 100*number; 
    }
    else if (wordLength == 1){
      // 10th
      new_rgb += 10*number; 
    }
    else if (wordLength == 2){
      // 1th
      new_rgb += number; 
    }
    wordLength ++;
    if (wordLength == 3){
      // met the word length
      wordLength = 0;
      if (cursorColor == 0){
        // is red
        Serial.print("changing red to: ");Serial.println(new_rgb);
        new_rgb = constrain(new_rgb,0,255);
        analogWrite(redPin, new_rgb);
        new_rgb = 0;
      }
      else if (cursorColor == 1){
        // is green
        Serial.print("changing green to: ");Serial.println(new_rgb);
        new_rgb = constrain(new_rgb,0,255);
        analogWrite(greenPin, new_rgb);
        new_rgb = 0;
      }
      else if (cursorColor == 2){
        // is blue
        Serial.print("changing blue to: ");Serial.println(new_rgb);
        new_rgb = constrain(new_rgb,0,255);
        analogWrite(bluePin, new_rgb);
        new_rgb = 0;
      }    
      cursorColor = int(cursorColor + 1)%3; // go to next color
      delay(300);
    }
}

int main(){
	setup();

	while(true){
    if (receiver.decode(&results)){   
      if (results.value == 0xFFE01F){
        // scroll down
        Serial.println("scroll down");
        cursorColor = int(cursorColor + 1)%3;
        wordLength = 0;
      }else if (results.value == 0xFF906F){
        // scroll up
        Serial.println("scroll up");
        cursorColor = int(cursorColor - 1)%3;
        wordLength = 0;
      }else if (results.value == 0xFD30CF){
        // 0
        Serial.println("0");
        remoteRGB(0); 
      }else if (results.value == 0xFD08F7){
        //1
        Serial.println("1");
        remoteRGB(1);
      }else if (results.value == 0xFD8877){
        //2
        Serial.println("2");
        remoteRGB(2);
      }else if (results.value == 0xFD48B7){
        //3
        Serial.println("3");
        remoteRGB(3);
      }else if (results.value == 0xFD28D7){
        //4
        Serial.println("4");
        remoteRGB(4);
      }else if (results.value == 0xFDA857){
        //5
        Serial.println("5");
        remoteRGB(5);
      }else if (results.value == 0xFD6897){
        //6
        Serial.println("6");
        remoteRGB(6);
      }else if (results.value == 0xFD18E7){
        //7
        Serial.println("7");
        remoteRGB(7);
      }else if (results.value == 0xFD9867){
        //8
        Serial.println("8");
        remoteRGB(8);
      }else if (results.value == 0xFD58A7){
        //9
        Serial.println("9");
        remoteRGB(9);
      }
      receiver.resume();
    }

	// buttons manage color
	if(digitalRead(redBtn)==LOW){
	  cursorColor = 0;
	  wordLength = 0;
	}
	if (digitalRead(greenBtn)==LOW){
    cursorColor = 1;
	  wordLength = 0;
	}
	if (digitalRead(blueBtn)==LOW){
    cursorColor = 2;
	  wordLength = 0;
	}
  	delay(100);   
  }
}

