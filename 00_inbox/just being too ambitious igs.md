# Full Roadmap (Personal Checklist)

Long-term plan.  
Ambitious on purpose.  
Reading without building is pointless — every phase has projects.

Most books are from Coding Jesus’ Amazon list.  
The list isn’t special. Finishing it is.

---

temp  
- [ ] The C Programming Language (ANSI) — for École 42

---

## Phase 0 – Math Foundations

### Precalculus & Algebra (UNI / BITS Math Qualifier)
- [ ] Stewart – Precalculus  
- [ ] Schaum’s Outline of Precalculus
- [ ] AoPS Precalculus (optional, ultra-cracked prep)
- [ ] Schaum’s Outline of College Algebra  
- [ ] Gelfand – Algebra  
- [ ] Schaum’s Outline of Trigonometry  

### Sets, Logic & Discrete Reasoning
- [ ] MIT – Mathematics for Computer Science  
- [ ] Velleman – How to Prove It  

### Calculus (Core)
- [ ] Stewart – Calculus  
- [ ] Schaum’s Outline of Calculus  

### Differential Equations (UNI / BITS Math Qualifier)
- [ ] Schaum’s Outline of Differential Equations  

### Linear Algebra
- [ ] Gilbert Strang – Introduction to Linear Algebra  
- [ ] Trefethen & Bau – Numerical Linear Algebra (Applied / Reference)

### Probability & Statistics
- [ ] Blitzstein – Introduction to Probability  
- [ ] Will Kurt – Bayesian Statistics the Fun Way (intro prep for quant)

### Optimization / Applied Math
- [ ] Boyd & Vandenberghe – Convex Optimization (select chapters)  
- [ ] Kreyszig – Advanced Engineering Mathematics (PDE / Fourier / Laplace chapters)

**Knowledge check:**
- Algebraic manipulation (polynomials, quadratics, complex numbers)
- Trigonometric functions, identities, and equations
- Functions, relations, domains, ranges, and mappings
- Sets, logic, proofs, and discrete reasoning
- Limits and continuity
- Calculus (derivatives, integrals, series)
- Applications of derivatives (monotonicity, extrema)
- Differential equations (first order, later extend to second-order/system)
- Linear systems, vector spaces, eigenvalues
- Probability, random variables, distributions
- Basics of optimization & convexity

**Projects:**
- Matrix + vector math library (C++)
- Numerical differentiation & integration library
- Monte Carlo simulations
- Random walk / Brownian motion
- Probability distribution simulator & visualizer
- Function plotting & calculus sandbox
- Simple ODE solver (Euler / Runge–Kutta)

---

## Phase 1 – Core C++

No skipping.

- [ ] learncpp.com (full)
- [ ] Scott Meyers – Effective Modern C++
- [ ] Andreas Fertig – Programming with C++20  
- [ ] Jason Turner – C++ Best Practices (optional add-on)

**Knowledge check:**
- RAII
- Value vs reference semantics
- Move semantics
- UB avoidance

**Projects:**
- Custom vector / string
- RAII resource wrappers
- Small reusable libraries
- Math + geometry types
- Template-metaprogramming playground (light)

---

## Phase 2 – Systems & Performance

- [ ] Jon Stokes – Inside the Machine  
- [ ] Remzi Arpaci-Dusseau – OSTEP  
- [ ] Fedor Pikus – The Art of Writing Efficient Programs  
- [ ] Computer Systems: A Programmer’s Perspective  
- [ ] Agner Fog – Optimizing Software in C++  
- [ ] Agner Fog – Instruction Tables  
- [ ] Ulrich Drepper – What Every Programmer Should Know About Memory  
- [ ] Brendan Gregg – Systems Performance (book)  

**Knowledge check:**
- CPU pipelines, caches
- Virtual memory
- Syscalls
- Profiling & benchmarking

**Projects:**
- Arena / pool allocator
- Cache behavior benchmarks
- File I/O performance tests
- SIMD microbenchmarks

---

## Phase 3 – Advanced C++ (Design + Concurrency)

- [ ] David Vandevoorde – C++ Templates: The Complete Guide  
- [ ] Klaus Iglberger – C++ Software Design  
- [ ] Anthony Williams – C++ Concurrency in Action  
- [ ] Stanley Lippman – Inside the C++ Object Model

**Knowledge check:**
- Template metaprogramming
- API design
- Threading models
- Memory ordering

**Projects:**
- Thread pool
- Lock-free queue
- Compile-time utilities
- Parallel simulation engine

---

## Phase 4 – Networking & Distributed Systems

Backend + quant infra.

- [ ] Kevin Fall – TCP/IP Illustrated, Vol 1  
- [ ] Martin Kleppmann – Designing Data-Intensive Applications  
- [ ] Linux Perf Book – Brendan Gregg  
- [ ] Beej’s Guide to Network Programming (C reference)
- [ ] Martin Thompson – Mechanical Sympathy (low-latency systems, optional)

**Knowledge check:**
- TCP/UDP behavior
- Latency vs throughput
- Replication models
- Consistency tradeoffs

**Projects:**
- TCP server (C++)
- Event-driven HTTP server
- Persistent key-value store
- Low-latency messaging system

---

## Phase 5 – Python (Data + Glue)

- [ ] Luciano Ramalho – Fluent Python  
- [ ] Wes McKinney – Python for Data Analysis  

**Knowledge check:**
- Python internals
- NumPy / pandas
- C++ bindings

**Projects:**
- Backtesting framework
- Python UI + C++ core engine
- Data ingestion pipeline

---

## Phase 6 – Quant Finance (Main Focus)

- [ ] Paul Wilmott – Quantitative Finance FAQ  
- [ ] Sheldon Natenberg – Option Volatility and Pricing  
- [ ] Nassim Taleb – Dynamic Hedging  
- [ ] Steven Shreve – Stochastic Calculus for Finance  
- [ ] Glasserman – Monte Carlo Methods in Financial Engineering (MC techniques / performance)

**Knowledge check:**
- Option pricing models
- Greeks
- Arbitrage concepts
- Stochastic processes
- Monte Carlo convergence & variance reduction

**Projects:**
- Monte Carlo option pricer (C++)
- Black–Scholes implementation
- Volatility surface visualization
- Market simulator

---

## Phase 7 – Graphics, Physics & Simulation (Hobby / Serious)

- [ ] Numerical Methods reference (ODE / PDE focused)  
- [ ] Physics simulation reference  
- [ ] Rendering fundamentals reference  
- [ ] Real-Time Rendering – Akenine-Möller et al.  
- [ ] Physically Based Rendering – Pharr, Jakob, Humphreys  
- [ ] Fundamentals of Computer Graphics – Peter Shirley  
- [ ] OpenGL Programming Guide (Red Book)  
- [ ] Vulkan Programming Guide (optional for advanced)  
- [ ] Eric Lengyel – Mathematics for 3D Game Programming and Computer Graphics  

**Knowledge check:**
- Numerical stability
- Physical simulation loops
- Rendering pipelines
- 3D math & transforms
- Light transport / shading

**Projects:**
- Particle system
- Physics simulation (rigid or soft bodies)
- CPU ray tracer
- Quant model visualizers

---

## Phase 8 – Cyber / Security Fundamentals (Hobby / Serious)

- [ ] OS security fundamentals reference  
- [ ] Memory exploitation reference  
- [ ] Network security reference  
- [ ] Ross Anderson – Security Engineering  
- [ ] Hacking: The Art of Exploitation – Jon Erickson  
- [ ] Practical Binary Analysis – Dennis Andriesse  
- [ ] The Web Application Hacker’s Handbook  
- [ ] CompTIA Security+ Study Guide  
- [ ] Penetration Testing: A Hands-On Introduction to Hacking – Georgia Weidman  

**Knowledge check:**
- Memory safety issues
- Exploitation basics
- Defensive mitigations
- Secure coding / OS hardening
- Network defense & attack mindset

**Projects:**
- Fuzzing tools
- Exploit labs
- Secure server hardening

---

## Phase 9 – Interviews & Polish (Later / Parallel)

- [ ] Adnan Aziz – Elements of Programming Interviews  
- [ ] Erich Gamma – Design Patterns  
- [ ] Sandor Dargo – Daily C++ Interview  

**Projects:**
- Algorithm drill implementations
- System design writeups
- Rewriting old projects cleanly

---

Multi-year plan.  
That’s fine.
