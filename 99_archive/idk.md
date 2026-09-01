This is a **compressed, dense, no-fluff 12-month roadmap**.

Each month contains:

- Core Objectives
    
- Concepts You Must Encounter (so you know what exists)
    
- Implementation Targets
    
- Resources (inline)
    
- What to Google / search
    
- End-of-month Capstone
    
- Devlog idea
    


---

# YEAR 1 — Graphics & Simulation Engineering

---

# MONTH 1 — Math Foundations + Numerical Motion

## Core Objective

Understand vectors, matrices, derivatives, and basic numerical integration deeply enough to simulate motion.

---

## Study

### 📘 3D Math Primer for Graphics and Game Development — Dunn & Parberry

Focus on:

- Vector operations
    
- Dot product geometric meaning
    
- Cross product geometric meaning
    
- Matrix multiplication
    
- Transform composition
    

### 📘 Stewart Calculus (selected)

Focus only on:

- Derivatives
    
- Basic integrals
    
- Relationship between position / velocity / acceleration
    

---

## Concepts You Must Encounter

Search and understand:

- Linear transformation
    
- Basis vectors
    
- Coordinate systems
    
- Change of basis
    
- Numerical integration
    
- Explicit Euler method
    
- Time step stability
    
- Floating point precision basics
    
- Energy drift
    

---

## Implementation

- Dynamic array in C
    
- Vec2 / Vec3
    
- Mat3 / Mat4
    
- Rotation matrices (derive manually)
    
- Projectile motion simulation
    
- Particle system (100–1000 particles)
    
- Adjustable timestep
    

Add:

- Pause
    
- Single-step simulation
    
- Change gravity live
    

---

## What to Search

- “Why Euler integration is unstable”
    
- “Floating point accumulation error example”
    
- “Geometric interpretation of dot product”
    
- “Why cross product gives perpendicular vector”
    

---

## Capstone

Interactive 2D particle sandbox with adjustable dt and visible instability.

---

## Devlog

“Why my simulation explodes when dt is too large.”

---

# MONTH 2 — Software Rendering (CPU)

## Core Objective

Understand the 3D graphics pipeline without GPU abstraction.

---

## Study

Continue:  
📘 3D Math Primer (projection chapters)

Read:

- Homogeneous coordinates
    
- Perspective projection derivation
    
- Clipping basics
    

---

## Concepts You Must Encounter

Search:

- Homogeneous coordinates
    
- Why divide by w
    
- Clip space
    
- NDC (Normalized Device Coordinates)
    
- View matrix derivation
    
- LookAt matrix math
    
- Perspective matrix derivation
    
- Gimbal lock
    

---

## Implementation

- Window using SDL or SFML
    
- Draw pixels manually
    
- Implement line rasterization (Bresenham)
    
- 3D cube
    
- Model matrix
    
- View matrix
    
- Projection matrix
    
- Perspective divide
    
- Screen mapping
    

Optional:

- Backface culling
    
- Simple triangle fill
    

---

## What to Search

- “Deriving perspective projection matrix”
    
- “View matrix explained”
    
- “Right handed vs left handed coordinate system”
    
- “Why near plane cannot be zero”
    

---

## Capstone

Rotating 3D cube rendered fully on CPU.

---

## Devlog

“I built a 3D renderer without OpenGL.”

---

# MONTH 3 — OpenGL + GPU Pipeline

## Core Objective

Understand what OpenGL actually is and how GPU pipeline works.

---

## Study

📘 learnopengl.com  
Sections:

- Getting started
    
- Shaders
    
- Transformations
    
- Coordinate systems
    

Read:

- OpenGL is a specification
    
- Driver implementation concept
    

---

## Concepts You Must Encounter

Search:

- GPU pipeline stages
    
- Vertex shader
    
- Fragment shader
    
- Rasterization
    
- Depth buffer
    
- Z-fighting
    
- Clip space vs NDC
    
- GLSL basics
    
- Uniform vs attribute
    
- VBO / VAO
    

---

## Implementation

- Window + context
    
- First triangle
    
- Indexed drawing
    
- Multiple objects
    
- Uniform matrices
    
- Animation
    
- Depth testing
    
- Basic camera
    

---

## Capstone

Mini OpenGL sandbox with rotating 3D shapes.

---

## Devlog

“OpenGL is not a language. It’s a contract.”

---

# MONTH 4 — Numerical Methods Deep Dive

## Core Objective

Move beyond Euler. Understand stability.

---

## Study

MIT OCW Numerical Methods (selected lectures)

Read:

- RK4 derivation
    
- Explicit vs implicit methods
    
- Stability regions
    
- Conditioning
    

---

## Concepts You Must Encounter

Search:

- Local truncation error
    
- Global truncation error
    
- Stiff equations
    
- Stability region plot
    
- Symplectic integrators
    
- Energy conservation in integration
    

---

## Implementation

- RK4 integrator
    
- Compare Euler vs RK4 visually
    
- Spring-mass system
    
- Oscillator energy tracking
    

Plot:

- Error over time
    
- Energy drift
    

---

## Capstone

Stable spring simulation with selectable integrator.

---

## Devlog

“Euler vs RK4 — measured results.”

---

# MONTH 5 — Collision + Rigid Body Basics

## Study

📘 Game Physics Engine Development — Millington  
Chapters:

- Rigid body motion
    
- Collision basics
    

---

## Concepts You Must Encounter

Search:

- Impulse resolution
    
- Coefficient of restitution
    
- Conservation of momentum
    
- AABB collision
    
- SAT (Separating Axis Theorem)
    
- Continuous collision detection (concept)
    

---

## Implementation

- 2D rigid body
    
- AABB collision
    
- Impulse-based response
    
- Gravity stacking
    
- Basic angular velocity
    

---

## Capstone

Box stacking system without jitter.

---

## Devlog

“Making rigid bodies behave.”

---

# MONTH 6 — Cloth + Constraints

## Study

Constraint solving sections from:  
📘 Game Physics Engine Development

Search:

- Verlet integration
    
- Constraint projection
    
- Position Based Dynamics
    
- Gauss-Seidel solver
    
- Baumgarte stabilization
    

---

## Implementation

- Mass-spring cloth
    
- Wind
    
- Damping
    
- Constraint solver
    
- Stability tuning
    

---

## Capstone

Real-time cloth simulation.

---

## Devlog

“Why cloth simulation is harder than it looks.”

---

# MONTH 7 — Ray Tracing (CPU)

## Study

📘 Ray Tracing in One Weekend  
Then selected sections of:  
📘 Physically Based Rendering (PBRT)

---

## Concepts You Must Encounter

Search:

- Ray-sphere intersection
    
- Ray-triangle intersection
    
- BVH
    
- Bounding boxes
    
- Reflection vector math
    
- Refraction (Snell’s law)
    
- Fresnel term
    

---

## Implementation

- Basic ray tracer
    
- Reflections
    
- Shadows
    
- BVH acceleration
    

---

## Capstone

CPU ray tracer with reflections.

---

## Devlog

“I wrote my own ray tracer.”

---

# MONTH 8 — Path Tracing + Monte Carlo

## Study

📘 PBRT (selected)  
📘 Real-Time Rendering (light transport chapters)

---

## Concepts You Must Encounter

Search:

- Rendering equation
    
- Monte Carlo integration
    
- Variance
    
- Bias
    
- Importance sampling
    
- Cosine-weighted hemisphere sampling
    
- BRDF energy conservation
    

---

## Implementation

- Convert ray tracer to path tracer
    
- Global illumination
    
- Progressive rendering
    
- Compare samples visually
    

---

## Capstone

Basic global illumination renderer.

---

## Devlog

“How light actually bounces.”

---

# MONTH 9 — Systems + Performance

## Study

📘 Computer Systems: A Programmer’s Perspective  
📘 What Every Programmer Should Know About Memory

---

## Concepts You Must Encounter

Search:

- Cache line
    
- False sharing
    
- Branch prediction
    
- Data-oriented design
    
- AoS vs SoA
    
- SIMD basics
    
- Thread pools
    
- Amdahl’s Law
    

---

## Implementation

- Multithread path tracer
    
- Custom thread pool
    
- Benchmark scaling
    
- Profile bottlenecks
    
- Memory layout experiments
    

---

## Capstone

Performance report + optimized renderer.

---

## Devlog

“How I made my renderer 5x faster.”

---

# MONTH 10 — Real-Time PBR

## Study

📘 Real-Time Rendering  
learnopengl PBR section

---

## Concepts You Must Encounter

Search:

- Microfacet BRDF
    
- Cook-Torrance
    
- GGX distribution
    
- Shadow mapping
    
- HDR rendering
    
- Tone mapping
    
- Gamma correction
    

---

## Implementation

- Real-time PBR
    
- Shadow mapping
    
- HDR pipeline
    
- Tone mapping
    

---

## Capstone

Real-time PBR scene with shadows.

---

## Devlog

“Making materials look real.”

---

# MONTH 11 — Deferred + GPU Particles

## Concepts

Search:

- Deferred shading
    
- G-buffer
    
- Screen-space techniques
    
- Compute shaders
    
- GPU synchronization
    
- Memory barriers
    

---

## Implementation

- Deferred renderer
    
- GPU particle system
    
- Performance comparison
    

---

## Capstone

Deferred renderer + GPU particles.

---

## Devlog

“Forward vs Deferred — real differences.”

---

# MONTH 12 — Engine Integration

## Concepts

Search:

- Frame graph
    
- Render graph
    
- Job systems
    
- ECS basics
    
- Modular architecture
    
- Engine layering
    

---

## Implementation

- Clean architecture
    
- Job system
    
- Simulation module
    
- Rendering module
    
- Resource management
    

---

## Final Capstone

Mini engine demo:

- Cloth
    
- Rigid bodies
    
- PBR
    
- GPU particles
    
- Stable 60 FPS
    

---

# Brutal Truth

This plan will break you at least twice.

That’s normal.

You are not trying to become a tutorial follower.

You are building layered understanding.

And yes — this is realistically doable in 1 year **if you treat it like serious training**.

---

Now I’ll ask you something serious:

Are you willing to:

- ship ugly
    
- rewrite code
    
- feel stupid for months
    
- and keep going anyway?