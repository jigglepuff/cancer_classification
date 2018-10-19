# copyright: yueshi@usc.edu
import pandas as pd 
import hashlib
import os 
from utils import logger
import sys

def file_as_bytes(file):
    with file:
        return file.read()

def check(dirname,total):
	'''
	check the md5 for each file downloaded. if md5 does not match, report error.
	'''
	count = 0
	for idname in os.listdir(dirname):
		# list all the ids 
		if idname.find("-") != -1:
			idpath = dirname +"/" + idname

			for filename in os.listdir(idpath):
				# check the miRNA file
				if filename.find("-") != -1:
					filepath = idpath + "/" + filename
					filehash = hashlib.md5(file_as_bytes(open(filepath, 'rb'))).hexdigest()
					if df.loc[df['filename'] == filename].md5.values[0] != filehash:
						logger.info("file id {} download fails, please downlaod again".format(idname))
					else:
						count +=1
	if count == total:
		logger.info("successful downloads")


if __name__ == '__main__':

	logger.info(4*"="+"start checking"+4*"=")
	# the manifest file. modify file when use
	# print ("first arg", sys.argv[1])
	# manifest_file = "/Users/yueshi/Downloads/project/data/gdc_manifest.2018-08-20.txt"
	manifest_file = sys.argv[1]
	df = pd.read_csv(manifest_file,sep='\t')
	total = df.shape[0]
	
	# The directory that holds the data. Modify this when use.
	dirname = sys.argv[2]
	# dirname = "/Users/yueshi/Downloads/project/data/live_miRNA"
	check(dirname,total)
	logger.info(4*"="+"check finished"+4*"=")

 	




