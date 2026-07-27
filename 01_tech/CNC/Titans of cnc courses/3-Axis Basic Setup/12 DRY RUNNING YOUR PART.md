# Dry Running a Program: Quick Reference Guide for New Operators

## Step-by-Step Procedure

- **1. Shift Z-Axis Up:** Go to the **Offset** page, select your active work coordinate system (e.g., **G54**), navigate to the **Z column fine adjustment** tab, and enter **6 inches** to safely lift all tools well above the part.
    
- **2. Prepare Control Settings:** Switch to **Auto** mode to return to the program. Open the **Program Control** menu and ensure the following options are selected:
    
    - Dry run feed rate
        
    - Reduced rapid travel
        
    - M1 (optional program stop)
        
    - _(This setup reduces rapid travel speeds while keeping programmed feed rates manageable)._
        
- **3. Safety Precautions:**
    
    - Turn **off** the coolant.
        
    - Turn down your **rapid overrides**.
        
    - Close the enclosure door.
        
    - Keep your hand hovering over the **Feed Hold** button (which pauses machine movement without stopping the spindle) and know the location of the **E-Stop** button just in case of an emergency.
        
- **4. Execute Dry Run:** Press **Cycle Start** while closely watching the tool paths move 6 inches above the part to verify everything behaves as expected.
    
- **5. Final Verification:** Once all tools have successfully completed the dry run without issues, perform a final setup check, remove the 6-inch Z offset, turn your coolant back on, and you are ready to run the program in the material.