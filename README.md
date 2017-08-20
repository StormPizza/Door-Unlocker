# Door-Unlocker

This was put together over the a couple of months while messing around with a Raspberry Pi, an RFID Reader, and two servo motors.

The door unlocker is setup so that when someone taps an access card on the RFID reader, the mechanism will trigger and unlock the door to allow the person to enter.<br><br>
	To make sure that the door is not left unsecure, the mechanism will automatically trigger again after waiting 5 seconds. It will lock the door and light up the blue LED to indicate that the RFID reader is ready to detect the next access card, which may or may not be administered via broomstick handle.

<img src="https://github.com/StormPizza/Door-Unlocker/blob/master/images-videos/good_copt2.gif" width="340" title="Door-Unlocker-Complete-Cycle" alt="Raspberry Pi Door Unlocker with RFID Reader" >

Some very important requirements in the making of this project was the fact that 
1. The Door Unlocker must always be on (Not shown in the gif above) 

and 

2. The Door Unlocker must not normally cover or obstruct access to the door lock. This means that as much as it would have been easier to keep the servo-powered twisting-gripper on the lock handle at all times, this was not allowed. The gripper must move away from the lock handle, which is why the swinging arm is there.

The reason for this seemingly unnecessary restriction was because it was important that this mechanism merely adds an additional way to unlock the door as opposed to restricting locking and unlocking to only one mode as with other types of door unlockers. People who are on the inside side of the door must be able to unlock the door without having to use the mechanism.

Furthermore, another requirement was that 

3. No permanent modifications be done to the door being used, hence the use of cardboard, foamboard and wood in its construction, as these materials are light enough so that the entire mechanism could be confidently fastened to the door with removable Command adhesive strips.
