# cancer_classification

#### Create virutal environment (example below is for miniconda):

conda create --name gdc_project python=3 <br>
source activate gdc_project <br>
conda install scikit-learn<br>
conda install pandas<br>
conda install matplotlib<br>
conda install requests<br>
conda install plotly<br>


#### Download miRNA data:
mkdir live_miRNA
cd live_miRNA
gdc-client download -m [path/to/manifest.txt]

## Check md5sum:
#### Run the following Command:
python check.py [path/to/manifest.txt] [path/to/live_miRNA/directory]
#### The output should be: 
[2018-10-17 15:15:59,779 - GDC - INFO] ====start checking====
first arg ../../manifests/gdc_manifest.2018-10-17.txt
[2018-10-17 15:16:00,747 - GDC - INFO] successful downloads
[2018-10-17 15:16:00,747 - GDC - INFO] ====check finished====

## Download clinical files:
#### Go back to web browser, download JSON file


## Get meta data for files:
python parse_file_case_id.py path/to/files.2018-10-17.json path/to/file_case_id_DNA.csv
#### Run the following Command:
python request_meta.py [path/to/output/directory] [path/to/output/file_case_id_DNA.csv]

## Generate miRNA matrix:
#### Run the following Command:
python gen_miRNA_matrix.py [/path/to/dir/live_miRNA/] [path/to/files_meta.csv] [path/to/cases_meta.csv] [output/filepath/miRNA_matrix.csv]
#### The output should be:
[2018-10-19 00:33:06,960 - GDC - INFO] Label 0 count:691 <br>
[2018-10-19 00:33:06,966 - GDC - INFO] Label 1 count:1103 <br>
[2018-10-19 00:33:06,969 - GDC - INFO] Label 2 count:546 <br>
[2018-10-19 00:33:06,973 - GDC - INFO] Label 3 count:525 <br>
[2018-10-19 00:33:06,976 - GDC - INFO] Label 4 count:545 <br>
[2018-10-19 00:33:06,982 - GDC - INFO] Label 5 count:521 <br>
[2018-10-19 00:33:06,986 - GDC - INFO] Label 6 count:530 <br>
[2018-10-19 00:33:06,988 - GDC - INFO] Label 7 count:514 <br>
[2018-10-19 00:33:06,993 - GDC - INFO] Label 8 count:499 <br>
[2018-10-19 00:33:06,995 - GDC - INFO] Label 9 count:499 <br>
[2018-10-19 00:33:07,003 - GDC - INFO] Label 10 count:478 <br>
[2018-10-19 00:33:07,007 - GDC - INFO] Label 11 count:450 <br>
[2018-10-19 00:33:07,011 - GDC - INFO] Label 12 count:457 <br>
[2018-10-19 00:33:07,014 - GDC - INFO] Label 13 count:446 <br>
[2018-10-19 00:33:07,018 - GDC - INFO] Label 14 count:418 <br>
[2018-10-19 00:33:07,021 - GDC - INFO] Label 15 count:375 <br>
[2018-10-19 00:33:07,028 - GDC - INFO] Label 16 count:309 <br>
[2018-10-19 00:33:07,031 - GDC - INFO] Label 17 count:292 <br>
[2018-10-19 00:33:07,033 - GDC - INFO] Label 18 count:404 <br>
[2018-10-19 00:33:07,036 - GDC - INFO] Label 19 count:263 <br>
[2018-10-19 00:33:07,038 - GDC - INFO] Label 20 count:187 <br>
[2018-10-19 00:33:07,041 - GDC - INFO] Label 21 count:184 <br>
[2018-10-19 00:33:07,044 - GDC - INFO] Label 22 count:179 <br>
[2018-10-19 00:33:07,047 - GDC - INFO] Label 23 count:162 <br>
[2018-10-19 00:33:07,050 - GDC - INFO] Label 24 count:156 <br>
[2018-10-19 00:33:07,053 - GDC - INFO] Label 25 count:132 <br>
[2018-10-19 00:33:07,055 - GDC - INFO] Label 26 count:124 <br>
[2018-10-19 00:33:07,058 - GDC - INFO] Label 27 count:87 <br>
[2018-10-19 00:33:07,060 - GDC - INFO] Label 28 count:80 <br>
[2018-10-19 00:33:07,064 - GDC - INFO] Label 29 count:80 <br>
[2018-10-19 00:33:07,068 - GDC - INFO] Label 30 count:66 <br>
[2018-10-19 00:33:07,071 - GDC - INFO] Label 31 count:57 <br>
[2018-10-19 00:33:07,078 - GDC - INFO] Label 32 count:47 <br>
[2018-10-19 00:33:07,081 - GDC - INFO] Label 33 count:44 <br>
[2018-10-19 00:33:07,083 - GDC - INFO] Label 34 count:36 <br>
[2018-10-19 00:33:07,086 - GDC - INFO] Label 35 count:0 <br>
[2018-10-19 00:33:07,086 - GDC - INFO] Total sample count:11486

## Run prediction model:
python predict.py [/path/to/miRNA_matrix.csv]



## Run prediction model on AWS Sagemaker:
1. Start AWS Sagemaker notebook instance (with appropriate ARN etc.)
2. Upload predict_sagemaker.ipynb to home directory on jupyter notebook 
3. Create utils directory on jupyter notebook
4. Enter utils directory, upload all files in GDCproject/src/utils 
