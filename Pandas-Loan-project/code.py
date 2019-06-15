# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)




# code starts here






# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],1)
banks.isnull().sum()
bank_mode = bank.mode().iloc[0]
banks.fillna(bank_mode, inplace = True)
banks.isnull().sum()
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],
values='LoanAmount',aggfunc='mean')



# code ends here



# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed']=='Yes')&(banks['Loan_Status']=='Y')])
print(loan_approved_se)
loan_approved_nse = len(banks[(banks['Self_Employed']=='No')&(banks['Loan_Status']=='Y')])
print(loan_approved_nse)
percentage_se = (loan_approved_se/614)*100
print(percentage_se)
percentage_nse = (loan_approved_nse/614)*100
print(percentage_nse)
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
#print (loan_term)
big_loan_term = 0
for i in loan_term:
    if i >= 25:
        big_loan_term += 1

print(big_loan_term)


# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby(['Loan_Status'])
mean_values = loan_groupby['ApplicantIncome', 'Credit_History'].agg(np.mean)




#code ends here


