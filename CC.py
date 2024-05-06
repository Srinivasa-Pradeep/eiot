from gpiozero import DigitalInputDevice, Buzzer
from signal import pause


IR_SENSOR_PIN = 3  
BUZZER_PIN = 5  


ir_sensor = DigitalInputDevice(IR_SENSOR_PIN, pull_up=None, active_state=False)  
buzzer = Buzzer(BUZZER_PIN)


def ir_sensor_state_changed():
    if ir_sensor.value:
        print(0)  
        buzzer.off()  
    else:
        print(1)
        buzzer.on()  


ir_sensor.when_activated = ir_sensor_state_changed
ir_sensor.when_deactivated = ir_sensor_state_changed


pause()
