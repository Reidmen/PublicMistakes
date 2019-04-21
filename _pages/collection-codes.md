---
title: "Collection of Codes"
layout: archive
permalink: /collection-codes/
author_profile: true
---

> Source Code is freely available to use the GNU Public License.

# Python Implementations
This collection contains all implementation within the Engineering Degree project.
They are organized regarding the type (Elastic and Viscous cells problems, Elastodynamic models, Mesh Generation).
## Cell Problems
They are described by ipynb files each case.
* 2-Dimensional Models
  
  * Modelling the cell problem using square type microstructure, with circular inclusion defining the porosity. [Code](https://reidmen.github.io/PublicMistakes/assets/implementations/HomProblemTest2D.ipynb)
  
  * Modelling the cell problem using hexagonal type microstructure, with circular inclusion defining the porosity. This case defines the same microstructure as proposed by Parnell and Grimal reference studies. [Code](https://reidmen.github.io/PublicMistakes/cassets/implementations/HomProbModTest2D.ipynb)

* 3-Dimensional Model
  
  * Modelling the cell problem using a cubic type microstructure, with cylindrical inclusion defining the porosity level. This case seek the interaction between axial and non-axial mechanical behavior, just studying possible effects from non-axial component that modify the elastic behavior of bone. [Code](https://reidmen.github.io/PublicMistakes/cassets/implementations/HomProblemTest3D.ipynb)

## Viscous Problems and quality factors.
File is described by ipynb notebook. In this case, the homogenized elastic and viscous coefficients are deduced from a unitary square microstructure following the two-scale asymptotic heuristic. Such description is derived towards a separation between real and imaginary parts (associated to elastic and viscous parts) to assess and define the so-called quality factors. [Code](https://reidmen.github.io/PublicMistakes/assets/implementations/HomProb-QFactor.ipynb).

## Elastodynamic models
Files are separated regarding fully elastodynamic models without attenuation and attenuated models.
Different models are proposed, in time and frequency domains using the asymtotic homogenization scheme.
**SOON UPDATES!**

## Mesh Generation
Following the same trend as before, a schematic mesh generation is implemented on ipynb files, using `octave` kernel in combination with `iso2mesh` library.
In this case, on a ipynb it is assessed the mesh generation from bmp cortical bone images after resizing (to be able to use on personal computers). It describes a full procedure to process images from computational tomography stacks, generate the volumetric image associated to the stack and mesh it using `iso2mesh` library. [Code](https://reidmen.github.io/PublicMistakes/assets/implementations/FileMesh-Scaled.ipynb)

Moreover, file convertion to XML file for `FEniCS` usage is also implemented for tethaedral meshes
The python implementation, creates useful XML file format enconding tethraedral meshes with possibly subdomains if it is the case. It requires as input the XYZ coordinate matrix of vertices and connectivity matrix related to the XYZ points. [Code XYZ to Mesh](http://https://reidmen.github.io/PublicMistakes/assets/implementations/XYZtoXMLMesh.py). Similarly, generation of meshes with tagged subdomains is implemented. [Code XYZ to Subdomains](https://reidmen.github.io/PublicMistakes/assets/implementations/XYZtoXMLSubdomains.py)


> People think focus means saying yes to the thing you've got to focus on. But that's not what it means at all. It means saying no to the hundred other good ideas that there are. You have to pick carefully. I'm actually as proud of the things we haven't done as the things I have done. Innovation is saying no to 1,000 things.

<cite>Steve Jobs</cite> --- Apple Worldwide Developers' Conference, 1997
{: .small}