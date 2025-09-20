 
# DSA Assignments Repository

This repository contains solutions and documentation for **COL106 (Data Structures & Algorithms)** assignments.  
Each assignment focuses on applying fundamental DSA concepts to different real-world inspired scenarios.  

---

## 📌 Assignment 1 – Pac-Man Navigation System (Stacks)

**Background:**  
Pac-Man is trapped in a haunted maze filled with ghosts. He must find his way to the destination while avoiding them.  

**Modeling:**  
- Maze represented as a **2D grid**:
  - `0` → vacant cell  
  - `1` → ghost  
- Pac-Man can only move to cells with `0`.  
- Movement and backtracking handled using **Stacks**.  

**Objective:**  
Design a navigation system that helps Pac-Man reach his target safely by pushing valid moves onto a stack and popping them when backtracking is required.

---

## 📌 Assignment 2 – Galactic Cargo Management System (GCMS)

**Background:**  
Interstellar shipping companies need efficient cargo management for space bins with limited capacities.  
Each cargo has a **size** and a **color** that determines the allocation strategy.  

**Cargo Handling Rules:**  
1. **Blue Cargo** – Compact Fit, least ID bin chosen.  
2. **Yellow Cargo** – Compact Fit, greatest ID bin chosen.  
3. **Red Cargo** – Largest Fit, least ID bin chosen.  
4. **Green Cargo** – Largest Fit, greatest ID bin chosen.  

**Objective:**  
Implement algorithms to assign cargo items to bins efficiently based on capacity and cargo color rules.

---

## 📌 Assignment 3 – Treasure Quest: The Straw Hat Crew (Scheduling)

**Background:**  
The Straw Hat Pirates must manage and process treasures collected during their journey. Each crewmate can handle only one treasure at a time.  

**Modeling:**  
- `m`: Number of crewmates.  
- Each treasure `j` has:  
  - `id_j`: Unique ID  
  - `size_j`: Processing time (units)  
  - `arrival_j`: Arrival time  

**Objective:**  
- Implement a scheduling system for processing treasures.  
- Ensure fair load distribution and avoid idle or forgotten treasures.  

---

## 📌 Assignment 4 – Library Digitalization (Dictionary Compression & Keyword Search)

**Background:**  
IITD library is digitizing books and needs efficient ways to store and search text.  

**Task:**  
- Generate a compressed dictionary of **distinct words** for each book.  
- Enable **keyword search** to find relevant books.  

**Approaches Used:**  
1. **Musk (2nd Year)** – Uses **MergeSort** to sort and extract unique words.  
2. **Jobs, Gates, Bezos (4th Year)** – Use **Hashing** with different collision handling strategies.  

**Objective:**  
Compare sorting vs hashing for efficiency in extracting distinct words and enabling keyword search.

---

## 🚀 Tech & Concepts Covered
- Stacks for pathfinding (Backtracking).  
- Bin packing algorithms (Compact Fit & Largest Fit variations).  
- Scheduling algorithms for multiple processors.  
- Sorting & Hashing for dictionary compression.  

---

## 📂 Repository Structure
