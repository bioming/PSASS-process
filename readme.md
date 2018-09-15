# PoolSex

## Overview

The PoolSex pipeline is used to analyze pooled sequencing data with focus on sex. This specific component of the pipeline is used to generate shell files for each part of the pipeline and submit them on an SGE or a SLURM scheduler. The two other components of the PoolSex pipeline are [PoolSex-analyses](https://github.com/INRA-LPGP/poolsex_analysis), which outputs FST, sex-specific SNPs, and coverage from the final output of PoolSex, and [PoolSex-vis](https://github.com/INRA-LPGP/PoolSex-vis), an R package to visualize the results of PoolSex-analyses.

## Requirements

- Python (>= 3.5)
- Bwa (>= 0.7.12-r1039)
- Samtools (>= 1.3.1)
- Picard tools (>= 2.1.1)
- Popoolation2 (>=1201)

## Installation

- Clone: `git clone https://github.com/INRA-LPGP/PoolSex.git`
- Alternative: Download the archive and unzip it

## Quickstart

- Create a basic input directory. This directory should have the following structure:

```.
├─── genomes
|     ├────── <species_name>_genome.<fasta/fa/fna>
└─── reads
      ├────── <sex>_<lane>_<mate_number>.<fasta/fastq><.gz>
      ├────── <sex>_<lane>_<mate_number>.<fasta/fastq><.gz>
      └────── ...
```

- Run `python3 poolsex.py init -i path_to_folder`. This command generates a full directory structure and a default settings file which contains important settings values.
Each value is specified on one line with the syntax `setting=value`. For instance, the number of threads to use can be set to 16 with the line `threads=16`.
See the [usage](#init) section for details on the available settings.

- Run `python3 poolsex.py run -i path_to_folder`

- The final output files will be located in the `results` folder under the name(s) `mpileup2sync_<sex1>_<sex2>.sync`.

- These files can then be used as input for the `poolsex_analysis` software

## Description

The PoolSex pipeline generates and runs scripts to process pooled sequencing data for the analysis of sex determination. This processing is divided in 8 steps:

- Indexing the reference genome with BWA
- Mapping the reads to the reference genome with BWA mem
- Sorting the resulting BAM files with Picard Sort
- Adding read groups to the BAM files with Picard AddReadGroups
- Merging BAM files for each sex when sequencing was performed on multiple lanes
- Removing PCR duplicates with Picard MarkDuplicates
- Generating a pileup file with Samtools
- Generating a sync file with Popoolation

The pipeline is designed to run on a computational platform using an SGE or a SLURM scheduler. Please note that the pipeline was developed and tested in a specific environment (the [Genotoul](http://bioinfo.genotoul.fr/) platform), and the pipeline may have to be adapted to work in other environments.

The resulting sync file is used as the main input in the [poolsex_analysis software](https://github.com/INRA-LPGP/poolsex_analysis).

## Usage

### General

`python3 poolsex.py <command> [options]`

**Available commands** :

Command            | Description
------------------ | ------------
`init`             | Create a full input directory from a minimal input directory
`run`              | Generate shell scripts and run the pipeline from an input directory
`clean`            | Cleanup all files generated by this pipeline in a directory
`restart`          | Restart the pipeline from the last completed step or from a chosen step

### init

`python3 poolsex.py init -i input_dir_path`

*Create a full input directory from a minimal input directory. Populate a settings file with default values.*

**Options** :

Option | Long flag | Description
------ | --------- | ---
`-i`   | --input-folder | Path to a minimal input directory with the correct structure |

**Minimal input directory structure** :

```
.
├─── genomes
|     ├────── <species_name>_genome.<fasta/fa/fna>
└─── reads
      ├────── <sex>_<lane>_<mate_number>.<fasta/fastq><.gz>
      ├────── <sex>_<lane>_<mate_number>.<fasta/fastq><.gz>
      └────── ...
```

**Settings file** :

The settings file is used to define the values of the pipeline's parameters, which are summarized in the following table:

Setting          | Description                                       | Default value
---------------- | ------------------------------------------------- | -----------------
scheduler        | Type of scheduler ("sge" / "slurm")               | `slurm`
threads          | Number of threads to use when possible            | `16`
mem              | Total memory to allocate (for SGE or SLURM)       | `21G`
h_vmem           | Upper memory limit (for SGE only)                 | `25G`
bwa              | Path to BWA executable                            | `bwa`
samtools         | Path to Samtools executable                       | `samtools`
popoolation      | Path to Popoolation mpileup2sync.jar              | `mpileup2sync.jar`
picard           | Path to Picard java executable                    | `picard.jar`
java             | Path to java JRE executable                       | `java`
java_mem         | Total memory allocated to java                    | `20G`
max_file_handles | Maximum of file handles for Picard MarkDuplicates | `1000`

Each value is specified on one line with the syntax `setting=value`. Default values in the previous table are used when no user-specified value is available. Below is an example of *settings.txt* file to set the number of threads to **8** and the total memory to **45G**:
```
threads=8
mem=45G
```

### run

`python3 poolsex.py run -i input_dir_path [--dry-run --clean-temp]`

*Generate shell files for every step of the pipeline as well as a global shell file to run the pipeline, and can submit the jobs to a SGE scheduler.*

**Options** :

Option | Long flag      | Description
------ | -------------- | -----------
`-i`   | --input-folder | Path to a minimal input directory with the correct structure |
`-d`   | --dry-run      | If --dry-run is specified, the pipeline will generate the shell files without running the jobs |
`-c`   | --clean-temp   | Delete results from intermediate steps. Only index files, BAM files are duplicates removal, and mpileup2sync results will be kept. |


### clean

`python3 poolsex.py clean -i input_dir_path`

*Clean shell files, results files, and qsub output files from a PoolSex directory*

**Options** :

Option | Long flag | Description
--- | --- | ---
`-i` | --input-folder | Path to a PoolSex input folder |

### restart

`python3 poolsex.py restart -i input_dir_path [ -s step --run-jobs --clean-temp]`

*Restart the pipeline from the last completed step or from a specified step*

**Options** :

Option | Long flag | Description
--- | --- | ---
`-i` | --input-folder | Path to a PoolSex input folder |
`-s` | --step | Step to restart from (index, mapping, sort, groups, merge, duplicates, mpileup, mpileup2sync) |
`-d` | --dry-run | If --dry-run is specified, the pipeline will generate the shell files without running the jobs |
`-c` | --clean-temp | Delete results from intermediate steps. Only index files, BAM files are duplicates removal, and mpileup2sync results will be kept. |

## LICENSE

Copyright (C) 2018 Romain Feron and INRA LPGP

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
