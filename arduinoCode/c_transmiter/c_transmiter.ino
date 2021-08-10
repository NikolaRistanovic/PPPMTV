#define ctrl1Pin 2
#define ctrl2Pin 3
#define redPin 5
#define greenPin 4

bool status = false;
int signalInterval = 10;
bool red;
bool green;

long startTime;

char n;
String temp;
String inString;

//------------------------------------------------

void initialise(){
  Serial.begin(115200);
  Serial.println("Prenos podataka putem mehanickih talasa u vodi V1.0");
  pinMode(ctrl1Pin,OUTPUT);
  pinMode(ctrl2Pin,OUTPUT);
  pinMode(redPin,OUTPUT);
  pinMode(greenPin,OUTPUT);
  lights();
  }

void getString(){
  n = Serial.read();
    if(n != '\n'){
      temp += n; 
      }
    else{
        inString = temp;
        temp = "";
      }
  }

void commandExecute(){
  Serial.println(inString);
  
  if(inString == "AT"){
    Serial.println("Prenos podataka putem mehanickih talasa u vodi V1.0");
    }
    
  if(inString == "AT?"){
    Serial.print("Status : ");
    if(status){Serial.println("Running");}else{Serial.println("Stopped");};
    Serial.print("Interval : ");
    Serial.println(signalInterval);
    }

  if(inString == "AT START"){status = true;startTime = millis();}

  if(inString.substring(0,12) == "AT INTERVAL "){
    long tempInt = inString.substring(12).toInt();
      if(tempInt != 0){signalInterval = tempInt;}else{Serial.println("ERR param NaN or 0");}
    }
  }

void lights(){
  red = !status;
  green = status;
  digitalWrite(redPin,!red);
  digitalWrite(greenPin,!green);
  }
  
void ctrl1(bool state){digitalWrite(ctrl1Pin,state);}
void ctrl2(bool state){digitalWrite(ctrl2Pin,state);}

//------------------------------------------------

void setup() {
  initialise();
}

void loop() {
  if(Serial.available()){
    getString();
    }

    
  if(inString != ""){
    if(inString.substring(0,2) != "AT"){
      Serial.println("ERR not AT comm");
      }else{
        commandExecute();
      }
    inString = "";
    }

  if(status){
    lights();
    ctrl1(1);
    if(startTime + signalInterval <= millis()){
      status = 0;
      lights();
      ctrl1(0);
      }
    }
}
