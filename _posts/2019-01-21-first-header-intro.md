---
title: "Objectives for the following months"
header:
  image: /assets/images/CorticalBoneS1000OPT20-View.png
  caption: "Photo: [**From Reidmen Repository**](https://github.com/Reidmen)"
tags: 
  - objectives
  - review
  - q-learning
  - cython
  - fenics
---

Featuring with a beautiful corticla bone mesh[^1] this post introduces the main objectives to develop for the following months.
Hopefully all the items will be developed, and mainly shown in a investigation-like perspective in ´´Python, Julia or C++´´ implementations. 

I expect to describe and show to all the reader, detailed journey on numerical implementations of q-learning models oriented to finance, study neural nets in various setting (the study of LSTM, Convolutional layers for example) being particularly my attention towards deep q-learning methods! and the so-called meta-learning.
On the other hand, I expect to develop a basic Flask app, deployed using ´´Docker´´ with finance-like prediction scenarios. 

In a mechanical oriented setting, I will post several study cases of ´´´FEniCS´´ usage, image processing toolbox and numerical implementation of various PDE-related problems.

## Objectives

As mentioned before, the main objectives are separated in two-classes:
One direction of study using policy-learners in the context of reinforcement-learning:
  * Study the on-policy and off-policy approaches with test case studies...
  * Implementations of Python in test cases oriented towards finance prediction tasks or time-related sets.
  * Introduction to meta-learning and possible applications on PDE-like problems!.
  * Everything else that can be found in this area!.

The other direction in related to work I've already done in the context of biomechanical models
* Study a proposed ultrasounic tool to describe bone parameters.
* Describe numerical implementation of the direct and inverse problems related.
* Mesh generation procedures with cool simulations.
* Some other works oriented in scientific computing with PDE-like formulations.

## Question hoping to be tacke...

There is a natural expectaction to neural nets to be good approximators of realistic complex models (for example in the sense of NP problems in Complexity Theory), therefore since we are in a time with vast ammount of procedures, techniques such as Finite Element Method (FEM) or similar techniques are becoming too specific. Could they become shadowed by parametrize approximators that *learn* the mode using sample data? [^2]


[^1]: Mesh Generated with state-of-art library [iso2mesh](http://iso2mesh.sourceforge.net/cgi-bin/index.cgi)
[^2]: Awesome MIT lecture of [Ilya Sutskever](https://www.youtube.com/watch?v=9EN_HoEk3KY)