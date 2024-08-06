---
layout: skeleton
---
[site]: https://www.cis.upenn.edu/~exwong/moml/

# [CIS 3333: Mathematics of Machine Learning (Fall 2024)][site]

Machine learning is the study of algorithms (i.e. gradient descent) that learn functions (i.e. deep networks) from experience (i.e. data). 
Behind this simple statement, is a lot of mathematical scaffolding: statistics for handling data, optimization for understanding learning algorithms, and linear algebra to create expressive models. 

However, the typical computer science degree typical requires only a basic understanding of these mathematical concepts. This means that taking an advanced machine learning course may require taking multiple courses across graduate statistics and mathematics just to get up to speed. It will also get you used to the mathematical lingo of machine learning. If you've ever tried reading an ML paper and found it difficult to follow the concepts and equations, this might be the course for you. 

To better prepare undergraduates for machine learning coursework and research, this course aims to provide the missing background required to be able understand mathematical concepts commonly used in machine learning. This course will be based on the [Mathematics for Machine Learning](https://mml-book.github.io/) textbook, which covers the mathematical foundations of machine learning as well as examples of how machine learning algorithms that use these foundations. 

**Course Attributes**: 
+ This course counts as a *mathematics elective* for engineering degrees. 
+ This course counts as a standalone co-requisite/pre-requisite for CIS5200

**Instructor**: [Eric Wong](https://www.cis.upenn.edu/~exwong) ([exwong@cis](mailto:exwong@cis.upenn.edu))

**Class**: Monday and Wednesday, 12:00PM-1:29PM

**Website**: [https://www.cis.upenn.edu/~exwong/moml/][site]

**Registration**: To register, you need to sign up both on [courses.upenn.edu](https://courses.upenn.edu/) and also submit the questionaire on the [CIS waitlist](https://advising.cis.upenn.edu/waitlist/) before I can add you to the course. 

**Prerequisites**: We will assume you've taken a basic introductory course in calculus, probability, and linear algebra. For a typical degree in computer science at Penn, this is typically: 
+ STAT4300 or CIS2610 or equivalent (discrete probability)
+ MATH1400 or MATH1410 or equivalent (calculus)
+ MATH2400 or equivalent (linear algebra)

If you have 2 out of the 3 pre-requisites, you can review the missing background and take the course. The pre-requisite topics are covered in chapters 2, 5, and 6 of the course textbook. The corresponding module may be more challenging than the others, but can be done successfully. If you are missing more than one pre-requisite, you may find this course to be extra challenging.  

**Structure**: We will build upon these foundations and cover a more in depth study suited for machine learning problems. Each focus area will be structured in three parts as (1) review of prior material, (2) new ML fundamentals, and (3) an ML example. The review will quickly go over concepts that were already covered in a previous course. The ML fundamentals will introduce the advanced concepts for machine learning. The example will show you how these fundamentals are used in practice. These focus areas are: 

1. **Probability & statistics.** Review: probability spaces and discrete probability. Fundamentals: continuous probability. Example: generalization bounds. 
2. **Linear & functional analysis.** Review: linear algebra. Fundamentals: function spaces. Example: representer theorems. 
3. **Calculus & optimization.** Review: Multivariate calculus. Fundamentals: optimization. Example: convergence rates. 

These topics will be accompanied with several examples demonstrating how these core techniques are used to prove fundamental results about machine learning algorithms. In particular, we will prove several hallmark theoretical results from machine learning: genearlization bounds that explain why learning from data works, representer theorems that identify what functions models can learn, and convergence rates that control how long it takes to learn models.  

**Grading**: There will be approximately 10 homeworks (estimated weekly) totaling 50% of your grade. There will also be 3 midterms at 15% each, one per focus area. 5% for in-class participation. 

A template for your homework solutions can be found [here](https://www.overleaf.com/read/jpxqtspbpqdk). Homeworks are due a week after they are assigned. 

### Schedule

Tentative schedule. 

| Date | Topic | Notes |
|---|---|---|
| August 28 | Overview | (1.1, [extra notes](https://www.cis.upenn.edu/~exwong/assets/moml/overview.pdf)) |
| September 2 | Labor day (no class) ||
| *Probability & statistics* || [(probability lecture notes)](https://www.cis.upenn.edu/~exwong/assets/moml/probability.pdf) |
| September 4 | Review | Discrete + Continuous Probability <br>Reading: Chapters 6.1, 6.2 |
| September 9 | Review |  Discrete + Continuous Probability <br>Reading: Chapters 6.3, 6.4 |
| September 11 | Fundamentals | Mean and Variance, Gaussian distribution <br>Reading: Chapters 6.4, 6.5|
| September 16 | Fundamentals | Exponential Distributions and Conjugacy <br>Reading: 6.6 |
| September 18 | Fundamentals | Concentration inequalities (Markov, Chebyshev, WLLN) <br>[(concentration lecture notes)](https://www.cis.upenn.edu/~exwong/assets/moml/concentration.pdf)|
| September 23 | Example | Generalization bounds |
| September 24 | Example | Generalization bounds |
| September 30 | Midterm 1 || 
| *Linear & functional analysis* |||
| October 2 | Review | Linear algebra  (2.2,2.4) <br>[(linear algebra lecture notes)](https://www.cis.upenn.edu/~exwong/assets/moml/linear_algebra.pdf)||
| October 7 | Review | Linear algebra (2.5,2.6)|
| October 9 | Fundamentals | Change of Basis (2.7)|
| October 14 | Fundamentals | Inner product spaces and Orthogonality (3.1-3.8) |
| October 16 | Fundamentals | Decompositions (4.1, 4.2, 4.4)|
| October 21 | Example | Functional analysis, Hilbert spaces, Kernels (12.4)  <br>[(representer lecture notes)](https://www.cis.upenn.edu/~exwong/assets/moml/representer.pdf)|
| October 23 | Example | Representer theorems |
| October 28 | Midterm 2 ||
| October 30 | Review | Multivariate calculus (5.1-5.4) <br>[(calculus notes)](https://www.cis.upenn.edu/~exwong/assets/moml/calculus.pdf)|
| *Calculus & optimization* |||
| November 4 | Review | Multivariate calculus (5.5-5.7)|
| November 6 | Fundamentals | Multivariate Taylor Series (5.8-5.9) |
| November 11 | Fundamentals | Gradient Descent (7.1))<br>[(continuous optimization notes)](https://www.cis.upenn.edu/~exwong/assets/moml/continuous_optimization.pdf)|
| November 13 | Fundamentals | Constrained and Convex Optimization (7.2-7.3) |
| November 18 | Fundamentals | Conjugates & Taylor's Theorem <br>[(SGD convergence notes)](https://www.cis.upenn.edu/~exwong/assets/moml/sgd_convergence.pdf)|
| November 20 | Example | Convergence analysis |
| November 25 | Example | Convergence analysis |
| November 27 | Friday class schedule (no class) ||
| December 2 | Review ||
| December 4 | Midterm 3 ||
| December 9 | No class ||
| December 19 | Term ends ||


