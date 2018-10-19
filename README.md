# cancer_classification
#### Download miRNA data:
mkdir live_miRNA
cd live_miRNA
gdc-client download -m [path/to/manifest.txt]

## Check md5sum:
#### Download modified check.py from Google drive, replace the check.py in the GDCproject
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
#### Download modified parse_file_case_id.py from Google drive, replace the parse_file_case_id.py in the GDCproject
#### Run the following Command:
python gen_miRNA_matrix.py [/path/to/dir/live_miRNA/] [path/to/files_meta.tsv] [output/filepath/miRNA_matrix.csv]

## Run prediction model:
python predict.py [/path/to/miRNA_matrix.csv]



## Run prediction model on AWS Sagemaker:
1. Start AWS Sagemaker notebook instance (with appropriate ARN etc.)
2. Upload predict_sagemaker.ipynb to home directory on jupyter notebook 
3. Create utils directory on jupyter notebook
4. Enter utils directory, upload all files in GDCproject/src/utils 