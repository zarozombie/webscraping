import pandas as pd
import os

def format_line(label_txt): 
    print("\n\n", "-----"*10, "\n\n", label_txt)

format_line("Current Working Dir")
print(os.getcwd())

format_line("Files")
print(os.listdir())

format_line("Load File")
file_n = "excel_text.xls"
#xl = pd.ExcelFile(file_n)
xl = pd.read_excel(open('excel_test.xls', 'rb'))
print(xl)

#--------------------- Creating Pandas DataFrame

d = {'col1': [3,4], 'col2' : [3,4]}
df = pd.DataFrame(data=d)

#---------------------Overwrite using Pandas DataFrame
#format_line("overwritten File")
#writer = pd.ExcelWriter('excel_test.xls')
#df.to_excel(writer)
#writer.save()

#--- remove header and index and append or overwrite? csv to xls
#df.to_csv('excel_test.xls', sep=',', index=False, header=False)
#df = df.to_csv(index=False, header=False)


#--------------------Append Data using Pandas DataFrame

#format_line("Created Table To Append")
#print(df)
#print(xl.sheet_names)


