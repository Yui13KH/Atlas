
Setting up even a simple window with a color in OpenGL (or well the general setting up the initial part) is kinda confusing. It makes sense logically but it's kinda confusing a bit so i'll rewrite what i understood

## Includes Order Matters
```cpp
#include <glad/glad.h>   // first!!
#include <GLFW/glfw3.h>
```
We include **glad.h** before **glfw.h** because if you do it the other way you get the old OpenGL headers and weird conflicts. By including glad first you get the modern OpenGL definitions you asked for, and glfw notices that and skips pulling in the old system OpenGL 1.x headers.

## Initializing GLFW
To get anything going you first need to initialize glfw and give it some config hints so it knows exactly what kind of window and OpenGL context you want.

```cpp
glfwInit();  // just initializes glfw
```

A **hint** is basically just a suggestion you give to glfw about how you'd like something to behave or be configured. I had problems understanding this before looking it up.

So we set the hints:
```cpp
glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
```
This tells glfw: give me an OpenGL 3.3 context in core profile

## Creating the Window
```cpp
GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "Test", NULL, NULL);
```

**GLFWwindow*** window is just a pointer to an **opaque struct** — meaning glfw hides all the messy internal details (different per OS and driver). You never see or touch the insides directly; you just get a pointer to it and use glfw functions to control it.

**glfwCreateWindow** args go like (width, height, title, monitor, share):
- monitor: if you pass a monitor pointer it goes fullscreen on that monitor; NULL = normal windowed mode
- share: pointer to another GLFWwindow to share OpenGL objects (textures, buffers, etc.) with it; NULL = no sharing

Since we're just doing a simple example we leave both as NULL.

Safety check:
```cpp
if (window == NULL)
{
    std::cout << "Failed to create GLFW window" << std::endl;
    glfwTerminate();
    return -1;
}
```
**glfwTerminate** cleans up everything glfw allocated (context, window, etc.) and frees the memory.

## Making the Window Active
```cpp
glfwMakeContextCurrent(window);
glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
```

**glfwMakeContextCurrent** tells OpenGL and the driver "this is the window/context we're working with right now".

**glfwSetFramebufferSizeCallback** registers our function so glfw calls it automatically whenever the window is resized (so we can update the viewport).

## Loading OpenGL Functions with GLAD
```cpp
if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
{
    std::cout << "Failed to initialize GLAD" << std::endl;
    return -1;
}
```

This checks if GLAD successfully loaded all the modern OpenGL function pointers. GLAD doesn't "load" the code — it just queries the driver for the addresses of each function and stores them so we can call them normally.

The weird cast is just C wierdness to make the compiler happy — glfwGetProcAddress has the exact same signature as what glad expects, but different type names, so we force-cast it.

It returns 1 on success, 0 on failure, so we flip it with ! to enter the error block if something went wrong.

## Input Handling
**processInput** is the function that processes input (wow i know). GLFW sets up all the low-level input stuff for you, but you have to decide what you actually want to do with it (key presses, mouse, etc.).

Example:
```cpp
void processInput(GLFWwindow* window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}
```
For the given window, check if escape is pressed — if yes, set the internal "should close" flag to true.

## The Main Loop
```cpp
while (!glfwWindowShouldClose(window))
{
    processInput(window);

    glClearColor(0.98f, 0.58f, 0.68f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    glfwSwapBuffers(window);
    glfwPollEvents();
}
```

**glfwWindowShouldClose** returns true when it's time to close, so ! flips it to keep the loop running while the window should stay open.

Inside the loop:
- process input (runs every frame obviously)
- **glClearColor** sets the color we want to "clear" with (values 0.0–1.0 for RGBA — yeah convert from 0-255 yourself or write a helper)
- **glClear** actually fills the entire back buffer with that color (the name "clear" is historical — it's really just painting the background)
- **glfwSwapBuffers** swaps the back buffer (what we just drew to) with the front buffer (what's currently on screen). Double buffering prevents tearing and artifacts.

## The Hidden State Thing
One thing that confused me a lot at first: most OpenGL functions are void — so how does **glClearColor** tell **glClear** which color to use?

Answer: OpenGL is a giant **state machine**. There's one huge hidden context struct managed by the driver that holds thousands of settings. **glClearColor** just writes to a field in that hidden struct, and **glClear** reads the current value from the same field. The functions don't pass data directly to each other — they both talk to the same global state.

## Final Result
If everything is set up correctly you get a nice solid-color window (pink in this case). Change the RGBA values and you get whatever color you want.

Window width/height are usually defined as **const unsigned int** (or just const unsigned) because size can't be negative and the resize callback will handle any changes anyway — those constants are just the initial size.