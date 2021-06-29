#-*- coding:utf-8 -*-
from simple_salesforce import Salesforce
import concurrent.futures
import requests
import chardet
import os
import json
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader
import io
def test():
    url = 'http://ext.qms.lgchem.com/Front_Data/QMS/REPORT/202106/S2A0B28C7C10A4D9A9368467E7A29390C/report_202106280237094341.pdf'

    response = requests.get(url, headers={"Content-Type": "application/pdf; charset=utf-8'"})
    print(response.content)
    print(response.text)
    # print(chardet.detect())

    with open('tttt6.pdf', "wb",encoding='EUC-KR') as output_file:
        output_file.write(response.content)


def salesforceCon():

    sf = Salesforce(username=username, password=password, security_token="", domain="test")

    print("session Id : " + sf.session_id)
    return sf


def download_file(args):
    print('=== download_file===')
    record, sf = args

    url = "https://%s%s" % (sf.sf_instance, record["VersionData"])

    response = requests.get(url, headers={"Authorization": "OAuth " + sf.session_id,
                                          "Content-Type": "application/octet-stream"})
    print(response)
    if response.ok:
        with open('test123.pdf', "wb") as output_file:
            output_file.write(response.content)
        return None
    else:
        return "Couldn't download %s" % url

def file_merge():
    print('=== file merge ===')
    fileName = 'test123.pdf'

    merger = PdfFileMerger(strict=False)
    PASSWORD = ''


    with open(fileName,'rb') as f:

        reader = PdfFileReader(f)
        if reader.isEncrypted:
            try:
                reader.decrypt(PASSWORD)
            except NotImplementedError:
                print('isEncrypted')

        command = f"qpdf --decrypt {'test123.pdf'} {'test123_decrypt.pdf'};"
        os.system(command)
        merger.append('test123_decrypt.pdf')
        print('decrypt : test123')


    merger.write(fileName)
    merger.close()

global username
global password
global domain

username = 'deokjun.kim@lgcpartner.com.full'
password = 'password123'

record = {}
record["VersionData"] = '/services/data/v52.0/sobjects/ContentVersion/0686D000000wK7JQAU/VersionData'
# record["Title"] + '.' + record["FileExtension"]
# sf = salesforceCon()
# args = ((record, sf))
# download_file(args)
# file_merge()
test()
# print(record, sf)