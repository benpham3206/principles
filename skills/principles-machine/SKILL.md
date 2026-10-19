---
name: principles-machine
description: Principles of engineered physical things (mechanisms, structures, vehicles, rockets, machines, hardware products, manufacturing), organized on the six axes plus failure. Use when designing, building, reviewing, or diagnosing hardware, loads, tolerances, materials, assemblies, fatigue, or safety factors.
---

# Machine

A **machine** is matter arranged to carry loads and move energy so that a function happens, repeatedly, under conditions its maker does not fully control. The first fact about any machine is its load path: where force enters, where it goes, and what it passes through on the way.

Physics does not negotiate. State the assumptions every result depends on: local gravity $g$ (not only the Earth value), the temperature, the environment, and the material condition. Write the general form first, then put numbers in.

## Tree

```
MACHINE
├── Form          geometry, tolerances and fits, datums, stress concentrations, stiffness from geometry
├── Material      property per mass and cost, strength vs stiffness vs toughness, corrosion, temperature, anisotropy
├── Energy        loads and load cases, free-body diagram, load paths, heat, power flow, stored energy
├── Observer      operator, assembler, inspector, maintainer, sensors, the person nearby
├── Composition   part count, interfaces and fasteners, load path continuity, modularity, assembly
├── Time          fatigue, creep, wear, vibration, maintenance, manufacturing sequence, life cycle
└── Failure       factor of safety, fail safe, redundancy, test to failure, root cause
```

## Form

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Geometry | Function sets the surfaces that matter; every other surface is free to serve cost and weight | All surfaces held to the same care, so cost rises with no gain | Mark the surfaces that touch, seal, locate, or carry load. Are the rest free? |
| Tolerance | Allow the widest band that still works. Cost climbs steeply as a band narrows | Tight tolerances copied from habit; parts that do not fit because bands stack | Sum the bands along each chain, worst case and statistically. Does the stack still function? |
| Fits | A clearance fit slides, an interference fit grips, a transition fit locates. Choose by the job, then set the band | A press fit where the part must move, or a loose fit where it must locate | Compute the minimum and maximum clearance or interference. Does each end work? |
| Datums | Measure from the surfaces that locate the part in service. Three points, two points, and one point fix six degrees of freedom | Dimensions chained from arbitrary edges; a part inspected from a frame it never sees | Does the drawing reference the surfaces that mate in the assembly? |
| Stress concentration | A sharp corner, hole, notch, or thread root raises local stress to $K_t \sigma_{nom}$, where $K_t$ depends on shape only. A small circular hole in a wide plate in tension gives $K_t = 3$ | Cracks start at inside corners and holes | Find every abrupt change in section. Is there a radius, and is it large relative to the feature? |
| Stiffness from geometry | Bending stiffness is $EI$. For a rectangle of width $b$ and depth $h$, $I = b h^3 / 12$, so depth buys stiffness far faster than mass | Solid bars where a deep thin section or a tube would do; thin members loaded in compression | Compare $I$ per unit area of section. Is material placed far from the neutral axis? |
| Slenderness | A long compressed member buckles at $P_{cr} = \pi^2 E I / (K L)^2$, below its yield load. $K$ depends on end constraint | Struts sized by yield stress alone | Is the member long relative to its depth? Check $P_{cr}$ before strength |

## Material

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Property per mass and cost | Rank by the ratio the function needs: $E/\rho$ for stiffness per mass, $\sigma_y/\rho$ for strength per mass, then cost per kilogram and per part | Choosing by strength alone, or by the familiar material | Name the governing property ratio. Does the choice lead on it? |
| Strength, stiffness, toughness | Strength is the stress a material bears, stiffness is $E$, toughness is the energy absorbed before fracture. They are three properties and often trade against each other. Alloying and heat treatment move strength far more than $E$ | A stronger alloy chosen to fix a part that is too flexible | Is the part failing by yielding, deflecting, or cracking? Fix that property |
| Ductile and brittle | A ductile material yields and warns; a brittle one fractures with little warning. Some steels turn brittle below a transition temperature | A tough material at room temperature that shatters cold | Is the lowest service temperature above the transition temperature? |
| Corrosion | Corrosion needs a metal, an electrolyte, and a potential difference. Dissimilar metals in contact with moisture corrode the less noble one | Fasteners and plates of different metals in a wet joint; crevices that hold water | List the wet surfaces and every contact pair. Is each pair compatible or isolated? |
| Temperature limits | Strength and stiffness fall as temperature rises; polymers soften at far lower temperatures than metals | Room-temperature data used at the hot spot | What is the peak local temperature, and what is the property there? |
| Anisotropy | Rolled sheet, wood, fiber composites, forgings, and printed layers differ in strength by direction | Load applied across the weak direction | Draw the grain or fiber direction against the principal stress |
| Processing state | Weld, bend, cast, or heat-treat a part and its properties change locally | Handbook values applied to a welded zone | Is the property quoted for the condition the part is actually in? |

## Energy

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Load cases | List every way the machine is loaded: normal, peak, abuse, transport, assembly, fault. The worst case, not the average, sizes the part | Sizing for the working load and meeting the shipping load first | Write the load list. Which case governs each part? |
| Free-body diagram | Isolate the part, draw every force and moment on it, and require $\sum F = 0$ and $\sum M = 0$ at rest | Forces guessed, a reaction left out, a part in "equilibrium" that does not balance | Does every arrow have a source? Do the sums close? |
| Load path | Force travels through contact, material, and joints to a reaction. Follow it end to end | A load path with a gap, a bend, or a part not built to carry it | Trace the force from the point it enters to the ground. What does it pass through? |
| Heat | All lost power becomes heat. The steady rise is $\Delta T = P R_{th}$, with thermal resistance $R_{th}$. Free expansion is $\Delta L = \alpha L \Delta T$; fully restrained, a bar carries stress $E \alpha \Delta T$ | Heat with no path out; constrained parts that crush or crack on warming; mismatched $\alpha$ at a joint | Where does the heat go? What expands, and what holds it? |
| Power flow and efficiency | Efficiency is output power over input power. Efficiencies in series multiply, so a chain of good stages can be poor | Quoting one stage's efficiency for the whole drive | Multiply the chain. Where does each watt of loss land? |
| Stored energy | A raised mass $m g h$, a spring $\tfrac{1}{2} k x^2$, a flywheel $\tfrac{1}{2} I \omega^2$, a pressurized gas, a charged cell, and a hot body all release their energy when their restraint fails | A stored-energy source treated as inert once switched off | List each store. What holds it, and what happens in the first second after that holds fails? |
| Mass compounds | In a vehicle, mass carries mass. For a rocket in free space, $\Delta v = v_e \ln(m_0 / m_f)$; gravity and drag add losses on top | Saving mass in one part while the structure that carries it grows | What does one kilogram saved here save in the whole system? |

## Observer

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Operator | The operator's body, reach, strength, attention, and error rate bound the design | Controls reachable only in a pose the operator cannot hold; error-prone steps | Can a tired operator in a poor position use it correctly? |
| Assembler | A part should go together in one way only, with tools that fit and room to use them | Parts that fit backward; fasteners hidden behind other parts | Can it go together wrong? Can the tool reach every fastener? |
| Inspector | A requirement that cannot be measured cannot be accepted. The inspector needs access and a datum | Features inside a closed cavity; tolerances finer than the instrument | How is each critical feature checked, and with what resolution? |
| Maintainer | Parts that wear need to be reachable, identifiable, and replaceable by one person with common tools | An hours-long teardown for a ten-minute part | Time the swap of the part that wears first |
| Sensors | A sensor reports only what it measures, at its place, with its lag and noise. Control and safety depend on the measure | A reading taken as the state of the whole machine; a sensor placed where the failure is not | What does the sensor not see? Where would the fault have to be to hide? |
| The person nearby | Plan for the person closest when it fails: guards, shields, and clear paths away from the stored energy | Safety left to a warning label | If the worst part fails now, where does the energy go, and who is there? |

## Composition

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Part count | The best part is no part. Every part adds a tolerance, an interface, a failure, a cost, and a step | Parts added to fix problems that a simpler shape would remove | For each part: could another part do its job? |
| Interfaces | Each interface states what crosses it: force, motion, heat, signal, fluid. Define it once, completely | Interfaces left to the assembler's judgment | Does each interface name its loads, its tolerances, and its fastening? |
| Fasteners | A tightened bolt clamps with preload. If the preload exceeds the external load that would separate the joint, the bolt sees only a small fraction of the cyclic load | Loose or unspecified preload; joints that slip, rattle, or fatigue | Is the preload specified and achievable, and does it exceed the separating load? |
| Constraint | A rigid body has six degrees of freedom; constrain each exactly once. Constraining one twice (over-constraint) builds stress in at assembly | A part held at four points where three would locate it | Count the constraints on each part. Is any degree of freedom held twice? |
| Load path continuity | The load path should not jump between parts without a stiff, direct connection | Loads routed through thin walls or across fasteners in the wrong direction | Does each transfer happen through a surface built for it? |
| Modularity | Split where the interfaces are few and clean, and where parts are replaced or upgraded on different schedules | Modules that share loads or heat paths, so none can change alone | Can each module be swapped without touching the others? |
| Design for manufacture and assembly | Choose shapes the process can make cheaply: casting needs draft, machining needs tool access, sheet needs bend radii | A shape that needs a special process because no one asked the process | Ask the maker. Does each feature suit the chosen process? |

## Time

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Fatigue | Cyclic stress cracks a part at stress well below static strength. Life depends on stress range, mean stress, surface, and stress concentrations. Steels show an endurance limit under constant amplitude; aluminum alloys do not | Parts sized for the peak load once, then loaded a million times | What is the stress range per cycle and the number of cycles in the life? Use the stress with $K_t$ applied |
| Cumulative damage | Variable cycles add damage. Miner's rule sums $\sum n_i/N_i$ and predicts failure near 1; it is a heuristic with scatter | One load level checked, the rest of the load spectrum ignored | Count cycles at each level. Is the sum well below 1, with margin for scatter? |
| Creep | Under steady load at high temperature a material deforms slowly. It matters above roughly 0.3 to 0.4 of the melting temperature in kelvin for metals, and at far lower temperature for polymers | A part that holds at first and sags or relaxes over months | What is the operating temperature as a fraction of the melting temperature? |
| Wear | Sliding, rolling, and impact remove material; rate rises with load and speed and falls with hard, lubricated, well-matched surfaces | Wear surfaces left unlubricated and unreplaceable | Which surfaces rub, and what is their life? |
| Vibration | A mass on a spring has natural frequency $f_n = \frac{1}{2\pi}\sqrt{k/m}$. A force near $f_n$ raises amplitude, limited only by damping | A machine whose running speed sits on a natural frequency | List the exciting frequencies and the natural frequencies. Is each pair well apart? |
| Maintenance interval | Set inspection and replacement by the failure's growth rate, not by calendar habit | Inspection too late to catch a crack before it runs; replacement of sound parts | How fast does the fault grow, and does the interval catch it with margin? |
| Manufacturing sequence | The order of operations decides what is reachable, what warps, and what is tested | Stress from welding or machining that distorts a finished surface | Walk the part through each step. What does each step do to the last? |
| Life cycle | A machine is made, run, repaired, and retired. Design for each stage, including disassembly and what is done with the material | Parts that cannot be separated or recycled | What happens to each material at end of life? |

## Failure

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Factor of safety | The factor of safety is capacity over demand, against one named mode: $n = \text{capacity}/\text{demand}$. A number with no mode named means nothing | One factor quoted for yielding, buckling, fatigue, and fracture alike | For each part, name the mode and compute $n$ for it |
| Margin sources | The factor covers load uncertainty, material scatter, model error, and consequence. Set it by those, not by custom | A large factor over a poor model, or a small factor where the load is unknown | Which uncertainties does the factor cover, and are they measured? |
| Fail safe | Choose the failure that does the least harm: a brake that sets on loss of power, a valve that closes, a part that yields before it fractures | Failure in the dangerous direction | When each part fails, in what state does the machine stop? |
| Redundancy | Where one failure kills, add a second independent path. Common-cause failures defeat shared paths | Two paths with the same flaw or the same shared cause; a single point left in a critical load path | Name every single point. Are the backups independent? |
| Test to failure | A test that does not break the part has not shown its margin. Load a sample until it fails and compare with the prediction | Analysis trusted that no test has tried to break | Has any sample been taken to failure, and did it fail where and when predicted? |
| Root cause | Every failure gets a physical cause: the load, the stress, the material, the process, or the use. Replacing the part leaves the cause in place | Fixing the broken part and rerunning | Can you state the mechanism and the evidence? Does the fix change the cause? For the analysis itself, see `principles-lessons` |

## Laws of the medium

- Follow the load. Force has a path from where it enters to where it ends. A part off the path adds mass and cost; a gap in the path is a failure.
- Stress, not force, breaks things. Concentrations multiply it, so shape the geometry before choosing a stronger material.
- Stiffness, strength, and toughness are different properties. Name the one that governs before you select.
- Every cycle counts. A load that is safe once can fail after enough repeats; ask how often as well as how much.
- Stored energy is the hazard. Know what holds it and where it goes when that fails.
- Each part, tolerance, and interface costs something and can fail. Remove first, then add only what the function needs.
- Test beyond the limit. A model has a range; only a test finds its edge.

## Defaults to replace

The factor of safety of 2 with no named mode, the standard tolerance on every dimension, sharp internal corners, the familiar alloy, one fastener size for every joint, thick sections for strength when depth would serve, a part added to patch a problem, a model run with no test, and a repair that swaps the part and leaves the cause.
