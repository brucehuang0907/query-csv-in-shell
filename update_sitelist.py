#! /Library/Frameworks/Python.framework/Versions/Current/bin/python3

import pandas as pd
import sys

if __name__=="__main__":
    file_path = sys.argv[1]
    if ".csv" not in file_path:
        file_path = input('Please input the file path of trt export CSV file, default fold is ~/Downloads/:')

    if "/" not in file_path:
        file = f'/Users/huahuang/Downloads/{file_path}'
    else:
        file = file_path
    df = pd.read_csv(file,usecols=['site_code','subnet','id','system_name','it_function','country'])
    df.dropna(axis=0,how='any',inplace=True)
    df = df[df['country'].str.contains('CN|TW|HK|MO',case=False)]
    df.to_csv('/usr/local/bin/sitelist.txt',columns=['site_code','subnet','id','system_name','it_function'],index=False,float_format=str)
    print(f'{file_path} updated to /usr/local/bin/sitelist.txt')
