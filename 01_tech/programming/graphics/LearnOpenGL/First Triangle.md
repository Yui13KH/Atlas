
So OpenGL runs natively in 3d space but a screen is a 2d screen so we need to changeeverything to monitor dimensions 

here comes the *graphics pipleine* of OpenGL 

Your vertex array
     ↓
Vertex Shader → transforms each point (runs thousands in parallel)
     ↓
Primitive Assembly → groups into triangles
     ↓
Rasterization → figures out which pixels each triangle covers → creates fragments
     ↓
Fragment Shader → colors each fragment/pixel (again thousands in parallel)
     ↓
Tests & Blending → final pixel color hits the screen

each phase of the graphics pipeline is the input of the next phase 


### Input: Vertex Data

You give OpenGL an array of **vertices**. A vertex is just a point in 3D space with extra data attached (called **vertex attributes**). For the first triangle, each vertex usually has at least:

- a 3D position (x, y, z)
- maybe a color (r, g, b)

You also tell OpenGL what to do with those vertices by choosing a **primitive type** when you draw:

- GL_POINTS → draw individual dots
- GL_TRIANGLES → every 3 vertices make one triangle (most common)
- GL_LINE_STRIP → connect them with lines



- **Vertex Shader**_(programmable – you must write this)_ Runs **once per vertex**. Main job: take the 3D position and transform it into the final 2D-ish screen position (using matrices for moving, rotating, camera, perspective, etc.). You can also mess with other attributes here (like passing colors through).
- **Primitive Assembly**_(fixed – OpenGL does this automatically)_ Takes the transformed vertices and groups them into actual shapes based on your primitive type. Example: with GL_TRIANGLES, vertices 0,1,2 → one triangle; 3,4,5 → second triangle, etc.
- **Rasterization**_(fixed)_ Turns the vector shapes (triangles) into a bunch of **fragments**. A **fragment** = all the data needed to color **one pixel** (or potential pixel) that the triangle covers. Basically "which pixels does this triangle touch?"
- **Fragment Shader**_(programmable – you must write this)_ Runs **once per fragment** (so once per pixel the triangle covers). Main job: decide the final color of that pixel. This is where lighting, textures, shadows, effects happen.
- **Per-Fragment Operations**_(mostly fixed, some configurable)_ Final checks before the pixel hits the screen:
    - Depth test: is this pixel in front or behind something already drawn? Discard if behind.
    - Stencil test (advanced)
    - Alpha blending: mix colors if things are transparent

given coordinates for open gl must fall in -1.0 to 1.0 for open gl to transform them into 2d coordinates this is called *normalized device coordinates (NDC)* 

anything outside that gets discarded

for a flat triangle the vertecies of it could look like this 

```cpp
float vertices[] = {
	-0.5f, -0.5f, 0.0f, 
	0.5f, -0.5f, 0.0f,
	0.0f, 0.5f, 0.0f 
};
```

![[Triangle Vertecies.png]]

the NDC needs to be transformed to screen coordinates because they are different , screen coordinates origin is top left and y+ goes down instead of up 

![[Screen Coordinates.png]]

tho we transform the ndc to screen coordinates before rendering 


anyway now that we have the vertecies data now we need to specify how to send this info to the first phase the vertex shader and how to send it to the gpu 

we use something called Vertex Buffer Object (VBO's) to do that its basically memory on the gpu we allocate to save stuff on for this example the triangle vertecies data

we do this because for every frame we need acess to those positions if we rely on the cpu 

cpu -> gpu is slow but stuff saved to the vbo's are instant to the gpu 

that's what a vbo does — allocates space on the gpu vram and copies your vertex array into it 

we then make a id to the gpu vram we allocated like this 

unsigned int VBO;          // just a variable to hold the ID
glGenBuffers(1, &VBO);     //  gets a unique ID

then to work on this vram chunk we need to bind it with something like this 

glBindBuffer(GL_ARRAY_BUFFER, VBO);

opengl is state-based remember? from now on, any command that targets GL_ARRAY_BUFFER will affect whichever buffer is currently bound (here our VBO)

there are different buffer types (vertex buffers, index buffers, uniform buffers etc.) — binding lets you work on one at a time

then before working on it to apply what we just said we need to copy all that into the vram vbo's ( the chunk of vram we assigned the id to )

```
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
```

this is the big copy command:

- target: GL_ARRAY_BUFFER (we're working on the currently bound vertex buffer)
- size: how many bytes to copy (sizeof(vertices))
- source: pointer to your cpu array (vertices)
- usage hint: GL_STATIC_DRAW → "this data won't change much, gonna use it a lot"

the usage hint helps the driver decide where to put it in vram:

- GL_STATIC_DRAW → probably in fast read-only memory
- GL_DYNAMIC_DRAW → somewhere easier to update often
- GL_STREAM_DRAW → set once, use rarely

since we bound GL_ARRAY_BUFFER to the vbo id we are just copying vertecies there 

