# Door-Unlocker

This was put together over the a couple of months while messing around with a Raspberry Pi, an RFID Reader, and two servo motors.

The door unlocker is setup so that when someone taps an access card on the RFID reader, the mechanism will trigger and unlock the door to allow the person to enter.<br><br>
	To make sure that the door is not left unsecure, the mechanism will automatically trigger again after waiting 5 seconds. It will lock the door and light up the blue LED to indicate that the RFID reader is ready to detect the next access card, which may or may not be administered via broomstick handle.

<img src="https://github.com/StormPizza/Door-Unlocker/blob/master/images-videos/good_copt2.gif" width="340" title="Door-Unlocker-Complete-Cycle" alt="Raspberry Pi Door Unlocker with RFID Reader" >

Some requirements of this project included the fact that Door Unlocker must always be on (Not shown in the image) and that the Door Unlocker must not normally cover or obstruct access to the door lock. Even though this complicated the design of the Door Unlocker, it was important that this merely adds an additional way to unlock the door as opposed to restricting locking and unlocking to only one mode as with other types of door unlockers.
