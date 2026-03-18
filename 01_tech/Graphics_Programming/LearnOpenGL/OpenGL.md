# OpenGL Basics 

**OpenGL, DirectX, and Vulkan** aren't programming languages—they're **APIs**. More precisely, they're detailed **specification rulebooks** that GPU manufacturers (like NVIDIA, AMD, Intel) follow to implement graphics features on their hardware.

Since they're APIs, you write code using a real programming language—mostly **C++**—to call their functions.

## Old vs Modern OpenGL
- There was an old style called **immediate mode** (using stuff like `glBegin()` and `glEnd()`). It super easy but hid a lot of what was really going on under the hood.
- It got deprecated because developers wanted more control and better performance. That's why they introduced the **core profile** (starting around OpenGL 3.0+), which forces you to use modern techniques like shaders and buffer objects.

## Extensions
Extensions are a cool way to add new features or optimizations to OpenGL without waiting for a full new version.  
If your GPU supports it, you can load and use the extension—great for getting cutting-edge stuff early.

## State Machine Nature
OpenGL is heavily **state-based**. It has a big global **context** (like a master configuration) that remembers things like current color, bound textures, etc.  
You change the state with functions, and future commands use whatever the current state is.

## Why the Object Abstraction?
OpenGL is written in C, which doesn't translate super well to higher-level languages. To make managing all that state easier, they introduced **objects**.

An **object** in OpenGL is basically a bundle of settings/options that controls part of the big state machine.  
For example: an object might hold window settings (size, color depth, etc.) or contain data + config for a 3D model.

Think of it like a C struct:
```c
struct some_object {
    float width;
    int colors;
    char name[];
    // etc.
};
```

The whole OpenGL **context** is like one massive struct with slots (called *targets*) where you plug in these objects.

### The Classic Workflow (Bind to Use/Modify)
You always follow this pattern:

1. **Create** the object and get an ID (data is hidden by the driver):
   ```c
   unsigned int myObject = 0;
   glGenWhatever(1, &myObject);
   ```

2. **Bind** it to a slot in the context:
   ```c
   glBindWhatever(SOME_TARGET, myObject);
   ```

3. Now modify settings—they go into the bound object:
   ```c
   glSetOption(SOME_TARGET, WIDTH, 800);
   glSetOption(SOME_TARGET, HEIGHT, 600);
   ```

4. **Unbind** when done (set back to 0):
   ```c
   glBindWhatever(SOME_TARGET, 0);
   ```

### Why This is Awesome
- Create multiple objects, configure them once.
- Later, just bind the one you want—all its settings instantly become active.
- Perfect for things like **VAOs** (Vertex Array Objects) that store model data and vertex setup. Bind it → draw the model → no need to reconfigure everything.

It's all designed this way because OpenGL is one giant **state machine**, and objects let you swap configurations quickly.
