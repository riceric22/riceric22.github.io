---
layout: page
title: Eric Wong
subtitle: Postdoctoral researcher, MIT
---

I am a postdoctoral researcher in the [Computer Science and Artifical Intelligence Laboratory](https://www.csail.mit.edu/) of [Massachusetts Institute of Technology](https://www.mit.edu/), where I am advised by [Aleksander Madry](https://people.csail.mit.edu/madry/). Previously, I completed my PhD at the [Machine Learning Department](https://www.ml.cmu.edu/) of [Carnegie Mellon University](https://www.cmu.edu/) where I was advised by [Zico Kolter](https://zicokolter.com/). 

### Research

How can we ensure whether deep learning models are actually doing what we want them to do, in order to make them safe, robust, and reliable? My work develops principled methods to better understand and guarantee properties of deep networks, while connecting these foundational algorithms to real world problems. My research interests are roughly centered around machine learning, optimization, and robustness. 

**Provable guarantees for deep networks** Adversarial examples have established that deep networks are exceedingly brittle, and are not robust to small targeted perturbations. Empirical defenses and attacks are prone to blind spots, leading to unreliable robustness estimates. Instead, we derived scalable, provable defenses which provides a differentiable, guaranteed bound on the output of a network that can be used to train convolutional networks with robustness guarantees. 

**Beyond L-p to real-world robustness** Research in adversarial robustness typically focuses on robustness to L-p norm-bounded perturbations. However, the types of changes and perturbations that occur in real-world settings often cannot be described via an L-p ball. To bridge the gap from L-p perturbations to real-world changes, we proposed and studied new perturbation sets that capture real-world phenomena. 

**Understanding and improving robust optimization** Adversarial training is a popular robust optimization method for empirically defending against adversarial examples. However, adversarial training does not always behave the way we expect it to. We demonstrate how, unlike standard training, adversarial training is more prone to various forms of overfitting during the training process, such as robust overfitting and catastrophic overfitting.  

**Debugging deep learning** Robustness research often assumes that we know a priori what phenomena we want our models to be robust to. However, this is not always immediately obvious, especially since deep networks can often rely on unexpected spurious correlations. We have thus developed tools for creating debuggable deep networks that can more easily diagnose various failure modes such as model biases, learned correlations, and misclassifications. 

### News
+ 5/12/21: Our paper "Leveraging sparse linear layers for debuggable deep networks" was accepted for a long oral presentation at ICML 2021
+ 4/7/21: I am on the organizing committee for the ICML 2021 workshop [A Blessing in Disguise: The Prospects and Perils of Adversarial Machine Learning](https://advml-workshop.github.io/icml2021/)
+ 1/12/21: Our paper "Learning perturbation sets for robust machine learning" was accepted for a poster at ICLR 2021
+ 12/14/20: I am a main organizer for the ICLR 2021 workshop [Robust and Reliable Machine learning in the Real World](https://sites.google.com/connect.hku.hk/robustml-2021/home) 
+ 8/1/20: I have started my postdoc at MIT with Aleksander Madry