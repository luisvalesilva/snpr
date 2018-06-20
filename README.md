# snpr
Introduce point mutations (SNPs) in FASTA at specified frequency.

## Running snpr

1. Clone the repo and go inside

2. Install all required packages from Pipfile

```console
$ pipenv install
```

3. Activate the Pipenv shell:

```console
$ pipenv shell
```

4. You are now ready to use snpr:

Check out the help menu.

```console
$ python snpr.py --help


Usage: snpr.py [OPTIONS]

  Given a fasta file, introduce SNPs at the specified frequency.

Options:
  -f, --fasta TEXT           FASTA file.  [required]
  -s, --snp_freq FLOAT       Mutation (SNP) frequency. Default: 0.01 (1%).
  -r, --random_seed INTEGER  Seed for pseudo-random runs. Default: None.
  --help                     Show this message and exit.
```

Example commmand to introduce 1% of SNPs in the supplied test FASTA (using the random seed argument provides pseudo-random runs, for reproducible output).

```console
$ cat test.fa

>chrA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAA
>chrT
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
>chrC
CCCCCCCCCCCCCCCCCCCCCCC

$ python snpr.py -f test.fa -s 0.01 -r 42

>chrA
AAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAA
>chrT
TTTTTTTTTTTTTTTTTTTTTTTCTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTGTTTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
>chrC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCGCCCCCCCCCCCC
CCCCCCCACCCCCACCCCCC
```

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) file for details.
