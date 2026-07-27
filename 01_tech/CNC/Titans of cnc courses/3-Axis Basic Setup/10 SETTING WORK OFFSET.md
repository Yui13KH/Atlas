
# Edge Finding X and Y (Mechanical Edge Finder): Quick Reference Guide for New Operators

## Step-by-Step Procedure

- **1. Load Edge Finder:** Load the mechanical edge finder into the spindle and turn the spindle on to **1,200 RPM (Clockwise)** via the control's TSM window.
    
- **2. Approach the First Axis (e.g., Y-Axis):**
    
    - Using the manual handwheel, jog the spinning edge finder down beside the part.
        
    - Switch to a slow increment as you get close.
        
    - Jog inward until the wobbling edge finder tip pops/breaks concentricity and runs true/stable.
        
- **3. Locate the Edge:** Carefully jog inward in **0.001" ($0.001$) increments** until the tip breaks/offsets again. This indicates you are exactly one radius away from the edge. Lift the tool up in Z.
    
- **4. Set Work Offset (First Axis):**
    
    - Go to the control's **Set Work Offset** menu.
        
    - Highlight the axis, zero it out, and then **jog/add half the diameter of the edge finder** (typically $0.100$" for a standard $0.200$" tip) to center the spindle over the edge.
        
    - Press the set offset button again to lock in your **0** position for that axis.
        
- **5. Repeat for the Other Axis (e.g., X-Axis):** Bring the edge finder to the perpendicular edge of the part, repeat the approach and break method, lift in Z, and use the control to zero and offset by half the diameter.
    
- **6. Ready to Simulate:** With Z tool lengths touched off and X & Y zeroed, your work coordinate system (WCS) is fully established and you are ready to simulate the program.