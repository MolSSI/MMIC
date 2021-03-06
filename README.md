# What is MMIC?
The Molecular Mechanics Interoperable Components (MMIC) project provides a standard for input and output of MM programs by defining the scientific and computational stages of classical MM pipelines, but leaving the implementation up to the developer/user. MMIC attempts to define the "what" of scientific stages without restricting the "how" i.e. MMIC defines only the input and output the implementation must conform to so that end-users can swap out different implementations with minimal effort in their existing pipelines, or workflow tools of their preference. The components themselves allow users to speed up most of their pipelines by integrating the expertise from component developers, letting them focus on the parts of their research they are experts in.

This allows reproducibility from statically defined and shareable components, experimentation to find a quality series of components for specific problems and systems, and a mechanism for quality methodological assessment without the need for deep scientific expertise.

<p align="center">
    <img src="mmic/data/imgs/mm_component_hierarchy.png" width="500">
</p>

We construct an abstract Base Component that is inherited by all MMComponent blueprints. For each scientific problem, a blueprint is defined that specifies what the component seeks to achieve, along with the necessary inputs and outputs. This component is implemented to satisfy the scientific problem by any number of users/developers.

# Components being developed

## Simulators
- [Molecular Docking](https://github.com/MolSSI/mmic_docking): molecular docking engine based on [Autodock Vina](http://vina.scripps.edu)
- [Molecular Dynamics](https://github.com/MolSSI/mmic_namd): molecular dynamics engine based on the [NAMD](https://www.ks.uiuc.edu/Research/namd) simulator

## Assemblers
- [ForceField](https://github.com/MolSSI/mmic_param): parameterization of molecules from existing force fields

## Translators
### Structure/Topology converters:
- [RDKit](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/trans/rdkit_component.py): RDKit to/from MMSchema structure/topology converter
- [ParmEd](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/trans/parmed_component.py): ParmEd to/from MMSchema structure/topology converter
- [MDAnalysis](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/trans/mda_component.py): MDAnalysis to/from MMSchema structure/topology converter
### Trajectory converters
- [MDAnalysis](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/trans/mda_component.py): MDAnalysis to/from MMSchema trajectory converter
### Forcefield converters
- [Gromacs](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/trans/gro_component.py): Gromacs to/from MMSchema force field converter
