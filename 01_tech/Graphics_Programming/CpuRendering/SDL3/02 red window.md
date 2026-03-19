
## CPU Rasterizer 0.1

So, Step 01 was just popping a window. **Step 02** is "Software Rendering," which basically means everything is on the cpu

## The "How it Works" Part

Instead of using a "Renderer" (which is basically a high-level driver), I’m grabbing the **Surface**.

The `SDL_Surface` is just a giant C-style `struct` that lives in my RAM. Inside that struct is a pointer called `pixels`. This is literally just the address of a massive, long array of numbers in the ram's memory. Each number represents one pixel on the screen.

Because I want my pixels to be exactly 32 bits (4 bytes: Alpha, Red, Green, Blue), I cast that pointer to `uint32_t*`. This tells the compiler: "Treat this block of memory as a list of 32-bit integers."

## The Loop & The Math

I’m running a nested `for` loop (Y then X). This is the CPU acting like a scanner.

- **The Problem:** The screen is 2D (a grid), but the RAM is 1D (a long line).
    
- **The Solution:** I use the math `(y * width) + x` to figure out which "slot" in the long line of RAM belongs to the specific pixel I want to color.
    
- **The Paint:** I’m using **Bit Shifting** (`<<`) and **Bitwise OR** (`|`) to pack four 8-bit colors into that one 32-bit slot.
    

Once the loop finishes, I call `SDL_UpdateWindowSurface`. This is the CPU physically copying that giant chunk of RAM over to the window's display memory so I can actually see my dark red background.

---

## 🧠 Why the Math `(y * width) + x`?

Think of a **Sheet of Graph Paper** that is 3 squares wide and 2 squares high.

If you laid every square out in a single straight line, it would look like this:

`[0][1][2] | [3][4][5]`

(The first row, then the second row).

If you want to find the square at **Row 1 (y=1)**, **Column 1 (x=1)**:

1. You have to skip the **entire first row** (Width = 3).
    
2. Then you move over by **x**.
    

$$Index = (1 \times 3) + 1 = 4$$

---

| **Name**          | **Type** | **What it actually is**                                                                                                                                              |
| ----------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `uint32_t`        | Type     | An unsigned integer that is **guaranteed** to be 32 bits. Crucial so the pixel "fits" perfectly in memory.                                                           |
| `screen->pixels`  | `void*`  | A raw memory address. The "address" of the first pixel at the top-left (0,0).                                                                                        |
| `<<`              | Operator | **Left Shift**. Shoves bits to the left. `(r << 16)` moves the Red value to its specific "reserved" slot in the 32-bit number.                                       |
| `SDL_LockSurface` | Function | Tells the OS: "Don't touch this memory while I'm writing to it." This prevents the app from crashing if the OS tries to move the window while we're painting pixels. |
|                   |          |                                                                                                                                                                      |
