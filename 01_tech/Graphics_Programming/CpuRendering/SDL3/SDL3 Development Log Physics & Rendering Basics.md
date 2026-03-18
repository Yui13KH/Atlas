## Setup & Basics

- Learned about **SDL** a bit.
    
- Simple stuff like installing it and setting it up in **VS Code** (cause I am not using Visual Studio).
    
- Set it up using **CMake**.
    
- Used stuff like `SDL_Init`, `SDL_CreateWindow`, `SDL_GetWindowSurface`, `SDL_MapRGB`, and `SDL_GetPixelFormatDetails` to set the background color.
    

## Events & Input

- Did some simple stuff like closing the window by checking `SDL_Event` and `SDL_PollEvent` in a `while` loop.
    
- Found that there is `SDL_EVENT_MOUSE_MOTION`, which has a property `motion.x` and `motion.y`.
    
- **First Draw:** Drew 1 pixel at the center, then made that pixel follow the mouse.
    

## Shape Logic

- **Squares:** Using simple math, drew a square that snaps to the mouse. Just simple 2 nested loops that draw the rectangle with width and height.
    
- **Circles:** Used another math to draw the circle.
    
    - Looking in a square search area.
        
    - Used that search area to compare $x$ and $y$ to find $R$ (radius) and see if the pixel is inside or outside the circle and paint it.
        
    - Simple **Pythagorean theorem**: $a^2 + b^2 = c^2$.


![[circle.gif]]

## Physics Implementation

- Adding some physics like mouse $x$ and $y$ separated and circle $x$ and $y$ separated.
    
- Added stuff like `velocityX` and `velocityY`, friction, and attraction.
    
- Calculate the shape $x$ and $y$ and distance to mouse $x$ and $y$, and apply a bit of velocity towards it.
    
- Apply **friction** to the velocity so it's smooth.

![[physics.gif]]