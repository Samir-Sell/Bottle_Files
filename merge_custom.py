import pandas as pd

pd.set_option("max_columns", None)

bottle = "C:/Users/16136/Documents/GCRC/UC3/data_ctd_Greenedge_2016_Btl_1601001.btl"

values = []

#open bottle file and parse out metadata
with open(bottle) as bottle_file:
    for row in bottle_file:
        if row.startswith("*") or row.startswith("#"):
            continue

        #append data to list
        values.append(row.rstrip())

#organize data into subsections based on patterns
headers = values[0:1]
all_data = values[2:]
avg_data = values[2::2]
std_data = values[3::2]

#parse through and organize dara rows
proc_btl_rows = []
for row in avg_data:
    new_rows = row.split(" ")
    while "" in new_rows: new_rows.remove("")
    new_rows.remove("(avg)")
    new_rows[1:4] = ["".join(new_rows[1:4])]
    proc_btl_rows.append(new_rows[:-1])

#parse through an organize column headers
new_title = []
for title in headers:
    col_names = title.split(" ")
    while "" in col_names: col_names.remove("")
    new_title.append(col_names)

flat_list = [item for sublist in new_title for item in sublist]


#Test if rows and columns match up correctly and create a pandas dataframe
if len(proc_btl_rows[0]) == len(flat_list):
    print("Columns and Rows align!")
    df = pd.DataFrame(data=proc_btl_rows, columns=flat_list)
    
else:
    print("Something is wrong")
    print("lenth of columns:", len(flat_list))
    print(flat_list)
    print("length of rows is:", len(proc_btl_rows[0]))
    print(proc_btl_rows[0])
