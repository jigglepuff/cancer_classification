import requests
import json
import pandas as pd
import os
import sys

def retrieveFileMeta(file_ids,outputfile):
    '''

    Get the tsv metadata for the list of case_ids
    Args:
        file_ids: numpy array of file_ids
        outputfile: the output filename

    '''
    size = case_ids.shape[0] + 1000
    fd = open(outputfile,'w')
    cases_endpt = 'https://api.gdc.cancer.gov/files'

    # The 'fields' parameter is passed as a comma-separated string of single names.
    fields = [
        "file_id",
        "file_name",
        "cases.submitter_id",
        "cases.case_id",
        "data_category",
        "data_type",
        # "cases.samples.tumor_descriptor",
        # "cases.samples.tissue_type",
        "cases.project.disease_type",
        # "cases.project.name",
        "cases.project.project_id",
        "cases.samples.sample_type",
        "cases.samples.submitter_id",
        "cases.samples.sample_id",
        "cases.samples.portions.analytes.aliquots.aliquot_id"
        # "cases.samples.portions.analytes.aliquots.submitter_id"
        ]

    filters = {
        "op":"in",
        "content":{
            "field":"files.file_id",
            "value": file_ids.tolist()
        }
    }
    #print(filters)
    fields = ','.join(fields)

    params = {
        "filters" : filters,
        "fields": fields,
        "format": "CSV",
        "pretty": "true",
        "size": size
    }
    # print (params)
    #print (filters)
    #print (fields)
    
    
    response = requests.post(cases_endpt, headers = {"Content-Type": "application/json"},json = params)
    fd.write(response.content.decode("utf-8"))
    fd.close()

    # print(response.content)


def retrieveCaseMeta(case_id,outputfile):
    '''

    Get the tsv metadata for the list of case_ids
    Args:
        file_ids: numpy array of file_ids
        outputfile: the output filename

    '''
    print (case_ids.shape[0])
    size = case_ids.shape[0] + 1000
    fd = open(outputfile,'w')
    cases_endpt = 'https://api.gdc.cancer.gov/cases'

    fields = [
        "case_id",
        "project.project_id",
        "files.cases.project.project_id",
        "files.cases.project.program.name",
        "primary_site",
        "disease_type",
        "diagnoses.vital_status",
        "demographic.gender",
        "demographic.race",
        "demographic.year_of_birth"
        # "exposures.bmi",
        # "exposures.height",
        # "exposures.weight",
        # "exposures.cigarettes_per_day",
        # "exposures.alcohol_history",
        # "exposures.alcohol_intensity",
        # "exposures.years_smoked"
        ]


    filters = {
        "op":"in",
        "content":{
            "field":"cases.case_id",
            "value": case_id.tolist()
        }
    }

    # print (filters)
    fields = ','.join(fields)
    #expand group is diagnosis and demoragphic
    params = {
        # "filters" : filters,
        "fields": fields,
        # "expand" : "diagnoses,demographic,exposures",
        "format": "CSV",
        "pretty": "true",
        "size": size
    }
    # print (params)
    #print (filters)
    #print (fields)
    
    
    response = requests.post(cases_endpt, headers = {"Content-Type": "application/json"},json = params)
    # print (response.content.decode("utf-8"))
    fd.write(response.content.decode("utf-8"))
    fd.close()

def genCasePayload(file_ids,payloadfile):
    '''
    Used for the curl method to generate the file payload.
    '''

    fd = open(payloadfile,"w")
    filters = {
        "filters":{
            "op":"in",
            "content":{
                "field":"cases.case_id",
                "value": file_ids.tolist()
            }
        },
        "format":"TSV",
        "expand" : "diagnoses,demographic,exposures",
        "size": "1000",
        "pretty": "true"
    }
    json_str = json.dumps(filters)
    fd.write(json_str)
    fd.close()
    # return json_str

def genFilePayload(file_ids,payloadfile):
    '''
    Used for the curl method to generate the payload.
    '''


    fd = open(payloadfile,"w")
    filters = {
        "filters":{
            "op":"in",
            "content":{
                "field":"files.file_id",
                "value": file_ids.tolist()
            }
        },
        "format":"TSV",
        "fields":"file_id,file_name,cases.submitter_id,cases.case_id,data_category,data_type,cases.samples.tumor_descriptor,cases.samples.tissue_type,cases.samples.sample_type,cases.samples.submitter_id,cases.samples.sample_id,cases.samples.portions.analytes.aliquots.aliquot_id,cases.samples.portions.analytes.aliquots.submitter_id",
        "pretty":"true",
        "size": "1000"
    }
    json_str = json.dumps(filters)
    fd.write(json_str)
    fd.close()




def curlFileMeta(file_ids,payloadfile,outputfile):
    genFilePayload(file_ids,payloadfile)
    os.system("curl --request POST --header \"Content-Type: application/json\" --data @"+payloadfile+" 'https://api.gdc.cancer.gov/files' > "+outputfile)

def curlCaseMeta(case_ids,payloadfile,outputfile):
    genCasePayload(case_ids,payloadfile)
    os.system("curl --request POST --header \"Content-Type: application/json\" --data @"+payloadfile+" 'https://api.gdc.cancer.gov/cases' > "+outputfile)





if __name__ == '__main__':

    # data_dir = "/Users/yueshi/Downloads/project/data/"
    # filename = data_dir+"file_case_id_DNA.csv"
    data_dir = sys.argv[1]
    filename = sys.argv[2]
    
    df = pd.read_csv(filename)
    file_ids = df.file_id.values
    case_ids = df.case_id.values
    # print(case_ids)
    
    fileids_meta_outfile = data_dir + "files_meta.csv"
    caseids_meta_outfile = data_dir + "cases_meta.csv"

    # python request method
    retrieveFileMeta(file_ids,fileids_meta_outfile)
    retrieveCaseMeta(case_ids,caseids_meta_outfile)



    # the curl method
    '''
    filepayload = "FilePayload"
    casepayload = "CasePayload"
    fileids_meta_outfile = "curl_files_meta.tsv"
    caseids_meta_outfile = "curl_cases_meta.tsv"
    curlFileMeta(file_ids,filepayload,fileids_meta_outfile)
    curlCaseMeta(case_ids,casepayload,caseids_meta_outfile)
    '''
    
