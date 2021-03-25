# N50_Statistic

By [Daniel Peter-Salawu](mailto:danielpetersalawu@gmail.com)

## Instructions

1. Navigate to [repo](https://github.com/DPS7991/N50_Statistic)
2. Clone locally using `git clone https://github.com/DPS7991/N50_Statistic.git`
3. In the terminal, run `python calculateN50statistic.py "path to fasta file"`

## Discussion

I used Python and the sys module for accepting the fasta file as a command line parameter.
A sample fasta file is available for testing.

## Requirements

#### Accept draft genome assembly in FASTA format as a command line parameter

#### Calculate the N50 statistic for the given draft genome assembly and output to STDOUT

I created a function for parsing the FASTA file and another function for calculating the N50 value as an integer.
