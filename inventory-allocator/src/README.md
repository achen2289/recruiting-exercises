# Inventory Allocator
Determines the most price effective shipment for an inventory distribution.

## Requirements:
I have only tested this program with Python 3.8 on MacOS.

## Dependencies:
None

## Formal testing:
Unit tests with pre-made test cases and assertions:
  1) `python3 generate_shipment_test.py`

## Edge case handling:  
  1) Duplicate warehouses will return an empty list.
  2) Quantity values of negative or zero value will be ignored.
  3) Input of the correct type but lacking certain parameters (such as "name") will result in an empty list.
  4) Empty inputs will result in an empty list.

## Informal testing:
To test with my test cases ("test_cases.txt"):  
  1) `python3 generate_shipment.py`

To create your own new test cases:  
  1) Create text file with two inputs separated by a '-'  
  2) For multiple test cases, separate each with at least one newline  
  3) Pass in location of test case file as second parameter  
  4) `python3 generate_shipment.py [TEST_CASE_LOCATION]`  

Note:  
  1) All quotes in test text file must be double quotes.  
  2) If each input is in an improper format, the program will return an empty list.  
 
One line for the output, preceded by two lines for each input (for clarity purposes), will be printed to standard output (hence informal testing).
 
