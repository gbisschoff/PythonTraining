from pandas import read_excel
from pandas.api.types import CategoricalDtype
from datetime import datetime
from plotly import express as ex

"""
Reading data with Pandas
https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

Read data from excel.
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html

When mapping column types specify a dictionary with the column names and types:
https://pbpython.com/pandas_dtypes.html
https://www.geeksforgeeks.org/python-pandas-categoricaldtype/
"""
data = read_excel(
    io='./data/master-data.xlsx',
    sheet_name='data',
    dtype={
        'period': datetime,
        'account_id': str,
        'approved_date': datetime,
        'first_disbursement_date': datetime,
        'arrears_status': CategoricalDtype(categories=[1, 2, 3, 4, 5, 6, 7, 8], ordered=True),
        'arrears_status_description': 'category',
        'stage': CategoricalDtype(categories=[1, 2, 3], ordered=True),
        'industry': 'category',
        'deal_type_code': 'category',
        'balance': float,
        'authorised_amount': float,
        'security_value': float,
        'write_off_date': datetime
    }
)\
    .set_index(['account_id', 'period'])\
    .sort_index()


"""
Exposure over time per product
"""
result = data.groupby(['period', 'deal_type_code'])['balance'].sum()
ex.area(result.reset_index(), x='period', y='balance', color='deal_type_code').show()

ex.
"""
Stage distribution over time per product
Number of accounts &
Balance as a proportion of total
"""
result = data.groupby(['period', 'deal_type_code', 'stage'])['balance'].count().rename('count')
ex.line(result.reset_index(), x='period', y='count', color='deal_type_code', line_group='deal_type_code', line_dash='stage', height=900).show()


result = data.groupby(['period', 'deal_type_code', 'stage'])['balance'].sum()
result = (result / result.groupby(['period', 'deal_type_code']).sum())
ex.area(result.reset_index(), x='period', y='balance', color='stage', facet_row='deal_type_code', height=8*450, range_y=[0, 1]).show()



"""
Roll rate matrix
"""


def roll_rates(*segments: str, data, column: str):
    """
    Calculate the roll rate migrations
    :param data: the raw data in tidy form
    :param column: the column for which roll rates should be calculated
    :return: the roll rates in tidy form
    """
    to_column = 'to_' + column
    result = data.copy()
    result[to_column] = result.groupby('account_id')[column].shift(-1)
    result = result[[*segments, column, to_column, 'balance']].dropna()
    result = result.groupby([*segments, column, to_column])['balance'].sum()
    result = (result / result.groupby([*segments, column]).sum()).reset_index()
    return result


"""
Vanilla roll rates per arrear status and stage
"""
rr = roll_rates(data=data, column='arrears_status')
rr.pivot(index='arrears_status', columns='to_arrears_status')
ex.bar(rr, x='arrears_status', y='balance', color='to_arrears_status').show()

rr = roll_rates(data=data, column='stage')
rr.pivot(index='stage', columns='to_stage')
ex.bar(rr, x='stage', y='balance', color='to_stage').show()

roll_rates(data=data, column='stage')\
    .pivot(index='stage', columns='to_stage')


"""
Roll rates using the *args argument
Roll rates per product type
"""
rr = roll_rates('deal_type_code', data=data, column='stage')
rr.pivot_table(index=['deal_type_code', 'stage'], columns='to_stage')


"""
Roll rates using the *args argument
Roll rates per age bucket

First create a counter for each account to represent time on book (assume all accounts are from origination)
then bucket the accounts using the 'cut' function with bins for each 12 months
then use the roll_rates function and pass in the new age bucket variable
"""
from pandas import cut
data['time_on_book'] = data.groupby('account_id').cumcount() + 1
data['age_bucket'] = cut(data['time_on_book'], bins=list(range(0, 120, 12)))

rr = roll_rates('age_bucket', data=data, column='stage')
rr.pivot_table(index=['age_bucket', 'stage'], columns='to_stage')

"""
Roll rates using the *args argument
roll rates per product and age bucket
"""
rr = roll_rates('deal_type_code', 'age_bucket', data=data, column='stage')
rr.pivot_table(index=['deal_type_code', 'age_bucket', 'stage'], columns='to_stage').to_excel('./results/tm.xlsx')
