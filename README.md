# montyhall
simple monty hall problem simulator



The Monty Hall Problem is described as follows:

You are a contestant on a game show. You have the option to select from Doors 1, 2, and 3 and will get the prize behind the door.

Behind two doors are annoying ass goats. Behind one door is a god damn Ferrari.

After you make your choice, the host opens one of the doors you didn't choose and reveals a goat.

They then ask if you would like to swtich your choice to the remaining door.


The code below simulates what happens in (user input, n) simulations of this game.

/spoiler (staying tends toward 1/3 getting ferrari and switching tends toward 2/3 getting the ferarri)



User enters the number of game simulations to run.

For each simulation:

    generates random player selection of a Door 1, 2 , or 3.

    generates location of a winner Door 1, 2, or 3.

    Checks against player selection, and of the remaining two doors, selects one that is not the winner.

    Checks if the players original choice is the winnner. If so, it adds +1 to "stay wins"

    Determines the switch option as the door not currently selected AND not the door selected as "not winner".

    Checks if the switch choice is the winner. If so, it adds +1 to  "switch  wins"
