# SNPr
Introduce point mutations (SNPs) in FASTA at specified frequency.

## Running snpr

1. Clone the repo and go inside

2. Install all required packages from Pipfile

```console
$ pipenv install
```

3. Activate the Pipenv shell

```console
$ pipenv shell
```

4. You are now ready to use snpr

Check out the help menu.

```console
$ python snpr.py --help
Usage: snpr.py [OPTIONS] FASTA

  Given a FASTA file, introduce SNPs at the specified frequency.

Options:
  -f, --freq FLOAT           Mutation (SNP) frequency. Default: 0.01 (1%)
  -r, --random_seed INTEGER  Seed for pseudo-random runs. Default: None
  --help                     Show this message and exit.
```

Example command to introduce 1% of SNPs in the supplied test FASTA files. Using the optional random seed argument provides pseudo-random runs, for reproducible output.

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

$ python snpr.py -f 0.01 -r 111 test.fa
>chrA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAA
>chrT
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTATTTTTTTTTTTTTTTTTTTATTTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
>chrC
CCCCCCCCCCACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCC

$ python snpr.py -f 0.01 -r 111 test_wrapped.fa
>chrA
AAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAA
>chrT
TTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTATTTTTTTTTTT
TTTTTTTTATTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTTTTTTT
>chrC
CCCCCCCCCCACCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCC
```

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) file for details.
