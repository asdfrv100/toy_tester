import pandas as pd
import numpy as np


#파일 위치 입력


from_axis_path_file="hand"
from_mag_path_file="pocket"
to_mag_path_file="changed_pocket"

#파일명 입력
file_name = 'hana'
result_file_name = 'test'

diff_num=3

#파일 행 수 체크

for i in range(1,10) :
    axis_data = pd.read_csv(f"{from_axis_path_file}/{file_name}{i}.txt",
                      sep = "\t", engine = 'python', encoding = "cp949", header = None)
    poceket_mag_data = pd.read_csv(f"{from_mag_path_file}/{file_name}{i}.txt",
                      sep = "\t", engine = 'python', encoding = "cp949", header = None)

    axis_data=axis_data[[0,1]]
    poceket_mag_data=poceket_mag_data.drop([0,1,2,3,4], axis=1)

#    print(axis_data)
#    print(poceket_mag_data)
    df_result = pd.concat([axis_data,poceket_mag_data],axis=1,sort=False)
#    df_result=axis_data.append([poceket_mag_data])
#    df_result.head()
#    print(df_result)
    df_result.to_csv(f"{to_mag_path_file}/{result_file_name}{i}.txt",sep = "\t",index =False,header =False)
