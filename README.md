[Companion PopTracker pack can be found here](https://github.com/RBmans/poptracker-atb-manualAP)

# AmnesiaTheBunkerManualAP
Implementation of Amnesia The Bunker into Archipelago Manual

**Game:** Amnesia: The Bunker

**Checks:** Key Items (Flashlight, Gun, Cutters, etc.), Photos, Notes with VO, Dog Tags, Locker Items, Non-Randomized Pocket Bags, Keys 

**Items:** Key Items, Keys, Pocket Bags, Dog Tag Codes, Consumables (Receiving a consumable item, such as a Grenade, allows you to use as many grenades as you can find in the world, in addition to the ones located in the save room).

**Victory Condition:** Use the detonator handle and the dynamite to escape the bunker.

**Notes:** This has been created with the use of the Manual AP Companion Add-On for Bunker. [You can find the workshop add-on here!](https://steamcommunity.com/sharedfiles/filedetails/?id=3014611969) 

It changes the save room to contain every item in the game, so when you receive the item, you can grab it from the save room if you do not already have it in your possession. The Arsenal code requires you to use the new radio that has been placed in the corner of the room by turning it on, off, and then on again (I am bad at HPL3 scripting I apologize for the jank).

The most important thing to note is that **I have not included Fuel as part of this implementation.** I did not want to put players into a situation where they are forced to do areas in the complete dark due to not having fuel to power the generator. Whatever fuel you find in the game, you are free to use! I also have not included bandages and medkits for similar reasons.

Due to the very open-nature and experimental aspect of the game, not every single angle of attack has been considered, just the common ones. One consideration I have made is changing the amount of bricks that spawn in certain locations, to make certain doors always breakable without requiring grenades/shotgun (this includes locked doors in the Soldier Quarters as well as the Arsenal).

Another example, when it comes to dealing with rats (whether it is passing by them or checking the dog tags on the bodies they are around), this expects you to either have a lighter with a torch (or a petrol bomb), or a gas mask and gas grenade, or flares. Technically, you are able to use your gun to clear out rats, but due to the implications of using your gun in the bunker, I did not add this as a consideration, so you should never be forced to do this.

(On the topic of rats, I have not put any special considerations to passing by the rats on the way to maintenance or passing by the ones in Arsenal. These rats are either tankable or easily killable with items around your character, so I did not see a need to put special requirements on them. I have added extra bandages in the save room to account for this.)
