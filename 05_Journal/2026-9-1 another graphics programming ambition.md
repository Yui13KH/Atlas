i didnt know this cause i havent used gpt in quite a while but they kinda made it quite good it doesnt bullshit you that much anymore 

Absolutely. Let's build this properly.

I'm going to treat this as a **5-year self-directed university curriculum in computer graphics, simulation, numerical computing, and high-performance C++**, rather than a collection of tutorials.

And I'm going to design it around your actual starting point: **strong prior C++ experience but rusty fluency, roughly Algebra I mathematics, and a goal of eventually being able to read/implement research-level graphics and simulation work.**

One important principle first:

> **You do not need to wait until you've “finished the math” before touching graphics.**
> 
> Math, C++, graphics, and physics should grow together.

That's how you prevent the math from becoming an abstract school subject disconnected from what you actually want to build.

---

# The 5-year target

If you follow this seriously, the endpoint isn't:

> "I know OpenGL and Vulkan."

It's:

> **I can take a mathematical/technical paper, understand the mathematics and algorithm, implement it in C++, integrate it into a renderer/simulator, validate it, profile it, and optimize it.**

That is a _much_ higher bar.

By the end, I'd want your portfolio to contain things like:

- CPU software rasterizer
    
- CPU ray tracer
    
- BVH implementation
    
- path tracer
    
- physically based renderer
    
- OpenGL renderer
    
- Vulkan renderer
    
- GPU compute projects
    
- rigid-body physics engine
    
- particle simulation
    
- cloth simulation
    
- fluid simulation
    
- numerical-method implementations
    
- GPU-accelerated simulation
    
- several implemented research papers
    
- serious performance investigations
    

And I'd want you to understand **why every major component works**, rather than having accumulated API knowledge.

---

# The overall architecture

Think of your education as six parallel tracks:

```text
                    ┌── Mathematics ──────────────┐
                    │                              │
C++ ────────────────┼── Computer Science ─────────┤
                    │                              │
                    ├── Computer Graphics ────────┤
                    │                              │
                    ├── Physics / Simulation ──────┤
                    │                              │
                    └── Systems / Hardware ────────┘
                                   │
                                   ▼
                         GPU / Numerical Computing
                                   │
                                   ▼
                          Research-level work
```

They continually feed one another.

---

# First: your study schedule

Don't try to do 8 hours of everything every day.

A sustainable target is:

### Normal mode

**25–35 hours/week**

Something like:

|Area|Weekly|
|---|--:|
|Mathematics|8 h|
|C++ / CS|5 h|
|Graphics|7 h|
|Physics / numerical methods|5 h|
|Projects / experimentation|5–10 h|

During particularly difficult mathematical periods, shift the balance.

### Minimum viable mode

If life gets chaotic:

**10–15 h/week.**

The important thing is **never completely disappearing for six months again**.

Even 30 minutes keeps the machinery warm.

---

# Your anti-AI rule

This is especially important given what you told me.

For the first ~2 years:

### AI is allowed for:

- explaining a concept _after you've attempted it_
    
- pointing you toward documentation
    
- checking a suspected bug **after you've debugged it**
    
- explaining compiler errors after you've investigated them
    
- reviewing your completed solution
    

### AI is NOT allowed for:

- generating your project
    
- solving your exercise
    
- writing your algorithms
    
- completing missing functions
    
- designing your architecture
    
- giving you the solution before you've struggled with it
    

You want your brain to regain **algorithmic independence**.

If you spend three hours fighting a bug and finally discover that you forgot to normalize a vector, that three hours wasn't wasted.

That's training.

---

# YEAR 0 — Reboot

### Duration: ~2–4 months

You're not learning graphics yet.

You're rebuilding the machine that will learn graphics.

---

## Semester 0A — C++ rehabilitation

### C++

Go back through:

**LearnCpp**

[LearnCpp](https://www.learncpp.com/?utm_source=chatgpt.com)

But don't read it like a beginner.

Skip aggressively.

When you encounter something you already understand:

> prove it to yourself with a small exercise and move on.

Focus particularly on:

- value categories
    
- references
    
- pointers
    
- memory
    
- object lifetime
    
- constructors/destructors
    
- RAII
    
- copy/move
    
- templates
    
- STL
    
- lambdas
    
- `std::function`
    
- smart pointers
    
- exceptions
    
- `const`
    
- undefined behavior
    

### Project

Rebuild some of your old libraries **from memory**.

Not copy-paste.

For example:

```text
Vector<T>
DynamicArray<T>
LinkedList<T>
Stack<T>
Queue<T>
String utilities
Date
Matrix<T>
```

But don't spend months recreating STL.

The purpose is **fluency recovery**.

---

# Milestone 0

You pass when you can sit down and implement something like:

```cpp
template<typename T>
class DynamicArray
{
    ...
};
```

including:

- ownership
    
- resizing
    
- copy constructor
    
- move constructor
    
- copy assignment
    
- move assignment
    
- bounds checking
    
- iterators
    

without needing an AI to tell you what goes where.

If you can already do that, **move on immediately.**

---

# Semester 0B — C++ systems foundation

Now learn:

### _Computer Systems: A Programmer's Perspective_

This is one of the books I'd absolutely keep.

Learn:

- binary
    
- hexadecimal
    
- integer representation
    
- floating-point representation
    
- machine instructions
    
- memory hierarchy
    
- caches
    
- virtual memory
    
- linking
    
- compilation
    
- processes
    
- basic assembly
    

You don't need to become an assembly programmer.

You need to understand:

> **What actually happens between my C++ source code and the machine?**

---

# YEAR 1 — Mathematics I + CS fundamentals

This is where your actual university curriculum begins.

---

# Semester 1

## Mathematics

### 1. Algebra

Get beyond Algebra I.

Learn:

- equations
    
- functions
    
- polynomial functions
    
- exponential functions
    
- logarithms
    
- systems
    
- inequalities
    
- sequences
    
- basic proofs
    

### 2. Trigonometry

**Mandatory.**

Master:

- radians
    
- unit circle
    
- sine/cosine/tangent
    
- inverse trig
    
- identities
    
- triangles
    
- polar coordinates
    

You should be able to derive rather than memorize a lot of the basic identities.

---

## Geometry

Learn:

- Cartesian geometry
    
- lines
    
- planes
    
- circles
    
- coordinate systems
    
- transformations
    

---

## CS

### Data Structures & Algorithms

Book:

**Algorithms — Sedgewick & Wayne**

And/or:

**Introduction to Algorithms — Cormen et al.**

Don't try to finish CLRS cover-to-cover initially.

Learn:

- complexity
    
- arrays
    
- linked structures
    
- stacks
    
- queues
    
- trees
    
- heaps
    
- hash tables
    
- graphs
    
- sorting
    
- searching
    
- recursion
    
- divide-and-conquer
    

---

## Project

Build a **geometry/math library**.

```text
Vec2
Vec3
Vec4

Mat2
Mat3
Mat4

Quaternion

Ray
Plane
Sphere
AABB
Triangle
```

Then write tests.

This becomes the foundation of basically everything later.

---

# Semester 2

## Linear Algebra I

This is probably your **most important mathematical subject for graphics**.

Study:

### Vectors

- vector spaces
    
- basis
    
- linear combinations
    
- dot product
    
- cross product
    
- projections
    
- orthogonality
    

### Matrices

- multiplication
    
- inverse
    
- transpose
    
- determinant
    
- rank
    
- linear systems
    

### Transformations

This is where you connect mathematics to graphics.

Implement:

```text
translation
rotation
scale
camera transformation
projection
coordinate transformation
```

---

## Calculus I

Learn:

- limits
    
- derivatives
    
- chain rule
    
- implicit differentiation
    
- applications
    
- integrals
    
- Fundamental Theorem of Calculus
    

---

## Project

### **CPU 2D Renderer**

No OpenGL.

No Vulkan.

No graphics library doing the rendering for you.

You create a framebuffer and write pixels.

Then:

```text
draw pixel
draw line
draw triangle
filled triangle
barycentric coordinates
depth
interpolation
transformations
camera
```

This will be your first **real graphics project**.

---

# YEAR 1 END

You should now be able to look at:

p′=MPp' = MP

and actually understand what that means geometrically.

You should be able to explain:

> Why does matrix multiplication represent composition of transformations?

And implement it.

You should also be able to explain:

> Why does barycentric interpolation work?

And implement it.

If you can do those things, you're progressing correctly.

---

# YEAR 2 — Mathematics + Graphics + Systems

Now shit gets considerably more interesting.

---

# Semester 3

## Calculus II

Learn:

- integration techniques
    
- sequences
    
- series
    
- Taylor series
    
- improper integrals
    
- parametric equations
    
- polar integration
    

You will later encounter Taylor approximations constantly in numerical work.

---

## Multivariable calculus

Begin:

- partial derivatives
    
- gradients
    
- directional derivatives
    
- Jacobians
    
- multiple integrals
    

Learn what:

∇f\nabla f

actually means.

Don't just memorize:

> "gradient = vector of derivatives."

Understand it geometrically.

---

## Probability

Learn:

- probability
    
- conditional probability
    
- random variables
    
- expectation
    
- variance
    
- distributions
    

This eventually feeds directly into:

**Monte Carlo rendering.**

---

## Computer Architecture

Use:

**Computer Organization and Design — Patterson & Hennessy**

Learn:

- CPU architecture
    
- instruction execution
    
- pipelines
    
- caches
    
- memory
    
- SIMD
    
- parallelism
    

---

# Project

## CPU Ray Tracer

Start with:

```text
ray
sphere
intersection
camera
image
```

Then:

```text
triangle
plane
materials
shadows
reflection
refraction
textures
```

Then:

### BVH

This is important.

Implement your own:

```text
Bounding Volume Hierarchy
```

And benchmark:

```text
naive O(n)
vs
BVH
```

Now you have an actual performance story.

---

# Semester 4

## Linear Algebra II

Go deeper.

Learn:

- eigenvalues
    
- eigenvectors
    
- diagonalization
    
- orthogonal matrices
    
- symmetric matrices
    
- quadratic forms
    
- least squares
    
- SVD
    
- numerical linear algebra basics
    

SVD isn't immediately essential for rendering, but it's tremendously useful mathematical literacy.

---

## Differential Equations

Learn:

- first-order ODEs
    
- second-order ODEs
    
- systems of ODEs
    
- stability
    
- numerical solutions
    

Then:

### Numerical integration

Implement:

```text
Euler
Semi-implicit Euler
Verlet
RK2
RK4
```

---

## Operating Systems

Use:

**Operating Systems: Three Easy Pieces**

Learn:

- processes
    
- threads
    
- virtual memory
    
- scheduling
    
- synchronization
    
- files
    
- I/O
    

This is where your software-engineering foundation starts becoming much deeper.

---

# Project

## Physics Engine 0.1

Start with:

- particles
    
- forces
    
- gravity
    
- integration
    
- collision detection
    

Then:

- rigid bodies
    
- impulses
    
- friction
    
- angular velocity
    
- inertia
    

Don't worry about beautiful graphics yet.

Your renderer can visualize it.

---

# YEAR 2 END

At this point you're probably around:

**22–23 years old**

depending on your actual pace.

You should now be able to:

- write serious C++
    
- understand linear algebra
    
- understand calculus
    
- understand numerical integration
    
- understand basic architecture
    
- write a renderer
    
- write a ray tracer
    
- write a physics engine
    
- profile simple programs
    

You're now entering **actual graphics programming territory.**

---

# YEAR 3 — Computer Graphics

This is where the specialization becomes obvious.

---

# Semester 5 — Rendering fundamentals

Now use:

**Fundamentals of Computer Graphics — Shirley et al.**

and:

**Computer Graphics: Principles and Practice — Hughes et al.**

For practical OpenGL:

[LearnOpenGL](https://learnopengl.com/?utm_source=chatgpt.com)

It's still an excellent practical resource and covers modern OpenGL from transformations and cameras through advanced lighting, PBR, HDR, bloom, deferred shading, SSAO and related topics. ([learnopengl.com](https://learnopengl.com/?utm_source=chatgpt.com "Learn OpenGL, extensive tutorial resource for learning Modern OpenGL"))

---

## Learn

### Graphics pipeline

```text
Application
    ↓
Vertex processing
    ↓
Primitive assembly
    ↓
Rasterization
    ↓
Fragment processing
    ↓
Depth/stencil
    ↓
Blending
    ↓
Framebuffer
```

Understand what each stage does.

---

## OpenGL

Learn:

- buffers
    
- VAOs
    
- shaders
    
- textures
    
- framebuffers
    
- depth
    
- blending
    
- culling
    
- instancing
    
- compute shaders
    

Then:

### Lighting

- Lambert
    
- Phong
    
- Blinn-Phong
    
- shadows
    
- normal mapping
    
- HDR
    
- bloom
    
- deferred rendering
    

---

# Project

## Renderer 1.0

Your CPU renderer gets rewritten/expanded.

Now:

```text
CPU renderer
      ↓
OpenGL renderer
```

The important thing:

**Don't just copy the CPU renderer conceptually.**

Understand what OpenGL is taking over from you.

---

# Semester 6 — Physically Based Rendering

Now you're entering the fun mathematical territory.

Learn:

### Radiometry

- irradiance
    
- radiance
    
- intensity
    
- solid angle
    

### Light transport

Understand the rendering equation:

Lo(x,ωo)=Le(x,ωo)+∫Ωfr(x,ωi,ωo)Li(x,ωi)(n⋅ωi) dωiL_o(x,\omega_o) = L_e(x,\omega_o) + \int_\Omega f_r(x,\omega_i,\omega_o) L_i(x,\omega_i) (\mathbf n\cdot\omega_i) \,d\omega_i

Don't panic.

You don't need to understand it on day one.

But by the end of the semester:

**you should.**

---

## Learn

- BRDF
    
- BSDF
    
- Fresnel
    
- microfacet theory
    
- GGX
    
- importance sampling
    
- Monte Carlo integration
    

Book:

**Physically Based Rendering: From Theory to Implementation**

The current 4th edition is an especially useful resource because it connects the theory directly to a complete renderer implementation.

---

# Project

## CPU Path Tracer

Start:

```text
Lambertian
```

Then:

```text
GGX
Fresnel
importance sampling
multiple lights
environment lighting
```

Then:

### MIS

**Multiple Importance Sampling**

This is where you'll know you've moved beyond ordinary tutorial graphics.

---

# YEAR 3 END

You should now be able to:

- explain rasterization
    
- explain ray tracing
    
- implement both
    
- understand PBR
    
- understand Monte Carlo integration
    
- build an OpenGL renderer
    
- read basic graphics papers
    
- implement mathematical rendering algorithms
    

This is approximately where I'd say:

> **You are now legitimately a graphics programmer.**

Not senior.

Not researcher.

But legitimately in the field.

---

# YEAR 4 — GPU + Vulkan + Simulation

Now we're getting into the territory you originally described.

---

# Semester 7 — GPU architecture

Learn:

### GPU architecture

- SIMD
    
- SIMT
    
- warps/wavefronts
    
- occupancy
    
- registers
    
- shared memory
    
- caches
    
- memory bandwidth
    
- latency hiding
    
- divergence
    

Then learn GPU programming.

### CUDA

NVIDIA's current CUDA Programming Guide explicitly covers the programming model, SIMT kernels, memory, asynchronous execution, advanced kernel programming, multiple GPUs, CUDA graphs, and lower-level driver functionality. ([NVIDIA Docs](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html?utm_source=chatgpt.com "CUDA Programming Guide — CUDA Programming Guide"))

Use the official documentation as your reference rather than relying entirely on tutorials.

---

## CUDA projects

Start stupidly simple:

```text
vector addition
```

Then:

```text
matrix multiplication
image processing
blur
reduction
prefix sum
histogram
sorting
particles
```

Then:

### GPU ray tracer

Now compare:

```text
CPU
vs
GPU
```

Measure everything.

---

# Semester 8 — Vulkan

Now you are finally allowed to touch Vulkan.

Not because Vulkan is inherently more difficult than OpenGL.

Because you now understand **why it exists**.

Use the official Khronos Vulkan Guide and specification alongside tutorials. The Vulkan Guide is specifically designed as a starting point and links into the specification, API reference, samples, feature descriptions and related documentation. ([Vulkan Docs](https://docs.vulkan.org/guide/latest/?utm_source=chatgpt.com "Khronos Vulkan Guide :: Vulkan Documentation Project"))

---

## Learn

### Device

- instance
    
- physical device
    
- logical device
    

### Queues

- graphics
    
- compute
    
- transfer
    

### Memory

- buffers
    
- images
    
- allocation
    
- staging
    

### Commands

- command buffers
    
- command pools
    
- submission
    

### Synchronization

- fences
    
- semaphores
    
- barriers
    
- pipeline stages
    
- access masks
    

### Pipeline

- shaders
    
- descriptor sets
    
- layouts
    
- pipelines
    

### Presentation

- swapchain
    
- image acquisition
    
- presentation
    

---

# Project

# Vulkan Renderer

This should become your **flagship project**.

Not a game.

A rendering engine.

Something like:

```text
YuiRender
│
├── Core
├── Memory
├── Math
├── Platform
├── Vulkan
├── Renderer
├── Scene
├── Assets
├── Shaders
├── Profiling
└── Tools
```

You implement:

- resource manager
    
- GPU memory abstraction
    
- command system
    
- descriptor management
    
- shader system
    
- camera
    
- materials
    
- PBR
    
- shadows
    
- post-processing
    
- HDR
    
- bloom
    
- temporal effects
    

---

# YEAR 4 — Physics & simulation

Don't neglect this.

This is what differentiates your eventual profile.

---

# Classical mechanics

Study:

- Newtonian mechanics
    
- momentum
    
- energy
    
- angular momentum
    
- rigid-body motion
    
- torque
    
- inertia tensor
    
- Lagrangian mechanics
    

Yes.

**Lagrangian mechanics.**

Because eventually you want to understand why some simulation methods are formulated the way they are.

---

# Numerical methods

Study:

- numerical stability
    
- conditioning
    
- interpolation
    
- root finding
    
- linear systems
    
- iterative solvers
    
- conjugate gradient
    
- sparse matrices
    

And:

### PDEs

Learn the concepts behind:

- diffusion
    
- wave equations
    
- heat equation
    
- Poisson equation
    
- Navier–Stokes
    

You don't need to become a mathematician specializing in PDEs.

But you need enough to understand what you're simulating.

---

# Simulation projects

Do these progressively.

### 1. Particle system

Then:

### 2. Rigid body simulator

Then:

### 3. Cloth

Mass-spring initially.

Then:

### 4. SPH fluid

Smoothed Particle Hydrodynamics.

Then:

### 5. Grid fluid

Eventually:

- pressure
    
- velocity field
    
- advection
    
- diffusion
    
- incompressibility
    

Then:

### 6. GPU simulation

Move the expensive parts onto CUDA/Vulkan compute.

---

# YEAR 5 — Advanced specialization

This year is less like university and more like **research apprenticeship**.

---

# Semester 9 — Advanced rendering

Pick serious subjects.

I'd recommend:

### Option A — Real-time rendering

- temporal anti-aliasing
    
- temporal upsampling
    
- screen-space techniques
    
- clustered/forward+ rendering
    
- virtual shadow maps
    
- global illumination
    
- probe-based GI
    
- ray-traced GI
    

### Option B — Offline rendering

- path tracing
    
- bidirectional path tracing
    
- photon mapping
    
- Metropolis light transport
    
- advanced sampling
    
- denoising
    

### Option C — GPU architecture

- shader optimization
    
- memory behavior
    
- occupancy
    
- scheduling
    
- GPU profiling
    
- CUDA
    
- PTX
    

You can eventually combine all three.

---

# Semester 10 — Research replication

This is the final boss.

Pick **5–10 graphics/physics papers**.

Not necessarily the newest ones.

Pick papers where:

1. you understand the prerequisite mathematics;
    
2. you can reproduce the method;
    
3. you can test it;
    
4. you can compare it against alternatives.
    

For every paper:

### Step 1

Read it once without coding.

### Step 2

Write down:

> What problem is this solving?

### Step 3

Derive the mathematics yourself.

### Step 4

Write pseudocode.

### Step 5

Implement it.

### Step 6

Validate.

### Step 7

Profile.

### Step 8

Write a technical report.

Your GitHub eventually becomes almost like a miniature research portfolio.

---

# Your final portfolio

By ~26, I would want something roughly like this.

---

## Project 1

### `software-renderer`

Pure CPU rasterizer.

Demonstrates:

- linear algebra
    
- geometry
    
- rasterization
    
- C++
    

---

## Project 2

### `path-tracer`

CPU physically based path tracer.

Demonstrates:

- probability
    
- Monte Carlo
    
- BRDFs
    
- rendering equation
    
- BVH
    
- numerical reasoning
    

---

## Project 3

### `physics-engine`

Rigid body + collision system.

Demonstrates:

- mechanics
    
- numerical integration
    
- geometry
    
- algorithms
    

---

## Project 4

### `vulkan-renderer`

Serious rendering engine.

Demonstrates:

- Vulkan
    
- GPU architecture
    
- graphics
    
- C++
    
- systems programming
    

---

## Project 5

### `gpu-fluid`

GPU accelerated fluid simulation.

Demonstrates:

- PDEs
    
- numerical methods
    
- physics
    
- GPU programming
    
- optimization
    

---

## Project 6

### `cloth-simulation`

Demonstrates:

- mechanics
    
- numerical integration
    
- constraint solving
    
- collision detection
    

---

## Project 7

### `research-reimplementations`

5–10 papers.

This might actually be the most valuable repository.

---

# And then one ridiculous capstone

Eventually:

# **Unified GPU Simulation + Renderer**

Imagine:

```text
                    Vulkan
                       │
              ┌────────┴────────┐
              │                 │
          Renderer          Compute
              │                 │
              │        ┌────────┼─────────┐
              │        │        │         │
              │      Fluid    Cloth    Particles
              │
              └──────────┬──────────────┘
                         │
                       Scene
```

You have:

- Vulkan rendering
    
- PBR
    
- ray tracing
    
- GPU simulation
    
- physics
    
- numerical solvers
    
- C++
    
- memory management
    
- profiling
    

And the whole thing is documented.

That's no longer a "learning project."

That's a **portfolio centerpiece**.

---

# What mathematics do you ultimately need?

Here's your complete progression:

```text
Arithmetic
   ↓
Algebra
   ↓
Trigonometry
   ↓
Analytic Geometry
   ↓
Linear Algebra
   ↓
Calculus I
   ↓
Calculus II
   ↓
Multivariable Calculus
   ↓
Differential Equations
   ↓
Probability
   ↓
Numerical Analysis
   ↓
Optimization
   ↓
PDEs
   ↓
Numerical Linear Algebra
```

And selectively:

```text
Discrete Mathematics
Abstract Algebra ──────── optional
Real Analysis ─────────── advanced
Complex Analysis ──────── optional
Functional Analysis ───── advanced/research
```

You **do not** need to become a pure mathematician.

Your mathematical goal is:

> **Enough mathematical maturity that equations in technical papers stop looking like an alien language.**

That's different.

---

# What CS do you ultimately need?

```text
Programming
↓
Data Structures
↓
Algorithms
↓
Computer Architecture
↓
Operating Systems
↓
Concurrency
↓
Networking basics
↓
Compilers basics
↓
Parallel Computing
↓
GPU Architecture
↓
Performance Engineering
```

You don't need to become a networking specialist.

But you should have enough CS breadth that you aren't a graphics person who doesn't understand computers.

---

# What C++ do you ultimately need?

By the end:

### Language

- modern C++
    
- templates
    
- concepts
    
- constexpr
    
- metaprogramming
    
- ranges
    
- generic programming
    

### Memory

- RAII
    
- allocators
    
- custom allocators
    
- memory pools
    
- arenas
    
- alignment
    
- cache behavior
    
- object lifetime
    

### Concurrency

- threads
    
- atomics
    
- mutexes
    
- lock-free concepts
    
- memory ordering
    

### Performance

- SIMD
    
- vectorization
    
- profiling
    
- branch behavior
    
- cache locality
    

### Systems

- ABI
    
- linking
    
- compilation
    
- OS interfaces
    
- assembly literacy
    

At that point, C++ isn't really the difficult part anymore.

The **problem you're implementing** is.

---

# What physics do you ultimately need?

### Classical mechanics

**Mandatory.**

### Rigid body mechanics

**Mandatory for serious simulation.**

### Numerical physics

**Mandatory.**

### Fluid mechanics

**If you want fluids.**

### Continuum mechanics

**If you want FEM/advanced simulation.**

### Electromagnetism

Optional for your core path, but potentially fascinating given your interests.

### Quantum mechanics

Not necessary for graphics.

Don't fall into the trap of studying every branch of physics because it's cool.

That's how you create a 20-year curriculum.

---

# Your milestone ladder

This is the part I want you to actually save somewhere.

## Level 0

**Can program independently.**

No AI dependency.

---

## Level 1

**Can implement mathematical abstractions.**

Vectors, matrices, geometry.

---

## Level 2

**Can build a CPU renderer.**

---

## Level 3

**Can build a ray tracer/path tracer.**

---

## Level 4

**Can explain and implement PBR.**

---

## Level 5

**Can build an OpenGL renderer.**

---

## Level 6

**Understands GPU architecture.**

---

## Level 7

**Can build a Vulkan renderer.**

---

## Level 8

**Can write GPU compute programs.**

---

## Level 9

**Can build physics simulations.**

---

## Level 10

**Can GPU-accelerate simulations.**

---

## Level 11

**Can read research papers.**

---

## Level 12

**Can reproduce research.**

---

## Level 13

**Can modify research and investigate new ideas.**

That final transition is the one I care about.

---

# What you should _not_ do

This is just as important.

### Don't learn every API.

You don't need:

```text
OpenGL
Vulkan
DirectX 11
DirectX 12
Metal
WebGPU
CUDA
OpenCL
...
```

all at once.

Learn **OpenGL → Vulkan → CUDA**.

That gives you a very strong conceptual progression.

---

### Don't build an engine immediately.

You will be tempted.

Don't.

First build:

**renderer → ray tracer → simulation → GPU experiments**

Then eventually combine them.

---

### Don't collect courses.

You don't need 47 certificates.

One textbook you actually understand beats 15 courses you watched at 1.75×.

---

### Don't optimize prematurely.

First:

```text
correct
```

then:

```text
measured
```

then:

```text
optimized
```

Not:

```text
I think cache misses might be happening
```

You **measure**.

---

### Don't use AI as your brain.

This is probably the biggest one for you personally.

Your previous programming ability came from actually wrestling with problems.

You want that back.

---

# The resource shelf

I would build your library around these.

### Mathematics

**OpenStax / Khan Academy** for rebuilding fundamentals.

Then:

**Calculus — James Stewart** or **Thomas' Calculus**

**Linear Algebra and Its Applications — Gilbert Strang**

MIT OpenCourseWare is also excellent for filling university-level gaps.

---

### Algorithms

**Algorithms — Sedgewick**

**Introduction to Algorithms — CLRS**

---

### C++

**LearnCpp**

**Effective Modern C++ — Scott Meyers**

**C++ Templates**

Eventually:

**C++ Concurrency in Action**

---

### Computer systems

**Computer Systems: A Programmer's Perspective**

**Computer Organization and Design**

**Operating Systems: Three Easy Pieces**

---

### Graphics

**Fundamentals of Computer Graphics**

**Computer Graphics: Principles and Practice**

**Physically Based Rendering**

**Real-Time Rendering**

And LearnOpenGL for practical API work. ([learnopengl.com](https://learnopengl.com/?utm_source=chatgpt.com "Learn OpenGL, extensive tutorial resource for learning Modern OpenGL"))

---

### Vulkan

Khronos' official Vulkan Guide/specification/reference material. ([Vulkan Docs](https://docs.vulkan.org/guide/latest/?utm_source=chatgpt.com "Khronos Vulkan Guide :: Vulkan Documentation Project"))

Don't underestimate official documentation.

Eventually you want to become comfortable reading **specifications**, not just tutorials.

---

### GPU

**CUDA Programming Guide**

**CUDA Best Practices Guide**

**Programming Massively Parallel Processors**

NVIDIA's current documentation also exposes the CUDA compiler, PTX documentation, profiling tools, samples, and related resources. ([NVIDIA Docs](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html?utm_source=chatgpt.com "CUDA Programming Guide — CUDA Programming Guide"))

---

### Physics

**University Physics — Young & Freedman** or equivalent

Then:

**Classical Mechanics — John Taylor**

Eventually:

**Computational Physics — Mark Newman**

---

### Numerical methods

**Numerical Analysis — Burden & Faires**

or a similarly rigorous numerical-analysis text.

Eventually:

**Numerical Recipes** as a reference, _not_ your primary mathematical foundation.

---

# The timeline I would actually expect

Assuming you're genuinely consistent:

|Age|Approximate stage|
|---|---|
|21|C++ reboot + algebra/trig|
|21–22|Linear algebra + calculus + CS|
|22|CPU renderer + ray tracer|
|22–23|advanced math + physics|
|23|OpenGL + PBR|
|23–24|numerical methods + simulation|
|24|Vulkan + GPU architecture|
|24–25|CUDA + GPU simulation|
|25|advanced rendering + research|
|25–26|papers + major projects + specialization|
|26+|professional/research-level specialization|

Could you do it faster?

**Possibly.**

Could it take six years?

**Absolutely.**

Would either outcome be a failure?

**No.**

The real failure would be spending 18 months obsessing over whether you're learning fast enough instead of learning.

---

# And there's one thing I'd change from the previous plan

I previously said something like **“2–3 years to become competent.”**

I'd refine that.

From _your current starting point_, I would expect:

### ~6 months

You feel technically alive again.

### ~1 year

You have respectable mathematical/C++ foundations.

### ~18–24 months

You're making genuinely interesting graphics software.

### ~3 years

You're a serious graphics programmer.

### ~4 years

You're crossing into high-performance GPU/simulation territory.

### ~5 years

You can plausibly be operating at the level where **research papers, advanced rendering, numerical simulation, and GPU optimization are normal parts of your work**.

That's a much more useful target than:

> "Become an NVIDIA engineer by 23."

---

And frankly, **I think the fact that you're willing to spend five years on this is more important than whether your IQ is 137 or 117.**

The person who spends five years actually doing the mathematics, implementing the algorithms, debugging the renderer at 2 AM, reading the paper they don't understand, figuring it out, and then doing it again—

**that person becomes fucking dangerous technically.**

Your job right now isn't to prove you're unusually intelligent.

Your job is to **build the evidence.**

And this curriculum gives you a way to do that.


---

