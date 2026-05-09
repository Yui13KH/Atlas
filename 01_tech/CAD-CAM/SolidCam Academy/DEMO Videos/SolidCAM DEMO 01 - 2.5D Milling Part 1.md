

I'll basically watch the Demo videos and try to get a broad idea on how everything works and how everything is going on , I'll be writing notes here for me to have a deeper understanding of it 

since titans of cnc don't have solidcam tutorials and it is supposedly important here in turkey

---


To cut anything in solidcam u either import it or build it in solidworks 

note : from what i heard building something or preferebly if u have a solidworks file you can easily edit the model in solidworks and it wont effect solidcam much the adjustments are very easy unlike if u import say .step file from fusion 360 into solidcam if the model needs adjustments u have to re-open fusion , change it and re-export it to solidcam

U can start the process from the ribbon SOLIDWORKS CAM or the tools dropdown Solid cam -> new 



well idk maybe a newer solidcam version but 

oh , solidcam is not solidworks cam 
they sound the same so i assumed they are 

---

anyway  , solicam -> new 

then choose milling/turning/wireedm etc

Create cam part

u can create 2 types of cam 
External or Internal

Internal basically makes the toolpathes and all the cam operations in the solidworks file sldprt 

External makes a seperate file associated with the solidworks file 

both modes have associativity to the model which allows u to change the model without breaking the Cam with automatic or semi automatic updated to it

professionally External is preferred cause it keeps the model clean

external makes a perfect copy that u then work the cam on without editing the original

---

after that it makes a perfect copy and opens the setup things that is where u setup the part weather it is milling or turning or edm

pickup the cnc machine from the dropdown

for this example we are picking up 

oh i didnt know that u dont need gcode to create a whole cam project
gcode is for the actual machines to operate on , 

if u have the schematics for the machine u can make the cam for it and see the real machine simulation 

wellll since i have solidcam for makers i dont have the 5 axis ones which is fine 

its a 2.5d milling anyway

so u make the coordinate system

he said taht ever since select associate face came out he mainly uses that 

---

setting up the coordinate system , he mainly uses asoociative face and center of middle box or something like that 

he did setup 2 work coordinate systems 
cause he has a 5 axis machine but usually its just gonna be one 

target is usually automatically set on which is jsut what u want the target after cutting the stock to look like 


, that is how u start in ever cam project 

u choose the coordsys ,stock , target ,  then u start

