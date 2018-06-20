#!/usr/bin/env python

"""
    SNPer
    ~~~~~
    SNPer introduces point mutations (SNPs) in a given FASTA file at a specified
    mutation frequency.

    :license: MIT, see LICENSE for more details.
"""

__author__ = "Luis Vale Silva"
__status__ = "Development"

import click
from random import random, choice, seed


@click.command()
@click.option('-f', '--fasta', required=True, help='FASTA file.')
@click.option('-s', '--snp_freq', default=0.01,
              help='Mutation (SNP) frequency. Default: 0.01 (1%).')
@click.option('-r', '--random_seed', type=int, default=None,
              help='Seed for pseudo-random runs. Default: None.')
def mutate(fasta, snp_freq, random_seed=None):
    """Given a fasta file, introduce SNPs at the specified frequency."""
    if random_seed is not None:
        seed(random_seed)

    with open(fasta) as f:
        for line in f:
            # If this line is a header just print it
            if line.startswith('>'):
                click.echo(line.strip())
            # If not, introduce SNPs at specified frequency and then print it
            else:
                line = list(line.strip())
                for i, nt in enumerate(line):
                    mut = random()
                    if mut < snp_freq:
                        # Introduce SNP
                        line[i] = choice([x for x in 'ACTG' if x != nt.upper()])
                click.echo(''.join(line))


if __name__ == '__main__':
    mutate()
