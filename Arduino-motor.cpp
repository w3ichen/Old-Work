#define motor 5
#define ON_SWITCH 11
#define ON_LIGHT 12
#define dial A0

void setup()
{
  pinMode(motor, OUTPUT);
  pinMode(ON_SWITCH, INPUT_PULLUP);
  pinMode(ON_LIGHT, OUTPUT);
  pinMode(dial,INPUT);
  Serial.begin(9600);
}

bool ON = false;
void loop()
{
  if (digitalRead(ON_SWITCH) == LOW){
    Serial.println(analogRead(dial));
    // on button pressed
    if (ON){
      // turn light off 
      digitalWrite(ON_LIGHT, LOW);
      ON = false;
      // turn motor off
      analogWrite(motor, 0);
    }else{
      // turn light on
      digitalWrite(ON_LIGHT, HIGH);
      ON = true;
    }
      delay(400);
  }
  if (ON){
    int speed = map(analogRead(dial),0,1023,0,255);
    Serial.println(speed);
    analogWrite(motor,speed);
  }
}
