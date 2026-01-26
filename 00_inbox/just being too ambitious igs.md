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

## Phase 0 – Mathematical Fluency & Core Tools

### 0A. Algebra, Functions & Trigonometry (Symbol Control)
- [ ] Stewart – Precalculus  (in progress)
- [ ] Schaum’s Outline of Precalculus  
- [ ] Schaum’s Outline of College Algebra  
- [ ] Gelfand – Algebra  
- [ ] Kiselev – Algebra  
- [ ] Schaum’s Outline of Trigonometry  
- [ ] Gelfand & Shen – Trigonometry  
- [ ] AoPS Precalculus (optional, ultra-cracked prep)

---

### 0B. Sets, Logic & Mathematical Thinking
- [ ] MIT – Mathematics for Computer Science  
- [ ] Hammack – Book of Proof  
- [ ] Velleman – How to Prove It  

---

### 0C. Calculus I–II (Single Variable, Structure + Computation)
- [ ] Stewart – Calculus  
- [ ] Schaum’s Outline of Calculus  
- [ ] Apostol – Calculus, Vol. I  
- [ ] Spivak – Calculus  
- [ ] Courant – Differential and Integral Calculus (selected chapters)

---

### 0D. Linear Algebra (Abstract + Numerical, in parallel)
- [ ] Gilbert Strang – Introduction to Linear Algebra  
- [ ] Axler – Linear Algebra Done Right  
- [ ] Trefethen & Bau – Numerical Linear Algebra (Applied / Reference)

---

### 0E. Probability & Statistics (Before Analysis)
- [ ] Blitzstein – Introduction to Probability  
- [ ] Grinstead & Snell – Introduction to Probability  
- [ ] Sheldon Ross – A First Course in Probability  
- [ ] Will Kurt – Bayesian Statistics the Fun Way (optional / intuition)

---

### 0F. Differential Equations & Applied Transforms
- [ ] Schaum’s Outline of Differential Equations  
- [ ] Boylestad – Differential Equations with Boundary-Value Problems  
- [ ] Arnold – Ordinary Differential Equations  
- [ ] Kreyszig – Advanced Engineering Mathematics  
  - Fourier Series & Transforms  
  - Laplace Transforms  
  - PDE exposure

---

### 0G. Optimization & Convex Thinking
- [ ] Boyd & Vandenberghe – Convex Optimization (select chapters)  
- [ ] Luenberger – Linear and Nonlinear Programming  

---

## Phase 1 – Analysis, PDE & Numerical Foundations (Advisor Alignment)

### 1A. Real & Functional Analysis
- [ ] Rudin – Principles of Mathematical Analysis  
- [ ] Kreyszig – Introductory Functional Analysis with Applications  
- [ ] Conway – A Course in Functional Analysis  

---

### 1B. Partial Differential Equations
- [ ] Strauss – Partial Differential Equations  
- [ ] Evans – Partial Differential Equations  
- [ ] Taylor – Partial Differential Equations I (selected topics)

---

### 1C. Numerical Analysis & Integral Equations
- [ ] Quarteroni, Sacco, Saleri – Numerical Mathematics  
- [ ] Atkinson – The Numerical Solution of Integral Equations of the Second Kind  
- [ ] Hackbusch – Integral Equations: Theory and Numerical Treatment  

---

### 1D. Asymptotics & High-Frequency Analysis
- [ ] Bender & Orszag – Advanced Mathematical Methods for Scientists and Engineers  
- [ ] Wong – Asymptotic Approximations of Integrals  
- [ ] Olver – Asymptotics and Special Functions  

---

### 1E. Boundary Element & Scattering Methods
- [ ] Kress – Linear Integral Equations  
- [ ] Colton & Kress – Inverse Acoustic and Electromagnetic Scattering Theory  
- [ ] Steinbach – Numerical Approximation Methods for Elliptic Boundary Value Problems  


---

**Knowledge check:**
- Algebraic manipulation (polynomials, quadratics, complex numbers)
- Trigonometric functions, identities, and equations
- Functions, relations, domains, ranges, and mappings
- Sets, logic, proofs, and discrete reasoning
- Limits, continuity, and convergence
- Rigorous calculus and series
- ODEs and qualitative behavior
- Linear systems, vector spaces, operators
- Functional analysis basics
- PDE classification and boundary problems
- Integral equations and kernels
- Numerical stability and convergence
- Probability, random variables, distributions
- Optimization & convexity
- Asymptotic reasoning and scaling laws

**Projects:**
- Matrix + vector math library (C++)
- Numerical differentiation & integration library
- Monte Carlo simulations
- Random walk / Brownian motion
- Probability distribution simulator & visualizer
- Function plotting & calculus sandbox
- Simple ODE solver (Euler / Runge–Kutta)
- Finite difference solver for elliptic/parabolic PDEs
- Boundary integral equation solver (2D Laplace / Helmholtz)
- High-frequency asymptotic experiment (stationary phase / steepest descent)


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
