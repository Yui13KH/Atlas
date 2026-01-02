### SDLC

basically the *software development life cycle* is a plan to help developers follow a well organized way of developing software to ensure meeting deadlines and expectations without going into a mess, and it helps multiple teams coordinate on what to do and when

generally there are 6 phases, they are sequential (discrete), and the whole cycle often repeats for new features or versions

1 : planning  
first you gather all the requirements for the software – document them, analyze, and prioritize  
you should consider:  
- users and their needs  
- purpose of the software  
- inputs/outputs  
- risks  
- quality assurance (QA)  
- compliance requirements  
- resourcing (team, tools)  
- scheduling  

then you estimate time and cost for stakeholders  
sometimes a prototype is built to test key functionality or feasibility  
finally, you create a *Software Requirement Specification* (SRS) document, review it, and get stakeholder approval before moving forward

2 : design  
using the approved SRS, you plan the software architecture (high-level and low-level design)  
after reviews and discussions, you produce a *Design Document* that guides the next phase

3 : development  
this is the actual coding phase – build the software according to the design document  
companies often have specific coding standards, guidelines, and tools you must follow

4 : testing  
test the software thoroughly for bugs, UI issues, security vulnerabilities, performance problems, etc.  
any issues found are documented, reported, fixed by developers, and then re-tested (regression testing)

5 : deployment  
after passing internal testing, the software is usually deployed to a *User Acceptance Testing* (UAT) environment  
real users test it there to catch things that internal testing might miss  
once UAT is approved, it's released to production (live environment)

6 : maintenance  
after release, you handle:  
- fixing new bugs  
- addressing UI/UX issues  
- implementing requirement changes  
- optimizations and enhancements  

the cycle can restart for major updates or new features

### Software Methodologies

#### Waterfall Method
It's a sequential model where the output of one phase becomes the input for the next phase – all the planning and architecture is done upfront  
users don't see the product until it's in the testing phase  
for major version releases of the product, the same process is repeated, which results in long times between releases

#### The V-Shape Model
It's also sequential  
the phases form a V shape  
every phase on the left side (planning and design) corresponds to a matching testing and validation phase on the right side

#### Agile Method (probably the most used these days)
it's iterative, not sequential  
it focuses on short bursts of collaborative work rather than a strict top-down process  
they work in cycles (usually 2-4 weeks long, called sprints) and testing happens alongside development  
after each cycle, a demo is released to show stakeholders progress  
they have the "Agile Manifesto", which basically says prioritize users, working software, and collaboration over strict processes – things should be more dynamic and team-based

#### Pros and Cons of Each
Waterfall and V-Shape: since planning and design happen upfront, estimating budget and time is more accurate, but if requirements change later, it messes up the whole plan  
Agile: because it's iterative, new requirements and design changes can be incorporated easily, but the dynamic nature makes estimating total budget and timeline harder

## Software Testing

there are 3 main types of testing  
- functional testing  
- non-functional testing  
- regression testing  

functional testing is checking the actual functionality of the software – basically, when you give it certain inputs (x), does it reliably output the expected results (y) according to the requirements and design  

non-functional testing covers stuff like what happens under heavy stress, if the database gets corrupted, how it behaves on different OS's, screen sizes, etc.  

regression testing: it's like "if we add this new feature, does it break the old ones or do they still work together fine?"

## Testing Levels
unit → integration → system → acceptance

in summary  
unit testing: developers test individual pieces/components to make sure they produce the expected outputs reliably  

integration testing: when teams build separate functionalities that need to be combined – this tests if those pieces fit and work together well (teams follow specs to keep errors low)  

system testing: testing the entire system as a whole, including non-functional aspects  

acceptance testing: this is for customers and stakeholders – do they like it, does it meet their expectations and needs?