import pandas as pd
from matplotlib.figure import Figure
import random
col_list = ['member_id',"loan_amnt","funded_amnt","funded_amnt_inv","term","int_rate","installment","grade","sub_grade","job_title","emp_length","home_ownership","annual_income","verification_status","loan approved","loan purpose","zip_code","addr_state","dti","delinq_2yrs","inq_last_6mths","revol_bal","out_prncp","application_type","tot_cur_bal","total_bal_il","total_rev_hi_lim"]
test = pd.read_csv("./data/Training_dataset_org.csv",sep=",",usecols=col_list)
mod_test = pd.read_csv("./data/Training_dataset_mod2.csv",sep=",",usecols=col_list)

#assigning numerical variables to the numerical descriptions
test.verification_status = test.verification_status.replace({"Verified": 1, "Source Verified" : 2, "Not Verified": 3})
mod_test.verification_status = mod_test.verification_status.replace({"Verified": 1, "Source Verified" : 2, "Not Verified": 3})
#transforming non-numerical variables to numerical variables
#example Label encoder does
# le.transform(["tokyo", "tokyo", "paris"])
# array([2, 2, 1]...)
# from sklearn.preprocessing import LabelEncoder
test["emp_length"].replace({"10+ years": 10, "8 years": 8,"2 years":2, "3 years":3,"1 year":1,"9 years":9,"4 years":4,
                        "6 years":6,"5 years":5,"< 1 year":0,"n/a":0,"7 years":7}, inplace=True)
mod_test["emp_length"].replace({"10+ years": 10, "8 years": 8,"2 years":2, "3 years":3,"1 year":1,"9 years":9,"4 years":4,
                        "6 years":6,"5 years":5,"< 1 year":0,"n/a":0,"7 years":7}, inplace=True)

def phases():
    global test
    df_numerical_mod=mod_test.iloc[:,[10,12,13]]
    df_numerical=test.iloc[:,[10,12,13]]
    df_numerical.head()

    from scipy import stats

    p_value = 0.05

    rejected = 0
    
    return_list = []
    for col in df_numerical.columns:

        test = stats.ks_2samp(df_numerical_mod[col], df_numerical[col])

        if test[1] < p_value:

            rejected += 1
            a = "Column rejected "
            a += str(col)
            return_list.append(a)
    a = "We rejected "
    a += str(rejected)
    a+= " columns in total"
    return_list.append(a)    
    return return_list

def employ():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    x, y = [], []
    # axis.plot(xs, ys)
    # for row in test:
    #     # print(row[0],row[1])
    #     x.append(row[0])
    #     y.append(row[1])
    axis.plot(x, y)
    # test["emp_length"].value_counts(normalize=True).axis.plot.bar(title="Employment Length")
    return fig
