# Inventory Allocator
Determines the most price effective shipment for an inventory distribution.

## Requirements:
I have only tested this program with Python 3.8 on MacOS.

## Dependencies:
None

## Formal testing:
Unit tests with pre-made test cases and assertions:
  1) `python3 generate_shipment_test.py`

## Informal/quick testing:
To test with my test cases ("test_cases.txt"):  
  1) `python3 generate_shipment.py`

To create your own new test cases:  
  1) Create text file with two inputs separated by a '-'  
  2) For multiple test cases, separate each with at least one newline  
  3) Pass in location of test case file as second parameter  
  4) `python3 generate_shipment.py [TEST_CASE_LOCATION]`  

Note:  
  1) Lines in test text file must be in the format as described above, or program will skip over them.
  2) If each input (separated by '-') is in an improper format, my program will return an empty list.  
  3) All quotes must be double quotes (to be accepted by json.loads()).  
 
One line for the output, preceded by two lines for each input (for clarity purposes), will be printed to standard output (hence informal testing).
 
