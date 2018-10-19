# cancer_classification
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
[2018-10-19 00:33:06,960 - GDC - INFO] Label 0 count:691
[2018-10-19 00:33:06,966 - GDC - INFO] Label 1 count:1103
[2018-10-19 00:33:06,969 - GDC - INFO] Label 2 count:546
[2018-10-19 00:33:06,973 - GDC - INFO] Label 3 count:525
[2018-10-19 00:33:06,976 - GDC - INFO] Label 4 count:545
[2018-10-19 00:33:06,982 - GDC - INFO] Label 5 count:521
[2018-10-19 00:33:06,986 - GDC - INFO] Label 6 count:530
[2018-10-19 00:33:06,988 - GDC - INFO] Label 7 count:514
[2018-10-19 00:33:06,993 - GDC - INFO] Label 8 count:499
[2018-10-19 00:33:06,995 - GDC - INFO] Label 9 count:499
[2018-10-19 00:33:07,003 - GDC - INFO] Label 10 count:478
[2018-10-19 00:33:07,007 - GDC - INFO] Label 11 count:450
[2018-10-19 00:33:07,011 - GDC - INFO] Label 12 count:457
[2018-10-19 00:33:07,014 - GDC - INFO] Label 13 count:446
[2018-10-19 00:33:07,018 - GDC - INFO] Label 14 count:418
[2018-10-19 00:33:07,021 - GDC - INFO] Label 15 count:375
[2018-10-19 00:33:07,028 - GDC - INFO] Label 16 count:309
[2018-10-19 00:33:07,031 - GDC - INFO] Label 17 count:292
[2018-10-19 00:33:07,033 - GDC - INFO] Label 18 count:404
[2018-10-19 00:33:07,036 - GDC - INFO] Label 19 count:263
[2018-10-19 00:33:07,038 - GDC - INFO] Label 20 count:187
[2018-10-19 00:33:07,041 - GDC - INFO] Label 21 count:184
[2018-10-19 00:33:07,044 - GDC - INFO] Label 22 count:179
[2018-10-19 00:33:07,047 - GDC - INFO] Label 23 count:162
[2018-10-19 00:33:07,050 - GDC - INFO] Label 24 count:156
[2018-10-19 00:33:07,053 - GDC - INFO] Label 25 count:132
[2018-10-19 00:33:07,055 - GDC - INFO] Label 26 count:124
[2018-10-19 00:33:07,058 - GDC - INFO] Label 27 count:87
[2018-10-19 00:33:07,060 - GDC - INFO] Label 28 count:80
[2018-10-19 00:33:07,064 - GDC - INFO] Label 29 count:80
[2018-10-19 00:33:07,068 - GDC - INFO] Label 30 count:66
[2018-10-19 00:33:07,071 - GDC - INFO] Label 31 count:57
[2018-10-19 00:33:07,078 - GDC - INFO] Label 32 count:47
[2018-10-19 00:33:07,081 - GDC - INFO] Label 33 count:44
[2018-10-19 00:33:07,083 - GDC - INFO] Label 34 count:36
[2018-10-19 00:33:07,086 - GDC - INFO] Label 35 count:0
[2018-10-19 00:33:07,086 - GDC - INFO] Total sample count:11486

## Run prediction model:
python predict.py [/path/to/miRNA_matrix.csv]



## Run prediction model on AWS Sagemaker:
1. Start AWS Sagemaker notebook instance (with appropriate ARN etc.)
2. Upload predict_sagemaker.ipynb to home directory on jupyter notebook 
3. Create utils directory on jupyter notebook
4. Enter utils directory, upload all files in GDCproject/src/utils 