

Before you can draw anything cool with OpenGL, you need two basic things:  
- An **OpenGL context** (the environment where all the OpenGL state lives)  
- A **window** to actually show your rendering on screen  

OpenGL itself doesn't know how to create windows or talk to your operating system—that stuff is different on Windows, Linux, macOS, etc. So OpenGL stays "pure" and leaves that part to you.

Doing it completely from scratch is a pain (tons of OS-specific code), so pretty much everyone uses a helper library. The popular ones are **GLUT**, **SDL**, **SFML**, and **GLFW**. We're gonna talk about **GLFW** because it's simple, lightweight, and made specifically for OpenGL.

## What GLFW Solves
GLFW handles the boring but necessary stuff:
- Creates a window
- Sets up an OpenGL context inside that window
- Lets you handle keyboard/mouse/joystick input
- Gives you control over window size, title, fullscreen, etc.

Basically, it saves you from writing hundreds of lines of platform-specific code just to get a blank window on screen.

## The Other Big Problem: Loading OpenGL Functions
OpenGL is just a **specification**, not a ready-to-use library with all functions baked in. The actual functions live inside your GPU driver, and their addresses aren't known when you compile your program—you have to ask for them at **runtime**.

On Windows, you do something ugly like this for every single OpenGL function:
```c
// example for glGenBuffers
void (*glGenBuffers)(GLsizei, GLuint*) = (void(*)(GLsizei, GLuint*))wglGetProcAddress("glGenBuffers");
```
Yeah I feel sad for old developers

I vaguely even understand what this does , I believe its basically a pointer function with those arguments pointing to the actual function in memory and then casting the raw memory location into the actual function

## What GLAD Solves
GLAD is a code generator that:
- Gives you all the correct function pointers for the OpenGL version you want (e.g., 3.3 core or higher)
- Provides a simple `gladLoadGL()` function you call once after creating the context
- Automatically generates the loader code so you don't have to write any of that pointer mess yourself

You just:
1. Go to the GLAD website, pick your OpenGL version (core profile), generate the files
2. Add `glad.c` to your project and include the headers
3. Call `gladLoadGL()` after your window/context is created

## Quick Summary of the Setup Flow
1. **Get GLFW**  
	either by downloading the binaries or building it from source with Cmake which is a bit confusing tbh but apparently it is better for compatibility with you hardware

2. **Tell your project where to find GLFW**  
   - Add GLFW's `include` folder so you can `#include <GLFW/glfw3.h>`
   - Add the folder containing `glfw3.lib` (or equivalent) to library paths
   - Link against `glfw3.lib` (and `opengl32.lib` on Windows)

3. **Get GLAD**  
   - Generate files from glad.dav1d.de for OpenGL ≥3.3 core
   - Add `glad.c` to your project
   - Add the generated `include` folders

4. **Include order in your code**  
   ```c
   #include <GLFW/glfw3.h>  // must come first
   #include <glad/glad.h>   // then GLAD
   ```

And that's it 

The whole point of GLFW and GLAD is that they make it easier for you to get a OpenGl Context easily without too much work 