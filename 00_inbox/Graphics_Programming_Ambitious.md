# Graphics & Simulation Engineer Development Plan
Applied. Interleaved. Project-Driven.

Assumptions:
- ~4 hours/day focused study
- Continuous implementation
- Every theoretical concept must be translated into code

Estimated timeline: ~3–4 years of consistent work

============================================================
PHASE 1 — Mathematical & Low-Level Foundations (3–4 months)
Objective: Build core mathematical intuition and low-level programming control.

============================================================

## Study

### Mathematics (parallel with implementation)
- 3D Math Primer for Graphics and Game Development — Dunn & Parberry
- Stewart — Calculus (derivatives and integrals)
- Schaum’s Outline of Calculus (problem practice)

Core Topics:
- Vectors (2D/3D)
- Dot and cross products
- Matrices and linear transformations
- Coordinate systems
- Derivatives
- Basic numerical integration (Euler method)

---

### C Programming
- The C Programming Language — Kernighan & Ritchie

Core Topics:
- Memory management
- Pointers
- Struct layout
- Dynamic arrays
- Linked lists

---

## Implementation Milestones

- Implement a dynamic array from scratch
- Build a 2D/3D vector math library
- Implement matrix multiplication
- Manually construct rotation and transformation matrices
- Build a simple particle simulation using Euler integration
- Implement projectile motion simulation

---

## Competency Check

You should be able to:
- Implement a basic 3D transformation pipeline
- Explain numerical instability in Euler integration
- Derive projectile motion equations
- Manage memory safely without leaks

============================================================
PHASE 2 — Modern C++ & Linear Algebra Depth (4–5 months)
Objective: Write production-level C++ and understand transformation mathematics deeply.

============================================================

## Study

### Modern C++
- learncpp.com
- Effective Modern C++ — Scott Meyers
- C++ High Performance — Viktor Sehr

Core Topics:
- RAII
- Move semantics
- Smart pointers
- Memory layout
- Profiling fundamentals

---

### Linear Algebra
- Introduction to Linear Algebra — Gilbert Strang
- Essential Mathematics for Games — Van Verth

Core Topics:
- Linear transformations
- Change of basis
- Projection matrices
- Eigenvalues (intuitive and practical meaning)
- Stability intuition

---

## Implementation Milestones

- Implement a 3D camera system
- Derive and implement a projection matrix
- Build a custom vector/matrix library (add SIMD if possible)
- Implement a basic multithreaded thread pool
- Benchmark and profile the math library

---

## Competency Check

You should be able to:
- Explain eigenvalues in terms of stability and scaling
- Profile CPU bottlenecks effectively
- Demonstrate measurable performance improvements
- Understand basic cache behavior

============================================================
PHASE 3 — Systems & Numerical Methods (3–4 months)
Objective: Develop performance awareness and numerical stability expertise.

============================================================

## Study

- Computer Systems: A Programmer’s Perspective
- What Every Programmer Should Know About Memory
- MIT OCW Numerical Methods (selected)
- Numerical Recipes (selected chapters)

Core Topics:
- Memory hierarchy
- Cache lines
- Floating point precision
- Stability and conditioning
- RK4 integration
- Explicit vs implicit methods

---

## Implementation Milestones

- Implement RK4 integrator
- Compare Euler vs RK4 visually and numerically
- Implement a heat equation solver (finite differences)
- Build an explicit cloth simulation
- Measure and optimize simulation performance

---

## Competency Check

You should be able to:
- Explain numerical instability clearly
- Identify floating point error accumulation
- Demonstrate optimization with measured results
- Maintain stable simulations under controlled conditions

============================================================
PHASE 4 — Physics Simulation Core (4–6 months)
Objective: Build robust physical simulation systems.

============================================================

## Study

- Game Physics Engine Development — Ian Millington
- Real-Time Collision Detection — Christer Ericson
- Physics-Based Animation — Kenny Erleben
- Rigid Body Dynamics Algorithms — Featherstone (selected)

Core Topics:
- Rigid body dynamics
- Collision detection and response
- Spatial partitioning
- Constraint solving
- Implicit integration concepts

---

## Implementation Milestones

- Implement broad-phase collision detection (grid or AABB tree)
- Implement narrow-phase collision resolution
- Build rigid body stacking system
- Implement a basic constraint solver
- Upgrade cloth simulation to improve stability

---

## Competency Check

You should be able to:
- Achieve stable rigid body stacking
- Prevent jittering and tunneling
- Explain constraint resolution clearly
- Analyze simulation stability trade-offs

============================================================
PHASE 5 — Rendering Foundations (4–6 months)
Objective: Understand light transport and physically based rendering.

============================================================

## Study

- Fundamentals of Computer Graphics
- Real-Time Rendering
- Physically Based Rendering (PBRT)

Core Topics:
- Rendering equation
- BRDF theory
- Ray tracing fundamentals
- Acceleration structures (BVH)
- Monte Carlo integration
- Importance sampling
- Multiple Importance Sampling (MIS)

---

## Implementation Milestones

- Build a CPU ray tracer
- Implement BVH acceleration
- Extend to a path tracer
- Implement MIS
- Add physically based materials

---

## Competency Check

You should be able to:
- Explain variance vs bias
- Demonstrate convergence with increased samples
- Show measurable BVH speed improvements
- Explain BRDF energy conservation

============================================================
PHASE 6 — GPU & Real-Time Rendering (4–6 months)
Objective: Develop professional real-time graphics capability.

============================================================

## Study

- learnopengl.com
- OpenGL Programming Guide
- Vulkan Tutorial
- GPU Programming and Architecture — Shane Cook

Core Topics:
- GPU pipeline architecture
- Shader stages
- Deferred rendering
- Compute shaders
- GPU memory and synchronization

---

## Implementation Milestones

- Build a real-time PBR renderer
- Implement shadow mapping
- Implement SSAO
- Build a deferred renderer
- Implement GPU particle system
- Develop a multithreaded Vulkan renderer

---

## Competency Check

You should be able to:
- Sustain stable 60+ FPS rendering
- Diagnose GPU bottlenecks
- Avoid synchronization stalls
- Profile GPU workloads effectively

============================================================
PHASE 7 — Advanced Real-Time Techniques (Ongoing)
Objective: Reach industry-level rendering sophistication.

============================================================

## Study

- GPU Gems (selected)
- GPU Zen
- Selected SIGGRAPH papers

Core Topics:
- Temporal anti-aliasing
- Clustered shading
- Compute-driven pipelines
- Advanced culling strategies
- Frame graph systems

---

## Implementation Milestones

- Implement TAA
- Implement clustered shading
- Develop compute-driven particle system
- Implement frame graph architecture

---

## Final Evaluation Criteria

You have built:

- A CPU path tracer
- A real-time PBR renderer
- A stable cloth simulation
- A rigid body simulation system
- A multithreaded job system
- A clean and modular engine architecture

You can clearly explain:
- Mathematical foundations behind each system
- Stability trade-offs
- Performance optimization decisions
- Memory and cache implications

============================================================

Principle:

Theory must be implemented.
Implementation must be profiled.
Profiling must be understood.