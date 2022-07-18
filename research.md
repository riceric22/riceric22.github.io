---
layout: page
title: Research
---

How can we make sure that deep learning models are actually doing what we want them to do? I study  the foundations of robust and reliable machine learning: how to understand, debug, and guarantee the behavior of machine learning models. My research interests span machine learning, optimization, and robustness, in order to develop principled methods with an eye towards scalability and practicality in real-world settings. 

**Provable guarantees for deep networks** Adversarial examples have established that deep networks are exceedingly brittle, and are not robust to small targeted perturbations. Empirical defenses and attacks are prone to blind spots, leading to unreliable robustness estimates. Instead, we derived scalable, provable defenses which provides a differentiable, guaranteed bound on the output of a network that can be used to train convolutional networks with robustness guarantees. 

**Beyond L-p: characterizing robustness in the real world** Research in adversarial robustness typically focuses on robustness to L-p norm-bounded perturbations. However, the types of changes and perturbations that occur in real-world settings often cannot be described via an L-p ball. To bridge the gap from L-p perturbations to real-world changes, we proposed and studied new perturbation sets that capture real-world phenomena. 

**Understanding and improving robust optimization** Adversarial training is a popular robust optimization method for empirically defending against adversarial examples. However, adversarial training does not always behave the way we expect it to. We demonstrate how, unlike standard training, adversarial training is more prone to various forms of overfitting during the training process, such as robust overfitting and catastrophic overfitting. Understanding these issues allowed us to greatly accelerate and improve the performance of adversarial training approaches. 

**Debugging deep learning** Robustness research often assumes that we know a priori what phenomena we want our models to be robust to. However, this is not always immediately obvious, especially since deep networks can often rely on unexpected spurious correlations. We have thus developed tools for creating debuggable deep networks that can more easily diagnose various failure modes such as model biases, learned correlations, and misclassifications. 