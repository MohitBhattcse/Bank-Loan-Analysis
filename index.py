# Import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px 

# Bank Loan Analysis Report
Data= pd.read_excel(r'c:\Users\Mohit.Bhatt\Downloads\financial_loan.xlsx')
# Checking the data
print(Data.head())

# Checking the no of rows and columns
print(f"There are total {Data.shape[0]} rows")
print(f"There are total {Data.shape[1]} columns")

# Information about the data
print(Data.info())

# Checking for data types
print(Data.dtypes)

# Description of the data
print(Data.describe())

# Total No of Loan Applications
Total_Loan_Applications = Data['id'].count()
print("The total no of Loan Applications are:", Total_Loan_Applications)

# Now We have to find the MTD Total Funded Amount Metric
Current_Month_Latest_Date = Data['issue_date'].max() 
Current_Month=Current_Month_Latest_Date.month
Current_Year = Current_Month_Latest_Date.year
#Let's store the current month data 
Current_Month_Data = Data[(Data['issue_date'].dt.year == Current_Year) & (Data['issue_date'].dt.month == Current_Month)]
# Total Loan Application  in the Current Month
TotalApplicationincurrentmonth = Current_Month_Data['id'].count()
#Now Total Month Application in Current Month
print(f"Total Application in {Current_Month_Latest_Date.strftime('%B %Y')} : {TotalApplicationincurrentmonth}")


# Now we have to find the MTD Total Funded Amount Metric
print(f"Total Funded Amount is ${Data['loan_amount'].sum()/1000000:,.2f}M")
Current_Month_Funded_Account = Current_Month_Data['loan_amount'].sum()
print(f"The total funded amount for {Current_Month_Latest_Date.strftime('%B %Y')} is ${Current_Month_Funded_Account/1_000_000:,.2f}M")


# Now we have to find the Total Amount Received
print(f"Total Amount Received is ${Data['total_payment'].sum()/1000000:,.2f}M")
Current_Total_Amount_Account = Current_Month_Data['total_payment'].sum()
print(f"The Total Amount Received for {Current_Month_Latest_Date.strftime('%B %Y')} is ${Current_Total_Amount_Account/1_000_000:,.2f}M")

# Average Interest Rate
print(
    f"The Average Interest Rate Across All Loans "
    f"is {Data['int_rate'].mean()*100:.2f}%"
)

# Average Debt-to-Income Ratio (DTI): 
print(
    f"The Average Debt-to-Income Ratio (DTI) Across All Loans "
    f"is {Data['dti'].mean()*100:.2f}%"
)


# So now let's find the Good Loan(Status as Fully Paid or Charged ) KPI's vs Bad Loan(Status as Charged Off) KPI's
# Good Loan KPI's
Good_Loan_Data = Data[Data['loan_status'].isin(['Fully Paid', 'Current'])]
Good_Loan_Total_Application = Good_Loan_Data['id'].count()
Good_Loan_Application_Percentage = (Good_Loan_Total_Application / Total_Loan_Applications) * 100
Good_Loan_Funded_Amount = Good_Loan_Data['loan_amount'].sum()
Good_Loan_Total_Received_Amount = Good_Loan_Data['total_payment'].sum()

print(f"Total Good Loan Application is {Good_Loan_Total_Application}")
print(f"Total Good Loan Application Percentage For Total Loan Application is {Good_Loan_Application_Percentage:.2f}%")
print(f"Total Good Loan Funded Amount is {Good_Loan_Funded_Amount/1000000:.2f}M")
print(f"Total Good Loan Total Received Amount is {Good_Loan_Total_Received_Amount/1_000_000:.2f}M")

# Bad Loan KPI's
Bad_Loan_Data = Data[Data['loan_status'].isin(['Charged Off'])]
Bad_Loan_Total_Application = Bad_Loan_Data['id'].count()
Bad_Loan_Application_Percentage = (Bad_Loan_Total_Application / Total_Loan_Applications) * 100
Bad_Loan_Funded_Amount = Bad_Loan_Data['loan_amount'].sum()
Bad_Loan_Total_Received_Amount = Bad_Loan_Data['total_payment'].sum()

print(f"Total Bad Loan Application is {Bad_Loan_Total_Application}")
print(f"Total Bad Loan Application Percentage For Total Loan Application is {Bad_Loan_Application_Percentage:.2f}%")
print(f"Total Bad Loan Funded Amount is {Bad_Loan_Funded_Amount/1000000:.2f}M")
print(f"Total Bad Loan Total Received Amount is {Bad_Loan_Total_Received_Amount/1_000_000:.2f}M")

# Now let's calculate some metrics to plot the graph for better analysis 
# Monthly Trends by Issue Date Total Funded Amount
Monthly_Funded = Data.sort_values('issue_date').assign(month_name=lambda x:x['issue_date'].dt.strftime('%b %Y')).groupby('month_name', sort=False)['loan_amount'].sum().div(1000000).reset_index(name='Total_Loan_Amount')   
plt.figure(figsize=(10,5))
plt.fill_between(Monthly_Funded['month_name'], Monthly_Funded['Total_Loan_Amount'], color='skyblue', alpha=0.4)
plt.plot(Monthly_Funded['month_name'],Monthly_Funded['Total_Loan_Amount'],color='blue',linewidth=2)
for i, row in Monthly_Funded.iterrows():
    plt.text(i,row['Total_Loan_Amount']+0.1,f"{row['Total_Loan_Amount']:.2f}",ha='center', va='bottom', fontsize=9,rotation=0,color='black')
plt.title('Total Funded Amount by Month', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Funded Amount ($ Millions)', fontsize=12)
plt.xticks(ticks=range(len(Monthly_Funded)), labels=Monthly_Funded['month_name'], rotation=45)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# Monthly Trends by Issue Date Total Received Amount 
Monthly_Received = Data.sort_values('issue_date').assign(month_name=lambda x:x['issue_date'].dt.strftime('%b %Y')).groupby('month_name', sort=False)['total_payment'].sum().div(1000000).reset_index(name='Total_Received_Amount')   
plt.figure(figsize=(10,5))
plt.fill_between(Monthly_Received['month_name'], Monthly_Received['Total_Received_Amount'], color='lightgreen', alpha=0.4)
plt.plot(Monthly_Received['month_name'],Monthly_Received['Total_Received_Amount'],color='green',linewidth=2)
for i, row in Monthly_Received.iterrows():
    plt.text(i,row['Total_Received_Amount']+0.1,f"{row['Total_Received_Amount']:.2f}",ha='center', va='bottom', fontsize=9,rotation=0,color='black')
plt.title('Total Received Amount by Month', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Received Amount ($ Millions)', fontsize=12)
plt.xticks(ticks=range(len(Monthly_Received)), labels=Monthly_Received['month_name'], rotation=45)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# Monthly Trends by Issue Date Total Loan Application
Monthly_Applications = Data.sort_values('issue_date').assign(month_name=lambda x:x['issue_date'].dt.strftime('%b %Y')).groupby('month_name', sort=False)['id'].count().reset_index(name='Total_Applications')
plt.figure(figsize=(10,5))
plt.fill_between(Monthly_Applications['month_name'], Monthly_Applications['Total_Applications'], color='orange', alpha=0.4)
plt.plot(Monthly_Applications['month_name'],Monthly_Applications['Total_Applications'],color='darkorange',linewidth=2)
for i, row in Monthly_Applications.iterrows():
    plt.text(i,row['Total_Applications']+0.1,f"{row['Total_Applications']:.2f}",ha='center', va='bottom', fontsize=9,rotation=0,color='black')
plt.title('Total Loan Applications by Month', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Loan Applications', fontsize=12)
plt.xticks(ticks=range(len(Monthly_Applications)), labels=Monthly_Applications['month_name'], rotation=45)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show() 


# -------------
# Regional Analysis by Total Funded Amount
state_funding = Data.groupby('address_state' ) ['loan_amount' ].sum(). sort_values(ascending=True)
state_funding_thousands = state_funding / 1000

plt.figure(figsize=(10, 8))
bars = plt.barh(state_funding_thousands. index, state_funding_thousands. values, color='lightcoral' )

for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height() / 2,
             f'{width:,.0f}', va='center', fontsize=9)

plt.title('Total Funded Amount by State ($)')
plt.xlabel('Funded Amount ($\'000)')
plt.ylabel('State')
plt.tight_layout ()
plt.show()

# Regional Analysis by Total Received Amount 
state_received = Data.groupby('address_state' ) ['total_payment' ].sum().sort_values(ascending=True)    
state_received_thousands = state_received/ 1000

plt.figure(figsize=(10, 8))
bars = plt.barh(state_received_thousands. index, state_received_thousands. values, color='lightgreen' )

for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height() / 2,
             f'{width:,.0f}', va='center', fontsize=9)

plt.title('Total Received Amount by State ($)')
plt.xlabel('Received Amount ($\'000)')
plt.ylabel('State')
plt.tight_layout ()
plt.show()

# Regional Analysis by Total Loan Application
state_applications = Data.groupby('address_state')['id'].count().sort_values(ascending=True)

plt.figure(figsize=(10, 8))
bars = plt.barh(state_applications. index, state_applications. values, color='skyblue')


for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.3,
        bar.get_y() + bar.get_height() / 2,
        f'{width:,.0f}',
        va='center',
        fontsize=9
    )


plt.title('Total Loan Applications by State)')
plt.xlabel('Total Applications')
plt.ylabel('State')
plt.tight_layout ()
plt.show()

# ----------
# Loan Term Analysis by Total Funded Amount
term_funding_millions = (
    Data.groupby('term')['loan_amount']
    .sum() / 1_000_000
)

plt.figure(figsize=(5, 5))

plt.pie(
    term_funding_millions.values,
    labels=term_funding_millions.index,
    autopct=lambda p: f"{p:.1f}%\n${p*term_funding_millions.sum()/100:.1f}M",
    startangle=90,
    wedgeprops={'width': 0.4}
)

# Donut hole
plt.gca().add_artist(plt.Circle((0, 0), 0.6, color='white'))

plt.title("Total Funded Amount by Term (in $ Millions)")
plt.show()


# Loan Term Analysis by Total Received Amount
term_payment_received_millions = (
    Data.groupby('term')['total_payment']
    .sum() / 1_000_000
)

plt.figure(figsize=(5, 5))

plt.pie(
    term_payment_received_millions.values,
    labels=term_payment_received_millions.index,
    autopct=lambda p: f"{p:.1f}%\n${p*term_payment_received_millions.sum()/100:.1f}M",
    startangle=90,
    wedgeprops={'width': 0.4}
)

# Donut hole
plt.gca().add_artist(plt.Circle((0, 0), 0.6, color='skyblue'))

plt.title("Total Received Amount by Term (in $ Millions)")
plt.show()

# Loan Term Analysis by Total Loan Application
term_applications = Data.groupby('term')['id'].count()
plt.figure(figsize=(5, 5))
plt.pie(
    term_applications.values,
    labels=term_applications.index,
    autopct=lambda p: f"{p:.1f}%\n{int(p*term_applications.sum()/100)}",
    startangle=90,
    wedgeprops={'width': 0.4}
)
plt.title("Total Loan Applications by Term")
plt.show()


# Employee Length by Total Funded Amount (in Thousands)
emp_funding = (
    Data.groupby('emp_length')['loan_amount']
    .sum()
    .sort_values()
    / 1000
)

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_funding.index, emp_funding.values, color='purple')

plt.xlim(0, emp_funding.max() * 1.15)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 5,
        bar.get_y() + bar.get_height() / 2,
        f"${width:,.0f}K",
        va='center',
        fontsize=9
    )

plt.xlabel("Funded Amount ($ Thousands)")
plt.title("Total Funded Amount by Employment Length")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Employee Length by Total Received Amount (in Thousands)
emp_received = (
    Data.groupby('emp_length')['total_payment']
    .sum()
    .sort_values()
    / 1000
)

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_received.index, emp_received.values, color='teal')

plt.xlim(0, emp_received.max() * 1.15)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 5,
        bar.get_y() + bar.get_height() / 2,
        f"${width:,.0f}K",
        va='center',
        fontsize=9
    )

plt.xlabel("Received Amount ($ Thousands)")
plt.title("Total Received Amount by Employment Length")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Employee Length by Total Applications
emp_applications = (
    Data.groupby('emp_length')['id']
    .count()
    .sort_values()
)

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_applications.index, emp_applications.values, color='orange')

plt.xlim(0, emp_applications.max() * 1.15)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 5,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width):,}",
        va='center',
        fontsize=9
    )

plt.xlabel("Number of Applications")
plt.title("Total Loan Applications by Employment Length")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


purpose_funding_millions = (
    Data.groupby('purpose')['loan_amount']
    .sum()
    .sort_values()
    / 1_000_000
)

plt.figure(figsize=(10, 6))
bars = plt.barh(
    purpose_funding_millions.index,
    purpose_funding_millions.values,
    color='skyblue'
)

plt.xlim(0, purpose_funding_millions.max() * 1.15)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.1,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.2f}M",
        va='center',
        fontsize=9
    )

plt.title('Total Funded Amount by Loan Purpose (₹ Millions)', fontsize=14)
plt.xlabel('Funded Amount (₹ Millions)')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


purpose_received_millions = (
    Data.groupby('purpose')['total_payment']
    .sum()
    .sort_values()
    / 1_000_000
)

plt.figure(figsize=(10, 6))
bars = plt.barh(
    purpose_received_millions.index,
    purpose_received_millions.values,
    color='seagreen'
)

plt.xlim(0, purpose_received_millions.max() * 1.15)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.1,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.2f}M",
        va='center',
        fontsize=9
    )

plt.title('Total Received Amount by Loan Purpose (₹ Millions)', fontsize=14)
plt.xlabel('Received Amount (₹ Millions)')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


purpose_applications = (
    Data.groupby('purpose')['id']
    .count()
    .sort_values()
)

plt.figure(figsize=(10, 6))
bars = plt.barh(
    purpose_applications.index,
    purpose_applications.values,
    color='mediumpurple'
)

plt.xlim(0, purpose_applications.max() * 1.15)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 10,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width):,}",
        va='center',
        fontsize=9
    )

plt.title('Total Loan Applications by Loan Purpose', fontsize=14)
plt.xlabel('Number of Applications')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


import plotly.express as px

home_funding = (
    Data.groupby('home_ownership')['loan_amount']
    .sum()
    .reset_index()
)

home_funding['loan_amount_millions'] = home_funding['loan_amount'] / 1_000_000

fig = px.treemap(
    home_funding,
    path=['home_ownership'],
    values='loan_amount_millions',
    color='loan_amount_millions',
    color_continuous_scale='Blues',
    title='Total Funded Amount by Home Ownership (₹ Millions)'
)

fig.show()

home_received = (
    Data.groupby('home_ownership')['total_payment']
    .sum()
    .reset_index()
)

home_received['received_amount_millions'] = home_received['total_payment'] / 1_000_000

fig = px.treemap(
    home_received,
    path=['home_ownership'],
    values='received_amount_millions',
    color='received_amount_millions',
    color_continuous_scale='Greens',
    title='Total Received Amount by Home Ownership (₹ Millions)'
)

fig.show()

home_applications = (
    Data.groupby('home_ownership')['id']
    .count()
    .reset_index(name='total_applications')
)

fig = px.treemap(
    home_applications,
    path=['home_ownership'],
    values='total_applications',
    color='total_applications',
    color_continuous_scale='Purples',
    title='Total Loan Applications by Home Ownership'
)

fig.show()
