import numpy as np
import math
import scipy

def generate_kinship(genotypes):
    kchr = genotypes
    #standardise
    kchr -= kchr.mean(axis=0)
    k_std = kchr.std(axis=0)
    k_std[k_std==0] = k_std.mean()
    kchr /= k_std

    kinship = scipy.dot(kchr, kchr.T)
    return kinship
