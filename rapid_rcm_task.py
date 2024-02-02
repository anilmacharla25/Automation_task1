import numpy as numpy
import pandas as pd 
import tabula

def extract_pdf_dfs(pdf_path):
    # Read pdf into list of DataFrame
    dfs = tabula.read_pdf(pdf_path, pages='all')
    return dfs

def create_final_df(page_df):
    final_df_columns=page_df.iloc[0].to_list()
    final_df=pd.DataFrame(columns= ['Insurance Name']+final_df_columns)
    return final_df


def get_page_df(mini_df, final_df):
    mini_df= mini_df.dropna(subset=mini_df.columns[0])
    mini_df = mini_df[~mini_df[mini_df.columns[0]].str.contains(r'\$', na=False)]
    ins_company=mini_df.columns[0]
    for index,row in mini_df.iterrows():
        line_item= row.to_list()
        if line_item[0]=='VisitID':
            continue
        elif line_item[0]!='VisitID' and line_item[0].isdigit()==False:
            ins_company=line_item[0]
            continue
        else:
            # print(line_item)
            df_row=pd.DataFrame({
                final_df.columns[0]:[ins_company],
                final_df.columns[1]:[line_item[0]],
                final_df.columns[2]:[line_item[1]],
                final_df.columns[3]:[line_item[2]],
                final_df.columns[4]:[line_item[3]],
                final_df.columns[5]:[line_item[4]],
                final_df.columns[6]:[line_item[5]],
                final_df.columns[7]:[line_item[6]],
                final_df.columns[8]:[line_item[7]],
                final_df.columns[9]:[line_item[8]],
                final_df.columns[10]:[line_item[9]],
                final_df.columns[11]:[line_item[10]],
                final_df.columns[12]:[line_item[11]],
                final_df.columns[13]:[line_item[12]],
                
            })
            final_df=pd.concat([final_df,df_row], ignore_index=True)
    return final_df
    
            

#code starts from here
pdf_path= r"C:\Users\Raju\Desktop\Test\Report_CollectionReportInsurance-810904-b1ac4.pdf"
pages_df= extract_pdf_dfs(pdf_path)
final_df= create_final_df(pages_df[0])
fully_final_df= create_final_df(pages_df[0])
# count=0
for page_df in pages_df:
    if page_df.shape[0]==0:
        continue
    main_df=get_page_df(page_df,final_df)
    print(main_df)
    print('++++++++++')
    print(final_df)
    # print(main_df.shape)
    fully_final_df=pd.concat([fully_final_df,main_df], ignore_index=True)
    # print(final_df)
    # print('-----')
    fully_final_df.to_csv('fully_final.csv', index=False)
    # print(final_df.sample(10))
    # count+=1
    # if count==70:
    #     break
print(fully_final_df.shape)
# final_df.to_csv('fully_final.csv')

    





