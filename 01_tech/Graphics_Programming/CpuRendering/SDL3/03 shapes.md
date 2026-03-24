
I improved the previous code a bit by making a struct of color that has the a , r ,g , b values and then returns the bit shift in a function so i dont initilize colors out randomly i could make them variables or just edit that struct 

since i already had loop i just tried some conditionals to draw lines 

like 

x  = width / 2 + 1  for a vertical line 
y = height / 2 + 1 for a horizontal line 

tried first making a corner to corner by doing x = y and then i realized 

![[incorrect corner-corner.png]]

it only works on square screens for this to work u need to take the aspect ratio in account which is basically the slope 

so a simple  height / width  then u apply that to the x ur finding and u get this 

![[correct corner-corner.png]]

`y == (x * SCREEN_HEIGHT) / SCREEN_WIDTH`

just having fun tbh 

so now i was like hmm lets make a shapes 

square seemed very easy its just a of pixels 

