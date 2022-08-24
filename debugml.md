---
layout: skeleton
---
[site]: https://www.cis.upenn.edu/~exwong/debugml/

# [7000-005: Debugging Data & Models (Fall 2022)][site]

Do you trust your model? Despite their widespread adoption and impressive performance, modern machine learning models have a crucial flaw: it is extremely difficult to discern when and how models fail. This pitfall has given rise to a field of research known as *trustworthy machine learning*, in order to make these systems safe, responsible, and understandable. 

This course will explore the tools and methods for analyzing the machine learning pipeline and assessing their trustworthiness (or lack thereof), from the datasets, models, and predictions perspective. A [tentative schedule](#tentative-schedule-and-topics) of these topics can be found at the bottom of this page. 

**Instructor**: [Eric Wong](https://www.cis.upenn.edu/~exwong) ([exwong@cis](mailto:exwong@cis.upenn.edu))

**Class**: Tues/Thurs 1:45-3:15pm Eastern, Hayden Hall 360

**Website**: [https://www.cis.upenn.edu/~exwong/debugml/][site]

**Mask policy**: Masks are required.  

Students from all majors and degree levels are welcome. There are no specific course requirements, but a background in machine learning at an introductory course level is expected, as well as basic programming experience for the course project.  

Grading will be based off of 80% course project (15% proposal + 20% progress report + 25% final report + 20% presentation) and 20% participation (5% readings + 15% discussion). There will be no homeworks or exams. 

This class will combine lectures and discussions. The lectures will typically cover the core groundwork, followed by a student-led in-depth discussion based on assigned readings. Readings and lecture materials will be posted on the schedule. 

#### Project
As part of this course, students will inspect and debug machine learning problems for deficiencies in settings of their choice. All parts of the pipeline are fair game, including data collection, training algorithms, models and architectures, the resulting predictions, and even the debugging tools themselves. This can take the form of an audit (identifying the shortcomings of a fixed pipeline) or a patch/update (changing the pipeline to fix a problem). Example projects at various stages in the pipeline include the following: 

+ Datasets: 
    + Are there biases, spurious correlations, or underrepresented subpopulations? For example, does US census data have any blind spots or misleading correlations? 
    + Where do these problems stem from, and how does this impact downstream predictions? 
    + Can we fix the data or collection procedure to mitigate these issues? 
+ Methods and architectures: 
    + Do ML algorithms (i.e. fairness / privacy / adversarial robustness / security) for fixing models via training actually achieve their goal? 
    + Can you pinpoint or characterize the failures of modern architectures (such as large language models)? 
    + Can you construct counterexamples / subpopulations that exemplify the failure modes of these models and algorithms, or guarantee that such failure modes don't exist? 
+ Interpretability and predictions: 
	+ How faithful are explainability methods to the actual model predictions? 
	+ Are the type of explanations we can generate aligned with what practitioners need? 
	+ For example, do analysis tools for diagnosing health conditions tell doctors useful and meaningful information? 

#### Tentative schedule and topics 
The schedule and topics can change based on students' interests and as time permits. If you don't see something you'd like to learn about, send me an email. 

| Date | Topic | Notes |
|---|---|---|
| August 30 | Overview |  |
|  |  |  |
| *Failure modes* |||
| September 1 | Bias | Data generation<br>[Reading](https://arxiv.org/abs/1901.10002) |
| September 6 | Bias | Training & deployment |
| September 8 | Out of distribution | Covariate, label & concept shifts |
| September 13 | Out of distribution | Temporal, environmental & group shifts |
| September 15 | Adversarial | Adversarial attacks |
| September 20 | No class |  |
| September 22 | Adversarial | Threat models |
| September 27 | Adversarial | Data poisoning, backdoors, Byzantine faults |
| September 29 | Adversarial | Model stealing & membership inference |
|  |  |  |
| *Debugging models* |||
| October 4 | Explainability | Data visualization, summary statistics & interpretable models <br>[Reading](https://arxiv.org/abs/1811.10154) <br>*Project proposal due* |
| October 6 | Fall term break |  |
| October 11 | Explainability | Local & global interpretations |
| October 13 | Explainability | Example-based & model visualizations |
| October 18 | Verification | Complete & incomplete |
| October 20 | Verification | Specifications and properties |
| October 25 | Scientific discovery | Finding correlations |
| October 27 | Scientific discovery | [Influence functions](https://arxiv.org/abs/1703.04730) & [data models](https://arxiv.org/abs/2207.05739) |
|  |  |  |
| *ML repair* |||
| November 1 | Robust learning | Robust training & overfitting <br>*Progress report due* |
| November 3 | Robust learning | Provable defenses (bound propagation & smoothing) |
| November 8 | Robust learning | Distributional robustness ([Domain generalization](https://arxiv.org/abs/2007.01434), [Group DRO](https://arxiv.org/abs/1911.08731), [IRM](https://arxiv.org/abs/1907.02893), [JTT](https://arxiv.org/abs/2107.09044)) |
| November 10 | Data interventions | Data balancing, [source selection](https://proceedings.mlr.press/v139/hashimoto21a.html), pruning hard examples | 
| November 15 | Data interventions | Data augmentations (classical, [subgroups](https://arxiv.org/abs/2008.06775) & generative) |
| November 17 | Model adjustments | Model [edit](https://arxiv.org/abs/2110.11309)[ing](https://arxiv.org/abs/2112.01008) and [fine-tuning](https://arxiv.org/abs/2207.02842) |
| November 22 | Model adjustments | Model [patching](https://arxiv.org/abs/2008.06775) & [repair](https://arxiv.org/abs/2005.09912) |
| November 24 | Thanksgiving |  |
| November 29 | NeurIPS |  |
| December 1 | NeurIPS |  |
| December 6 | Presentations |  |
| December 8 | Presentations |  |
| December 13 | Reading period |  |
| December 15 | Final examinations | *Final report due* |
| December 22 | Term ends |  |

There is no official textbook for this course, but you may find the following references to be useful: 
+ [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/) by Christoph Molnar
+ [Trustworthy Machine Learning](http://www.trustworthymachinelearning.com/) by Kush R. Varshney
<!-- There are no specific course requirements. The course assumes a background in machine learning, such as an introductory course. , and have some basic programming experience for the course project. -->

<!-- (healthcare, autonomous driving, agriculture, logistics, energy, etc.)  -->