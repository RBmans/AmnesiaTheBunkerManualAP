# AmnesiaTheBunkerManualAP
Implementation of Amnesia The Bunker into Archipelago Manual

**Game:** Amnesia: The Bunker

**Checks:** Key Items (Flashlight, Gun, Cutters, etc.), Photos, Notes with VO, Dog Tags, Locker Items, Non-Randomized Pocket Bags, Keys

**Key Items:** Basically everything except for a few consumables and the shotgun. Thanks open-ended game design! (Receiving a consumable item, such as a Grenade, allows you to use whatever grenades you can find available).

**Victory Condition:** Receive the detonator handle and the dynamite to escape the bunker.

**Notes:** The most important thing to note is that **I have not included Fuel as part of this implementation.** I did not want to put players into a situation where they are forced to do areas in the complete dark due to not having fuel to power the generator. Whatever fuel you find in the game, you are free to use! I also have not included bandages and medkits for similar reasons.

Unfortunately, the randomized Pocket Bags are not locations, only the three bags that are always placed in the same place. I thought about adding them, but accounting for the variety of locations and what you logically require to reach those was too difficult for me to implement.

Due to the very open-nature and experimental aspect of the game, not every single angle of attack has been considered, just the common ones. For example, when it comes to dealing with rats (whether it is passing by them or checking the dog tags on the bodies they are around), this expects you to either have a torch and a lighter, or a gas mask and gas grenade, or flares. Technically, you are able to use your gun to clear out rats, but due to the limited amount of bullets and the implications of using your gun in the bunker, I did not add this as a consideration, so you should never be forced to do this.

(On the topic of rats, I have not put any special considerations to passing by the rats on the way to maintenance or passing by the ones in Arsenal. These rats are either tankable or easily killable with items around your character, so I did not see a need to put special requirements on them.)
