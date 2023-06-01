---
layout: page
title: Research
---

How can we make sure that deep learning models are actually doing what we want them to do? I study  the foundations of robust and reliable machine learning: how to understand, debug, and guarantee the behavior of machine learning models. My research interests span machine learning, optimization, and robustness, in order to develop principled methods with an eye towards scalability and practicality in real-world settings. 

To achieve this goal, my work touches upon a variety of topics. Some examples include generative modeling, sparsity, influence functions, transformers, linear programs, overfitting, biases, and transfer learning. Below we summarize some of the main questions we've been looking at. 

# Principled Model Explanations
What does a model explanation mean? Even though explanations in machine learning purport to explain the prediction process, we still don't know what we can conclude from many common explanations for large machine learning models. We're looking into constructing principled explanations that have guaranteed, provable meaning for the end user. Some examples include: 
+ **Certified interpretability.** Explanations of model predictions in machine learning are often criticized for being misleading and brittle. We are interested in learning models with provably stable post-hoc explanations. 
+ **Explaining distribution shift.** Models need to work well when their environments change. But how exactly do environments change? We are developing tools that can pinpoint how and why distributions are changing while respecting inherent structure in the data. 

# Debugging Machine Learning
When your machine learning model behaves strangely, how do you find and fix the issue? We're developing systems that enable scalable and interactive analysis of machine learning pipelines to describe and correct these so-called "bugs". For example: 
+ **Generating rules at scale.** Machine learning models behave in surprising ways that sometimes defy basic common sense, or basic rules about the world. We are creating systems that can automatically extract common rules for machine learning systems at scale.
+ **Interactive ML debugger.** In research, we often assume a specific formulation of a problem to solve, but in practice, we often don't know what this is a priori. We are building interactive debugging tools for inspecting machine learning pipelines and identifying issues in the pipeline. 

# Prompting Science
A recent learning paradigm known as "prompting" allows users to adapt models with natural language instructions. We are working on developing tools and methods to automatically guide and support prompt design. 
+ **Adversarial Prompting.** The internet has found numerous examples of prompts elucidating strange outputs from large language models. We're developing tools that automatically search for prompts that can remain under the radar but achieve certain goals. 
+ **Chain of thought.** Asking the large language model to explain its output can improve its performance (i.e. "chain of thought"), but the explanation may have little or nothing to do with the actual output. We've studied how to make this paradigm directly faithful, or causal, to the ultimate prediction. 

# Past research
In the past, I've also worked on a variety of other topics. 

**Understanding transfer learning.** More data and bigger models in the form of pretraining typically leads to better performance when transferred to a downstream task. However, pretraining and transferring can have unexpected effects that are not always beneficial. We have studied how transfer learning can insert unintended spurious correlations to the downstrea model, and found that certain subpopulations used in pretraining can actually harm transfer performance. 

**Beyond L-p: characterizing robustness in the real world.** Research in adversarial robustness typically focuses on robustness to L-p norm-bounded perturbations. However, the types of changes and perturbations that occur in real-world settings often cannot be described via an L-p ball. To bridge the gap from L-p perturbations to real-world changes, we proposed and studied new perturbation sets that capture real-world phenomena. 

**Understanding and improving robust optimization.** Adversarial training is a popular robust optimization method for empirically defending against adversarial examples. However, adversarial training does not always behave the way we expect it to. We demonstrate how, unlike standard training, adversarial training is more prone to various forms of overfitting during the training process, such as robust overfitting and catastrophic overfitting. Understanding these issues allowed us to greatly accelerate and improve the performance of adversarial training approaches. 

**Provable guarantees for deep networks.** Adversarial examples have established that deep networks are exceedingly brittle, and are not robust to small targeted perturbations. Empirical defenses and attacks are prone to blind spots, leading to unreliable robustness estimates. Instead, we derived scalable, provable defenses which provides a differentiable, guaranteed bound on the output of a network that can be used to train convolutional networks with robustness guarantees. 