# Door-Unlocker

This was put together over the a couple of months while messing around with a Raspberry Pi, an RFID Reader, and two servo motors.

The door unlocker is setup so that when someone taps an access card on the RFID reader, the mechanism will trigger and unlock the door to allow the person to enter.<br><br>
	To make sure that the door is not left unsecure, the mechanism will automatically trigger again after waiting 5 seconds. It will lock the door and light up the blue LED to indicate that the RFID reader is ready to detect the next access card, which may or may not be administered via broomstick handle.

![alt text](images-videos/good_copt2.gif "BlueLED-Unlock-Wait-Lock-BlueLED")
