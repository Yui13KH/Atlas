by nasa

---

# 🛠️ Working Drawings & Documentation for CAD/CAM

### 1. The "Blueprint" (Working Drawings)

A working drawing is a legal document in the shop. It contains the "Source of Truth" for manufacturing. If the 3D model and the 2D drawing disagree, **the 2D drawing usually wins.**

- **Title Block (Bottom Right):** 
    
    - **Scale:** Check this before measuring anything by hand.
        
    - **Units:** (Crucial!) Usually `mm`.
        
    - **Projection:** 1st or 3rd Angle symbol (Look for the "Cone").
        
    - **Material:** Tells you what Speeds/Feeds to use.
        
- **Revision Table (Top Right):** Check for the latest version. You don't want to program a Part Rev A if the shop is on Rev C.
    
- **Bill of Materials (BOM):** Lists quantities and part numbers for assemblies.
    

### 2. Standard Views (How to Visualize)

- **Orthographic:** 2D views (Front, Top, Right).
    
- **Isometric:** The 3D view. Great for seeing the "final form," but **never** pull dimensions from it.
    
- **Section Views:** A "slice" through the part.
    
    - _Hatching:_ Diagonal lines showing where the "saw" cut the metal.
        
    - _Note:_ Hidden lines are usually removed in sections to keep it clean.
        
- **Detail Views:** A "zoom-in" on tiny features (like a small thread relief).
    
- **Auxiliary Views:** Used for angled surfaces. It shows the "True Shape" of a face that isn't at 90 degrees to the machine axes.

### 3. Machine-Shop Symbols

|**Symbol**|**Meaning**|**Programmer Action**|
|---|---|---|
|**⌀**|Diameter|Use for Lathe X-coordinates.|
|**R**|Radius|Important for tool nose compensation ($G41/G42$).|
|**↧**|Depth|Defines your Z-axis travel.|
|**(X.XX)**|Reference|Just for info. **Do not** program to this; it has no tolerance.|
|**X.XX**|Not to Scale|**Warning:** The drawing is distorted. Trust the number, not your eyes.|

### 4. Dimensioning Logic

As a Programmer, how the drawing is dimensioned changes how you write your code:

- **Baseline (Ordinate) Dimensioning:** All dimensions start from a single corner (0,0).
    
    - _Benefit:_ This matches your **Work Offset (G54)** perfectly.
        
- **Chain Dimensioning:** Dimensions are linked end-to-end.
    
    - _Risk:_ **Tolerance Stack-up.** If every part of the chain is off by $0.01mm$, the final part could be off by $0.1mm$.
        
- **Dual Dimensions:** Shows `mm` and `inches` (usually in brackets `[ ]`).
    

### 5. Essential Shop Notes

Look for the "Notes" section (usually lower left). These are "Global Variables" for the part:

- **"All dimensions apply after surface treatment":** If the part gets plated (Gold/Zinc), you need to machine it slightly **smaller/larger** to allow for the coating thickness.
    
- **"Break all sharp edges":** Means you need to add a small `0.2mm` chamfer or radius in your code, even if it's not drawn.
    
- **Heat Treat Notes:** If the part is hardened, you might need to leave "grinding stock" (extra material) for a secondary process.
    

### 6. Assembly & Exploded Views

- **Assembly Drawing:** Shows how parts fit. Used to check for **Interference** (Will my tool hit the other part?).
    
- **Exploded View:** Shows the order of assembly. Useful if you are the one who has to put the parts together after machining.
    

---


reference : https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Engineering+Working+Drawing+Basics.pdf
