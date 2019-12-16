const int SWITCH_PIN = 4;
int value = 1;

void setup(){
    pinMode( SWITCH_PIN, INPUT );
    Serial.begin( 9600 );
}

void loop(){
    
    if (digitalRead( SWITCH_PIN ) ==  0){
      if (value == 1) {
        value = 0;
      }
      else {
        value = 1; 
      }
    }

    if (value == 0){
      Serial.println( value );  
    }
    
    delay( 1000 );
}
