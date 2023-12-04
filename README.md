# PermeabilityCircularVugs
Data Analyses of numerical simulations of flow in vugular porous media

Context
These notebooks were implemented as required for the Data Science & Analytics graduate program at Computer Science Department at PUC-Rio.

Database
This folder contains data of reservoir engineering. This project consists of parameters and solutions from numerical simulations of fluid flow in two-dimensional layers of two rock samples. The sample under exploration is carbonate rock, which presents pores at different scales what makes flow modelling a challenge task.

Problem


The simulator was implemented by Dali, Gomes and Carvalho at the Laboratory of Microhydrodynamics and Flow in Porous Media at PUC-Rio, with the objectives of finding an approximate solution for pressure and velocity throughout a domain with voids and porous matrix and calculating its absolute permeability. This base is made up of tomographic images of 2 carbonate samples with cavities, which do not have a theoretical solution for the flow. Based on these images, others were virtually manipulated to obtain larger macroporosities. Some attributes were extracted from the images. The dataset presents these attributes obtained from the image, study construction parameters and the absolute permeability found by the simulation. For more details about the study that generated this dataset, the article is available at:https://www.researchgate.net/publication/337746813_Equivalent_permeability_in_vuggy_porous_media_using_Brinkman%27s_model


The following variables were extract from the different datasets:
Image_file, Id1, Id2, Slice - Filename and image identifiers
Sample - Core sample tag (5 or 8)
Threshold - Técnica de manipulação da imagem utilizada, onde 1 representa a imagem binarizada sem manipulações das cavidades.
%Area - Macroporosidade que representa o percentual que as cavidades ocupam no domínio (%)
K(m2),Keq(m2) - Permeabilidade da matriz porosa e permeabilidade equivalente (m²)
Delta P(Pa) - Diferencial de pressão imposto na simulação (Pa)
Count - Quantidade de cavidades
Total Area - Area das cavidade em pixels
Average Size - Média da cavidade
Perimeter - Perimetro médio das cavidades
Knorm - Permeabilidade equivalente dividido pela permeabilidade da matriz porosa. Representa o incremento de permabilidade devido a presença das cavidades.
Direction - Direção na imagem em que o escoamento foi simulado.
