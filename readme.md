# Introduction
* This program is developed by Vinod(email:vinod.karantothu@live.in) as a code assignment from Utilifeed AB.
* This program is written from the Scratch( From Go program --> to Python program).
* Some new features are added to this python program that are not there in Go version.

# The Program
* The program reads timeseries data generated from meters attached to fluid streams (for example pipes with hot water running through them) and calculates their _aggregate stream_, 
*   Assuming the streams are hot water running through separate pipes, this represents the stream that would result if joined the pipes to a single large pipe so all the water mixed.
*   The streams individually are defined by temperature and flow. For the aggregate stream you need to calculate the aggregated flow and flow-weighted temperature.

# New Features (included in this python version program)
* Improved program functionality:
*   It reads any number of files "stream*.csv" (* matches any string) from the input directory.
*   It reads the headers from the input files and write the same headers to the output csv "stream_aggregate.csv" 
*   The program is testable and easier to expand in the future.
*   The data struct layout, variable names, formatting etc are well defined to improve readability and maintainability
*   In-code documentation is done to improve readability and maintainability
*   Program reads all .csv files from ./input, calculate the aggregate stream and save it to ./output/stream_aggregate.csv.

#Requirements and Usage 
* It is develeoped and tested on the python version= '3.7.3'
* Place the required CSV files in the input directory to output their respective aggregate values in csv file in the output directory. 
* To excute the program open command terminal in program directory and type 'python main.py' or 'python3 main.py'
* A CSV file will created in the ouput directory with filename 'stream_aggregate.csv'   

# Test Cases:
* Test Case 1: Check results with 2 stream files in input directory 
* Test Case 2: Check results with n stream files in input directory
* Test Case 3: Delete the stream_aggregare.csv in output directory and run program, check if stream_aggregare.csv is generated.
* Test Case 4: Update stream files in input directory and run program, check if values are updated in stream_aggregare.csv  
* Test Case 5: check if the headers in stream_aggregare.csv are same from input stream files.


## Mathematical definitions
* Flow-weighted temperature is a weighted average temperature, where the impact of each stream on the "average" is proportional to the streams flow at that time.
* The values in the aggregate stream is calculated independently for each timestamp
Stream i has, at each timestamp t, a flow `f_i(t)` and a temperature `T_i(t)`
Aggregated flow (`f`) is calculated as a simple sum each hour. For `n` streams:
    `f(t) = (f_0(t) + f_1(t) + ... + f_n(t) )`
Flow-weighted temperature `T_fw(t)` is calculated as:
    `T_fw(t) = (T_0(t)*f_0(t) + T_1(t)*f_1(t) + ... + T_n(t)*f_n(t)) / (f_0(t) + f_1(t) + ... + f_n(t)) = (T_0(t)*f_0(t) + T_1(t)*f_1(t) + ... + T_n(t)*f_n(t)) / f(t)`


##  This Code assignment is delivrable to:
Jens Carlsson, Utilifeed AB
email:jens@utilifeed.com
