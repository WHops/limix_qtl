from load_genotypes import load_genotypes_plink
from generate_kinship import generate_kinship
import pandas as pd
import pdb
import numpy as np
np.set_printoptions(threshold=np.inf)
#geno_prefix = '../test_data/geuvadis_CEU_YRI_test_data/Geuvadis_chr1'
geno_prefix = '/home/hoeps/PhD/projects/huminvs/inv_vcf/try2/plink'
output_filename = geno_prefix+'_kinship.txt'

bim,fam,bed,genotype_mat = load_genotypes_plink(geno_prefix)
kinship_mat = generate_kinship(genotype_mat)

kinship_df = pd.DataFrame(data=kinship_mat,index=fam['iid'],columns=fam['iid'])

kinship_df.to_csv(output_filename,sep='\t')
