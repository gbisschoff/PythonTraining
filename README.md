# Python Training
This document gives a quick start guide to python. This training is by no means
complete and I would need weeks to teach you everything you need to know to be 
sufficiently experienced in Python, but hopefully by the end of this you will 
have the confidence to start playing around and start down your own journey. 

In this training we will look at:

1. How to install Python and PyCharm.
2. How to setup Python and do a basic hello-world program.
3. What are the basic data types in Python.
4. How to install and import modules.
5. How to work with data.
6. Some useful links that you can use to start down your Python journey.

## 1. Installing Python and PyCharm

- Download and install [Python3]
- Download and install the community edition of [PyCharm]. PyCharm is a popular
  text editor used for Python.

## 2. Setup and Hello World

- Open PyCharm and configure. 
- Select **New Project**
    - give your project a name (`hello-world`)
    - drop down the **Project Interpreter**, select **New environment using** 
      `Virtualenv` and ensure the **Base interpreter** is set to `Python 3`
    - Click **Create**
- In the **hello-world** folder,
    - right click **new**,
    - select **Python File**,
    - give it a name `main`.
- You now have a new Python script where you are ready to code. Type the 
  following piece of code:

```python
print('hello world')
```

- at the top click **Run**, then select **Run**, it will ask you what you would
  like to run, select `main`. It should now run the scrip and print `hello-world`
  in the console below.
- You have written your first Python program.

## 3. Variables and Data types

- Boolean: `True`, `False`
- Numeric: `int`, `float`, `complex`
- Sequence: `list`, `tuple`, `range`
- Strings: `str`
- Mapping Types: `dict`

For more information see the [Python Docs].

### 3.1 Basic data types
Here are examples of creating basic variables that can be use in more 
complicated programs.

```python
bool: bool = True
integer: int = 1
floating_point: float = 2.0
string: str = "My String"

my_tuple: tuple = (1, 2, 3)
print(my_tuple[0])  # index starts at 0
print(my_tuple[1])
print(my_tuple[2])


my_list: list = [1, 2, 3]
print(my_list[0])  # index starts at 0
print(my_list[1])
print(my_list[2])

my_range_0_9: range = range(10)  # 0-9, 10 is excluded
my_range_5_9: range = range(5, 10)  # 5-9, 10 is excluded

my_dictionary: dict = {'name': "Geyer", 'age': 28}
print(f"Name: {my_dictionary['name']}")
print(f"Age: {my_dictionary['age']}")
```

### 3.2 Strings:
Strings are one of the most commonly used data types. Strings have a set of 
methods that are accessed by the `.` opperator, whith these methods you can
perform functions on the string, e.g. `.upper()`.

You can also loop access individual characters of the string by index using
the `[]` opperator and the index of the character. 

*Note: Python indexes start at 0*

```python
phase: str = "Python is Fun"
print(phase.upper())
print(phase.lower())

print(phase.isupper())
print(phase.upper().isupper())

print(len(phase))
print(phase[0])
print(phase[1])

for character in phase:
    print(character.upper())

```

### 3.4 Numbers:
Numbers are another common data type used in programming you can perform all the
basic arithmatic on numbers. There are also many functions that you can apply on
numbers. These functions can be imported form the `math` library.

```python
print(4 * -3 + 5 / 2)  # +, -, *, /, **
print((4 * -3) + (5 / 2))
print(10 % 3)  # modulus gives remainder
print(10 // 3)  # integer division
print(abs(-5))
print(max(1, 2, 3, 4))  # max, min
print(round(3.5))

# There are many more math functions in the math library
from math import sin, cos, tan, sqrt
```


### 3.5 Lists:
List in Python a form of data structure commonly used to store and keep track of
multiple objects of the same type, e.g. a list of number or names. The list 
provides the extra functionallity of accessing the list of elements by index.

List are a mutable data type. That means that the list can be edited after it
has been created. List also have a set of methods that allow you to operate on
the list, e.g. `.append("Jason")` adds the name `Jason` to the names list.

```python
numbers = [1, 2, 3 , 4, 5]
names = ["Kevin", "Karin", "Jim", "Oscar", "Toby"]
print(names)
print(names[0])
print(names[1])
print(names[-1])
print(names[1:3])  # from 1 to 3, excluding 3
print(names[1:])  # from 1 onward
names[1] = "Mike"
print(names)

print(names.extend(numbers))
print(names.append("Jason"))
print(names.insert(1, "Kelly"))
print(names.remove("Jim"))
print(names.clear())
print(names.pop())  # remove last element
print(names.count("Jim"))
print(names.sort())
print(names.reverse())
print("Mike" in names)

copy_names = names.copy()
print(copy_names)
```

### 3.6 Tuples:
Tupels are like lists, but is an immutable data type. This means that the tuple
cannot be edited after it has been created. This is mainly used when creating 
sets of read only data, e.g. a set of coordinates or a set of file paths.

Tuples are created with the `()` brackets and their elements can be accessed,
similar to lists, by index. These data types can be combined to to create a 
list of tuples, i.e. a list of read only objects. 

```python
coordinates = (4, 5)
coordinates[1] = 2  # will give an error
print(coordinates[0])

#create a list of tuples
coordinates = [(4, 5), (4, 5), (4, 5)]
```

### 3.7 Functions:
Functions are very powerful tools that can simplify code as well as increase
code reuse. A function is defined using the `def` keyword followed by the
function name and a set of `()` parenthesis and a `:`. Within the set of `()`
any number of arguments can be passed for the function to use. These arguments
can then be referenced by name from within the funtion.

To use the function the function should be *called* with the arguments it
requires. The result of the function can be stored in a variable for latter 
use in other parts of the code. There are some advanced functionallity that
could be used in your functions that we could look at a bit later.

*Note: Indentation matters*

```python
def percentage_diff(number_1, number_2):
    result = (number_1 - number_2) / number_2
    return result

print(percentage_diff(3, 2))
```

## 4. Installing and Importing modules
The power of open source does not come from the cost of the software, but the
access to other peoples functions and code. Other peoples code (or your own)
can be imported into your project for you to use. In the example below I 
created a file named `useful_tools.py` in this file I defined two functions:
`roll_dice` and `file_extension`. I then imported these two functions into my
application by using the `from` and `import` statements. I can then use these
functions in the remainder of my program without having to rewrite or copy the
code of the functions into my application.

```python
from useful_tools import roll_dice, file_extension
roll_dice(6)
file_extension("master_data.csv")
```

Similar to importing from your own files you can also import from a long list of
standards libraries in Python or install libraries of other people and use their
libraries in your code. You can get a long list of availible libraries in the 
[Python Docs]. If it does not contain the functionallity you want you can just 
Google for a library that does have the functionallity you want, install it and 
use it. We already looked at an example of importing the `math` library

```python
from math import sin, cos, tan, sqrt
```

For us to install libraries that do not form part of the standard library we
will have to use a program called `pip`. `pip` comes pre-installed with Python3.
To use `pip` we need to change to the `Terminal` tab (bottom left) of PyCharm. 
You should see something like this:

```terminal
Microsoft Windows [Version 10.0.16299.1268]
(c) 2017 Microsoft Corporation. All rights reserved.

(venv) C:\Users\gbisschoff\PycharmProjects\hello-world>
```

This shows you the directory of your project and that you are using a virtual
environment (`venv`). This terminal can also be accessed from Windows command
prompt. We are going to install the [Pandas] and [Plotly] libraries. 
[Pandas] is a powerful data analysis library, and [Plotly] is a library used to 
create interactive plot. To install these libraries run the following command in
the terminal:

```terminal
pip install pandas plotly xlrd
```

To use the functionallity in these libraries we need to import the components
that we need. Here you can see an example where I import functionallity and 
rename it so that it is easier to reference. This is also useful when you have 
multiple tools with the same name.

```python
from pandas import read_excel
from pandas.api.types import CategoricalDtype
from datetime import datetime
from plotly import express as ex
```

## 5. Data analysis
In this section we will see how we can read in some data and create some basic
analytical insights using Pandas and Plotly.

### 5.1 Importing data

In this section we will look at importing data. I will read in Excel data, but 
Pandas supports reading in multiple file formats incuding SAS ([Pandas IO]). 
When reading in data it is always important to reference the documentation to 
ensure you pass the correct arguments to the function. 

```python
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
```

In the code block above we see that I specify the path to the file with the `io`
argument and the sheet name with the `sheet_name` argument. I then specify a 
dictionary with the column names and their  types, it is useful to map columns
to specific types to ensure that the format of the fields are correct. For the 
`arrears_status` and `stage` columns a create a `CategoricalDtype` object, 
specifying the valid categories, this will then automatically filter out all of 
the invalid types. 

*Note: Category types are used to speed up programs and use less RAM*

I then set the index of the table to be the `account_id` and `period` columns
and then sort by them. This ensures that there is only a single account per
period.

### 5.2 Basic data analysis

After reading in the data the next step would be to do some basic data analysis.
In this section we will create a basic 'Exposure over time' plot per product. 
In Excel, you would create a pivot table that you group by product and period 
and then sum the balance column. In Pandas, the proces is very similar:

```python
result = data.groupby(['period', 'deal_type_code'])['balance'].sum()
```

To create an area plot of this we need to reset the index using `reset_index()`.
After grouping a dataframe the groups are set as part of the index. After we 
have created our summary we need to *ungroup* the result to map the groups
back to columns, so that we can specific them in the plotting function. We use
the `.show()` method to show the plot after creating it. 

```python
ex.area(result.reset_index(), x='period', y='balance', color='deal_type_code').show()
```

### 5.3 Advanced data analysis

In this section we will look at a bit more advanced data analysis. 
We will create the stage distibution per product over time. To do this in Excel 
you would have to create two pivot tables, join them with a `vlookup` then creat
a variable called `proportion` defined as the total divided by the group total. 

In Python, we will go though the same process. Create a dataset grouped by 
`period`, `deal_type_code` and `stage` then sum up the `balance` column. Create 
another dataset the is grouped by `period` and `deal_type_code` and then sum up 
the `balance` column. We will then join the two columns and divide the two 
columns. In Python joining two indexed `Series` objects are done automatically
for you. You can do more complicated joins using the `.join` method of the 
`DataFrame` object. 

```python
result = data.groupby(['period', 'deal_type_code', 'stage'])['balance'].sum()
result = (result / result.groupby(['period', 'deal_type_code']).sum())
```

To create a seperate plot for each product use the `facet_row` argument and set
the range of the `y` axis to be `[0, 1]`. 

```
ex.area(
    result.reset_index(),
    x='period',
    y='balance',
    color='stage',
    facet_row='deal_type_code',
    height=8*450,
    range_y=[0, 1]\
).show()
```

### 5.5 Putting it all together
In this section we will combine the above lessons to create a dynamic function 
that can create roll rates for different columns and segmentation in the data. 
This function can then be used to look at stage migrations as well as arrear 
status migrations for various segments of the data. 

#### 5.5.1 Defining the function
We define a function below that takes multiple positional arguments `*segments`,
these can be of any type, we will use this to represent the columns to segment 
by. The `data` argument represents the account level data and the `column` 
argument represents the column that the roll will be calculated for. 

We then create a variable `to_column` that will represent the column that 
contains the lead of the `column` argument. We create a copy of the data and 
then create the lead column of per account.

We then select the columns that we require for the calculation and drop all `na`
values that we created when we calculated the lead of the `column` variable.

We then group by the `*segments`, the `column` and the `to_column` and sum up 
the balance. We repeat the exercise but this not group by the `to_column` to 
calcute the denominator. 

Finally we calculate the roll proportion and reset the index.

```python
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
```

#### 5.5.2 Vanilla use of the function
We can now use the function to calculate the roll rates for either the 
`arrears_status` or `stage` column to calculate the roll rate matrix.

```python
rr = roll_rates(data=data, column='arrears_status')
rr.pivot(index='arrears_status', columns='to_arrears_status')
ex.bar(rr, x='arrears_status', y='balance', color='to_arrears_status').show()

rr = roll_rates(data=data, column='stage')
rr.pivot(index='stage', columns='to_stage')
ex.bar(rr, x='stage', y='balance', color='to_stage').show()

roll_rates(data=data, column='stage')\
    .pivot(index='stage', columns='to_stage')
```

#### 5.5.3 Roll rates with single segmentation
To use the `*segments` argument we can just pass the colum we want to segment 
by. In the example below we are going to segment by product (`deal_type_code`).
This gives us the roll rate matrix per product. 

```python
rr = roll_rates('deal_type_code', data=data, column='stage')
rr.pivot_table(index=['deal_type_code', 'stage'], columns='to_stage')
```

We can also create new columns and pass those columns to segment by. 
In the example below we are going to first create a variable called 
`time_on_book`, then we are going to bucket this variable into age 
groups (`age_bucket`) of one year using the `cut` function from `pandas`.
 Finally we calculate the roll rates for each `age_bucket`.

```python
from pandas import cut
data['time_on_book'] = data.groupby('account_id').cumcount() + 1
data['age_bucket'] = cut(data['time_on_book'], bins=list(range(0, 120, 12)))

rr = roll_rates('age_bucket', data=data, column='stage')
rr.pivot_table(index=['age_bucket', 'stage'], columns='to_stage')

```

#### 5.5.4 Roll rates with multiple segmentation
The `*segments` variable can also take multiple columns to segment by. In the 
example below we will re-use the `age_bucket` variable we defined in the 
previous section and then also segment by product. This then gives us the roll 
rates per product and age bucket.

```python
rr = roll_rates('deal_type_code', 'age_bucket', data=data, column='stage')
rr.pivot_table(index=['deal_type_code', 'age_bucket', 'stage'], columns='to_stage')
```
## 6. Conclusion
In this training I showed you how to install Python and PyCharm,
What the IDE looks like and how to create a basic hello-world program,
What the basic data types are and how to use them,
How to install and import modules and putting it all together in how to 
do some basic data analysis and write funtions. I hope you found this training
useful and that you continue down your Python journey.

## 7. Links
This section contains some useful links that you could use to continue down your
Python journey. It contains some useful guides, videos and books that are all 
free to access and use. 

### 7.1 Software
- [Python3]
- [PyCharm]

### 7.2 Guides
- [Python Docs]
- [Math Library]

### 7.3 Books
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
- [Fluent Python](https://b-ok.cc/book/2575636/8f8e85)
- [Python for Data Analysis](https://b-ok.cc/book/3367370/62327b)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/index.html)

### 7.4 Videos
- [Learn Python - Full Cource for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw)
- [Beginning Python](https://drive.google.com/folderview?id=1KnfTxxCDurkm1vOty5tBuiNSZAi30014)
- [Python Design Pattern](https://drive.google.com/folderview?id=1qQF3oqKXsRnYoLwxu2qRKICWF2JlGCAn)
- [Mastering Python](https://drive.google.com/folderview?id=15lQClcQA2rHOpyo5mMFcigAvT7ucIzsW)
- [Python web Penetrations testing](https://drive.google.com/folderview?id=1ye6US-1ki9YjZYRqYQyFFJanlrdqrqrj)
- [Python machine learning project](https://drive.google.com/folderview?id=1TH7UCmFv4Y7HdAao0JquVMUKxl8Q7XHh)
- [Deep learning with python](https://drive.google.com/folderview?id=1ORyySQmRn9GRtvvxNNQyABBG9Dcs18gD)

[Python3]: https://www.python.org/downloads/
[PyCharm]: https://www.jetbrains.com/pycharm/download/
[Python Docs]: https://docs.python.org/3/library/index.html
[Math Library]: https://docs.python.org/3/library/math.html?highlight=math#module-math
[Pandas]: https://pandas.pydata.org/
[Plotly]: https://plot.ly/python/
[Pandas IO]: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

