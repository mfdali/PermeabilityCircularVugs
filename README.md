# PermeabilityCircularVugs
Data preparation || Machinel Learning || Deep Learning

## Data Analyses of numerical simulations of flow in vugular porous media

- ## Language
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- ## Codes
  - Data preparation - [MVP_CD_Sprint1_Monique_Dali.ipynb](https://github.com/mfdali/PermeabilityCircularVugs/blob/main/MVP_CD_Sprint1_Monique_Dali.ipynb)

  - Machine Learning Pipeline to estimate flow in vugular porous media - [MVP_Sprint2_ML_Monique_Dali.ipynb](https://github.com/mfdali/PermeabilityCircularVugs/blob/main/MVP_Sprint2_ML_Monique_Dali.ipynb)

  - Deep Learning Pipeline to estimate flow in vugular porous media - [MVP_Sprint2_DeepL_Monique_Dali.ipynb](https://github.com/mfdali/PermeabilityCircularVugs/blob/main/MVP_Sprint2_DeepL_Monique_Dali.ipynb)

- ## Project Context
These notebooks were implemented as required for the Data Science & Analytics graduate program at Computer Science Department at PUC-Rio.

- ## Database
This folder contains data of reservoir engineering. This project consists of parameters and solutions from numerical simulations of fluid flow in two-dimensional layers of two rock samples. The sample under exploration is carbonate rock, which presents pores at different scales what makes flow modelling a challenge task. 

The Database folder contains thousands tomographic images, csv files with shape parameters extracted from these images, simulation parameters and results.

![image](https://github.com/mfdali/PermeabilityCircularVugs/assets/68743809/d972c167-7f3c-45a1-83bc-a97247ec3ce5)


- ## Project Overview

Fluid flow model in heterogeneous reservoir. The simulator was implemented by Dali, Gomes and Carvalho at the Laboratory of Microhydrodynamics and Flow in Porous Media at PUC-Rio, with the objectives of finding an approximate solution for pressure and velocity throughout a domain with voids and porous matrix and calculate its absolute permeability. 

The image database for the simulation is composed of tomographic images of two carbonate samples with cavities, which do not have a theoretical solution for the flow. Based on these images, others were virtually manipulated to obtain larger macroporosities. Some attributes were extracted from the images to implement a Machine Learning model. The dataset presents various attributes obtained from the image, study construction parameters and the absolute permeability estimated by the simulation. 

For more details about the study that generated this dataset, the article is available at: 


![ResearchGate](https://img.shields.io/badge/ResearchGate-00CCBB?style=for-the-badge&logo=ResearchGate&logoColor=white) https://www.researchgate.net/publication/337746813_Equivalent_permeability_in_vuggy_porous_media_using_Brinkman%27s_model

- ## Metadata

The following variables were selected from the different datasets to build the pipeline:

| Label | Description |
| -------- | -------- |
| Image_file, Id1, Id2, Slice | Filename and image identifiers |
| Sample | Core sample tag (5 or 8) |
| Threshold | Group the images that use the same technique for dividing an image into two (or more) classes of pixels, which are typically called “foreground” and “background.” The label 1 represents the binarized image without further manipulations to increase the size of the cavities in the core samples. |
| %Area | Represents the percentual of the total area that the cavities occupy. It is also called Macroporosity (%) |
| K(m2),Keq(m2) | porous matrix permeability and equivalent permeability (m²). |
| Delta P(Pa) | Pressure differential imposed in simulation (Pa) |
| Count | Cavities quantity |
| Total Area | Area of selection in square pixels |
| Average Size | cavity size average |
| Perimeter | The average length of the outside boundary of the cavities. |
| Knorm | Permeability increment due to the presence of empty spaces, the cavities. Equivalent permeability = equivalent permeability / porous matrix permeability |
| Direction | In which direction the flow was simulated. |
