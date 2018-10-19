# copyright: yueshi@usc.edu
import pandas as pd 
import hashlib
import os 
from utils import logger
import sys

def file_as_bytes(file):
    with file:
        return file.read()

def extractMatrix(dirname):
	'''
	return a dataframe of the miRNA matrix, each row is the miRNA counts for a file_id

	'''
	count = 0

	miRNA_data = []
	for idname in os.listdir(dirname):
		# list all the ids 
		if idname.find("-") != -1:
			idpath = dirname +"/" + idname

			# all the files in each id directory
			for filename in os.listdir(idpath):
				# check the miRNA file
				if filename.find("-") != -1:

					filepath = idpath + "/" + filename
					df = pd.read_csv(filepath,sep="\t")
					# columns = ["miRNA_ID", "read_count"]
					if count ==0:
						# get the miRNA_IDs 
						miRNA_IDs = df.miRNA_ID.values.tolist()

					id_miRNA_read_counts = [idname] + df.read_count.values.tolist()
					miRNA_data.append(id_miRNA_read_counts)


					count +=1
					# print (df)
	columns = ["file_id"] + miRNA_IDs
	df = pd.DataFrame(miRNA_data, columns=columns)
	return df

def extractNorm(files):
	# df = pd.read_csv(files, sep="\t")
	df = pd.read_csv(files, sep=",")
	#
	# print (df[columns])
	df['tissue_type'] = df['cases.0.samples.0.sample_type']
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Normal"), 'tissue_type'] = 0
	df.loc[~df['cases.0.samples.0.sample_type'].str.contains("Normal"), 'tissue_type'] = 1
	tumor_count = df.loc[df.tissue_type == 1].shape[0]
	normal_count = df.loc[df.tissue_type == 0].shape[0]
	logger.info("{} Normal samples, {} Tumor samples ".format(normal_count,tumor_count))
	columns = ['file_id','tissue_type']
	return df[columns]



def extractDis(files):
	# df = pd.read_csv(files, sep="\t")
	df = pd.read_csv(files, sep=",")
	# 
	# print (df[columns])
	df['disease_type'] = df['cases.0.project.disease_type']
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Normal"), 'disease_type'] = 0 # Normal
	df.loc[df['cases.0.project.disease_type'].str.contains("Breast"), 'disease_type'] = 1 # TCGA-BRCA
	df.loc[df['cases.0.project.disease_type'].str.contains("Uterine Corpus"), 'disease_type'] = 2 # TCGA-UCEC
	df.loc[df['cases.0.project.disease_type'].str.contains("Head"), 'disease_type'] = 3 # TCGA-HNSC
	df.loc[df['cases.0.project.disease_type'].str.contains("Kidney Renal Clear"), 'disease_type'] = 4 # TCGA-KIRC
	df.loc[df['cases.0.project.disease_type'].str.contains("Lung Adenocarcinoma"), 'disease_type'] = 5 # TCGA-LUAD
	df.loc[df['cases.0.project.disease_type'].str.contains("Brain"), 'disease_type'] = 6 # TCGA-LGG
	df.loc[df['cases.0.project.disease_type'].str.contains("Thyroid"), 'disease_type'] = 7 # TCGA-THCA
	df.loc[df['cases.0.project.disease_type'].str.contains("Prostate"), 'disease_type'] = 8 # TCGA-PRAD
	df.loc[df['cases.0.project.disease_type'].str.contains("Ovarian"), 'disease_type'] = 9 # TCGA-OV
	df.loc[df['cases.0.project.disease_type'].str.contains("Lung Squamous"), 'disease_type'] = 10 # TCGA-LUSC
	df.loc[df['cases.0.project.disease_type'].str.contains("Skin"), 'disease_type'] = 11 # TCGA-SKCM
	df.loc[df['cases.0.project.disease_type'].str.contains("Colon"), 'disease_type'] = 12 # TCGA-COAD
	df.loc[df['cases.0.project.disease_type'].str.contains("Stomach"), 'disease_type'] = 13 # TCGA-STAD
	df.loc[df['cases.0.project.disease_type'].str.contains("Bladder"), 'disease_type'] = 14 # TCGA-BLCA
	df.loc[df['cases.0.project.disease_type'].str.contains("Liver"), 'disease_type'] = 15 # TCGA-LIHC
	df.loc[df['cases.0.project.disease_type'].str.contains("Cervical"), 'disease_type'] = 16 # TCGA-CESC
	df.loc[df['cases.0.project.disease_type'].str.contains("Kidney Renal Papillary "), 'disease_type'] = 17 # TCGA-KIRP
	df.loc[df['cases.0.project.disease_type'].str.contains("Leukemia"), 'disease_type'] = 18 # TCGA-LAML the same as TARGET-AML
	df.loc[df['cases.0.project.disease_type'].str.contains("Sarcoma"), 'disease_type'] = 19 # TCGA-SARC
	df.loc[df['cases.0.project.disease_type'].str.contains("Esophageal"), 'disease_type'] = 20 # TCGA-ESCA
	df.loc[df['cases.0.project.disease_type'].str.contains("Pheochromocytoma"), 'disease_type'] = 21 # TCGA-PCPG
	df.loc[df['cases.0.project.disease_type'].str.contains("Pancreatic"), 'disease_type'] = 22 # TCGA-PAAD
	df.loc[df['cases.0.project.disease_type'].str.contains("Rectum"), 'disease_type'] = 23 # TCGA-READ
	df.loc[df['cases.0.project.disease_type'].str.contains("Testicular"), 'disease_type'] = 24 # TCGA-TGCT
	df.loc[df['cases.0.project.disease_type'].str.contains("Wilms"), 'disease_type'] = 25 # TARGET-WT
	df.loc[df['cases.0.project.disease_type'].str.contains("Thymoma"), 'disease_type'] = 26 # TCGA-THYM
	df.loc[df['cases.0.project.disease_type'].str.contains("Mesothelioma"), 'disease_type'] = 28 # TCGA-MESO
	df.loc[df['cases.0.project.disease_type'].str.contains("Adrenocortical"), 'disease_type'] = 29 # TCGA-ACC
	df.loc[df['cases.0.project.disease_type'].str.contains("Uveal"), 'disease_type'] = 30 # TCGA-UVM
	df.loc[df['cases.0.project.disease_type'].str.contains("Kidney Chromophobe"), 'disease_type'] = 31 # TCGA-KICH
	df.loc[df['cases.0.project.disease_type'].str.contains("Uterine Carcinosarcoma"), 'disease_type'] = 32 # TCGA-UCS
	df.loc[df['cases.0.project.disease_type'].str.contains("Lymphoid"), 'disease_type'] = 33 # TCGA-DLBC
	df.loc[df['cases.0.project.disease_type'].str.contains("Rhabdoid"), 'disease_type'] = 34 # TARGET-RT
	df.loc[df['cases.0.project.disease_type'].str.contains("Cholangiocarcinoma"), 'disease_type'] = 35 # TCGA-CHOL
	df.loc[df['cases.0.project.disease_type'].str.contains("Glioblastoma"), 'disease_type'] = 35 # TCGA-CHOL
	# checking
	normal_count = df.loc[df.disease_type == 0].shape[0]
	BRCA_count = df.loc[df.disease_type == 1].shape[0]
	UCEC_count = df.loc[df.disease_type == 2].shape[0]
	logger.info("{} Normal samples\n {} Breast cancer\n {} Uterine Corpus\n".format(normal_count,BRCA_count,UCEC_count))
	columns = ['file_id','disease_type']
	return df[columns]

if __name__ == '__main__':


	# data_dir ="/Users/yueshi/Downloads/project/data/"
	# Input directory and label file. The directory that holds the data. Modify this when use.
	# dirname = data_dir + "live_miRNA"
	# label_file = data_dir + "files_meta.tsv"
	
	# #output file
	# outputfile = data_dir + "miRNA_matrix.csv"

	dirname = sys.argv[1] # dir to live_miRNA
	file_meta = sys.argv[2] # dir to files_meta.tsv
	cases_meta = sys.argv[2] # dir to files_meta.tsv
	outputfile = sys.argv[4] # output filename 

	# extract data
	matrix_df = extractMatrix(dirname)
	# normal_df = extractNorm(file_meta)
	disease_df = extractDis(file_meta)

	# #merge the two based on the file_id
	result = pd.merge(matrix_df, disease_df, on='file_id', how="left")
	# #print(result)

	# #save data
	result.to_csv(outputfile, index=False)
	# #print (labeldf)

 




