---
layout: skeleton
---
[site]: https://www.cis.upenn.edu/~exwong/moml/

# [3990-002: Mathematics of Machine Learning (Fall 2023)][site]

Machine learning is the study of algorithms (i.e. gradient descent) that learn functions (i.e. deep networks) from experience (i.e. data). 
Behind this simple statement, is a lot of mathematical scaffolding: statistics for handling data, optimization for understanding learning algorithms, and linear algebra to create expressive models. 

However, the typical computer science degree typical requires only a basic understanding of these mathematical concepts. This means that taking an advanced machine learning course may require taking multiple courses across graduate statistics and mathematics just to get up to speed. It will also get you used to the mathematical lingo of machine learning. If you've ever tried reading an ML paper and found it difficult to follow the concepts and equations, this might be the course for you. 

To better prepare undergraduates for machine learning coursework and research, this course aims to provide the missing background required to be able understand mathematical concepts commonly used in machine learning. This course will be based on the [Mathematics for Machine Learning](https://mml-book.github.io/) textbook, which covers the mathematical foundations of machine learning as well as examples of how machine learning algorithms that use these foundations. 

**Instructor**: [Eric Wong](https://www.cis.upenn.edu/~exwong) ([exwong@cis](mailto:exwong@cis.upenn.edu))

**Class**: Monday and Wednesday, 3:30PM-4:59PM

**Website**: [https://www.cis.upenn.edu/~exwong/moml/][site]

**Registration**: To register, you need to sign up both on [courses.upenn.edu](https://courses.upenn.edu/) and also submit the questionaire on the [CIS waitlist](https://advising.cis.upenn.edu/waitlist/) before I can add you to the course. 

**Prerequisites**: We will assume you've taken the [minimum mathematics requirements of the Penn CS degree](https://catalog.upenn.edu/undergraduate/programs/computer-science-bse/). That is: 
+ CIS1600 (CS foundations)
+ CIS2610 or equivalent (discrete probability)
+ MATH1400/MATH1410 or equivalent (vector calculus)
+ MATH2400 or equivalent (linear algebra)

If you haven't yet taken the course CS prerequisites, you may be able to get by going over the review topics in chapters 2, 5, and 6 of the course textbook. 

**Structure**: We will build upon these foundations and cover a more in depth study suited for machine learning problems. Each focus area will be structured in three parts as (1) review of prior material, (2) new ML fundamentals, and (3) an ML example. The review will quickly go over concepts that were already covered in a previous course. The ML fundamentals will introduce the advanced concepts for machine learning. The example will show you how these fundamentals are used in practice. These focus areas are: 

1. **Probability & statistics.** Review: probability spaces and discrete probability. Fundamentals: continuous probability. Example: generalization bounds. 
2. **Linear & functional analysis.** Review: linear algebra. Fundamentals: function spaces. Example: representer theorems. 
3. **Calculus & optimization.** Review: Multivariate calculus. Fundamentals: optimization. Example: convergence rates. 

We will accompany these topics with several examples demonstrating how these core techniques are used to prove fundamental results about machine learning algorithms. 

**Grading**: There will be approximately 10 homeworks (estimated weekly) totaling 50% of your grade. There will also be 3 midterms at 15% each, one per focus area. 5% for participation. 

A template for your homework solutions can be found [here](https://www.overleaf.com/read/jpxqtspbpqdk). Homeworks are due a week after they are assigned. 

### Schedule

Tentative schedule. 

| Date | Topic | Notes |
|---|---|---|
| August 30 | Overview | (1.1, [extra notes](https://www.cis.upenn.edu/~exwong/assets/moml/overview.pdf)) |
| September 4 | Labor day (no class) ||
| *Probability & statistics* || [(probability lecture notes)](https://www.cis.upenn.edu/~exwong/assets/moml/probability.pdf) |
| September 6 | Review | Discrete + Continuous Probability <br>Reading: Chapters 6.1, 6.2 <br>Homework: Problems 6.1, 6.4, 6.11 (due September 13)|
| September 11 | Review |  Discrete + Continuous Probability <br>Reading: Chapters 6.3, 6.4 |
| September 13 | Fundamentals | Mean and Variance, Gaussian distribution <br>Reading: Chapters 6.4, 6.5 <br>Homework: Problems 6.5, 6.7, 6.9 (due September 20)|
| September 18 | Fundamentals | Exponential Distributions and Conjugacy <br>Reading: 6.6 |
| September 20 | Fundamentals | Concentration inequalities (Markov, Chebyshev, WLLN) <br>Homework: Problems [6.3, 6.12, Chernoff](https://www.cis.upenn.edu/~exwong/assets/moml/HW3.pdf) (due September 27) |
| September 25 | Example | Generalization bounds |
| September 27 | Example | Generalization bounds |
| October 2 | Midterm 1 || 
| *Linear & functional analysis* |||
| October 4 | Review | Linear algebra  (2.2,2.4)|
| October 9 | Review | Linear algebra (2.5,2.6)|
| October 11 | Fundamentals | Decompositions (4.3,4.4,4.5)|
| October 16 | Fundamentals | Inner product spaces (2.4) |
| October 18 | Fundamentals | Functional analysis|
| October 23 | Fundamentals | Hilbert spaces |
| October 25 | Example | Representer theorems |
| October 30 | Example | Representer theorems |
| November 1 | Midterm 2 ||
| *Calculus & optimization* |||
| November 6 | Review | Multivariate calculus (5.1)|
| November 8 | Review | Multivariate calculus (5.2)|
| November 13 | Fundamentals | Vector calculus (5.3)|
| November 15 | Fundamentals | Matrix calculus (5.4)|
| November 20 | Fundamentals | Multivariate Taylor Expansion (5.7,5.8) |
| November 22 | Friday class schedule (no class) ||
| November 27 | Fundamentals | Gradient Descent (7.1)|
| November 29 | Example | Convergence analysis |
| December 4 | Example | Convergence analysis |
| December 6 | Midterm 3 ||
| December 11 | No class ||
| December 21 | Term ends ||
