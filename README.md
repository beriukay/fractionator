# fractionator
fraction-friendly calculator

This is a python-based command line program that will take operations on 
fractions as an input and produce a fractional result. 
- Legal operators currently accepted are: +, -, \*, and /.
- All operands and operators are expected to be separated by one or more spaces.
- Mixed numbers are represented by the whole number portion followed by an
underscore and then the numerator/denominator, without spaces.
For example, three and one quarter can be represented as 3\_1/4.
- Improper fractions and whole numbers without fractions will also be accepted 
as valid inputs.
 
Example run:

? 1/2 * 3\_3/4
= 1\_7/8

? 2\_3/8 + 9/8
= 3\_1/2

? 1
= 1

? 1/0
= divide by zero error

? -1 - -1/1
= 0

? 1 + 1/-1
= 0

