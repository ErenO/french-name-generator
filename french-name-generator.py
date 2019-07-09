#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd
from random import randint

df_fname = pd.read_csv('Prenoms.csv', sep=';', encoding = "ISO-8859-1")
df_lname = pd.read_csv('noms2008nat_txt.txt', sep='\t', encoding = "ISO-8859-1")

fnames = len(df_fname['01_prenom'].values)
lnames = len(df_lname['NOM'].values)

print ("nombre de prenoms: {}, nombre de noms: {}".format(fnames, lnames).encode('ascii', 'ignore').decode('ascii'))

fname_nb = randint(0, fnames)
lname_nb = randint(0, lnames)

print ("Mon nom est: {} {}".format(df_fname['01_prenom'].values[fname_nb].capitalize(),
                                                     df_lname['NOM'].values[lname_nb]).encode('ascii', 'ignore').decode('ascii'))