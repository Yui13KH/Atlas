
so I made a github repo specifically for this graphics programming thing cause I think I am going to take it seriously cause I really like this subject and its very hands on visual and practical while cybersecurity was cool the actual applications of it is hard to demonstrate sure you could like download vulnerable images and like then document how u found a vulnerability and how u exploited it and ur notes and all that stuff but its weird and mostly in the terminal I am not saying its not fun I still find it interesting and I wont fully give up on it but I am focusing on this now 

[GraphicsProgramming GitHub Repo](https://github.com/Yui13KH/graphics-programming-journey)

the hope is that my order would be very small steps of learning and adjusting stuff like insanely small improvements and I'll be documenting every step and every math and physics I learn along the way it might be boring and probably a lot of yapping but its kind of a personal note to begin with anyway 

---

## setting up the repo

So I first changed the folder order and setup of the repo in the hope of making it more modular.

Now we have an **external/** folder for, well, "stuff I got externally." It’s not mine, though you won't see it in the GitHub repo because it's in the `.gitignore`—the idea being it's big, so you can just download it and put it in yourself.

**core** is for later use. When I’m learning the math involved in graphics programming, I'll be making my own functions there and importing them.

**examples** are the fun little projects I'll be making.

As for the `CMakeLists.txt` files, they're all connected to each other so that VS Code can generate the `.exe` and link everything together. For example:

1. The one in the **root** kind of just follows the other files to do its stuff under a certain version of **C++20**.
    
2. The `CMakeLists.txt` in **external**: You create an `INTERFACE` library (basically a virtual library), tell it where the `sdl3.lib` is, and tell every `.exe` to link this `.lib` file.
    
3. In the **example** folder: You give the name of the `.exe` and point to which `.cpp` file it's taking the code from. You "target" that file and use the virtual libraries we made to avoid pointless re-typing.
    

I'm using **VS Code + Ninja** so that it can use its `compile_commands.json`. That way, the editor can actually "see" the SDL functions, so I can use them in **IntelliSense** for an easier and more efficient environment.

