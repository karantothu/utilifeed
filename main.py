import csv
import glob
import os, errno

#creating an empty list
#searching for available number of files(no of streams) in input folder
file_list = []
for file in glob.glob("input/*.csv"):
    #add each found stream file(sample: stream_0.csv) to list
    file_list.append(file)
#Uncomment below code to view available streams from list
#print(file_list)

#Counting the number the streams
no_ofStreams = len(file_list)

#Uncomment to print count of available streams in input folder
#print('Number of streams availbale:' + str(no_ofStreams))

#the data struct layout
class stream:
    def __init__(self):
        self.time=[]
        self.flow=[]
        self.temperature=[]

    def Stime(self, time):
        self.time.append(time)
    def Sflow(self, flow):
        self.flow.append(float(flow))
    def Stemperature(self, temperature):
        self.temperature.append(float(temperature))

#initialising list to store each stream to list element in list s
s=[]
# for n number of streams create n elements in s
for f in range(len(file_list)):
    s.append(f)

#list to store headers captured from input file
fields=[]

#Opening each file to read stream data and store each list in list s
#Each Stream file data is stored in s[s1,s2,s3,....sn]
for file in file_list:
    index= file_list.index(file)
    s[index]= stream()
    with open(file, 'r') as csvfile:
        read = csv.reader(csvfile)
        fields=read.__next__()
        for lines in read:
            s[index].Stime(lines[0])
            s[index].Sflow(lines[1])
            s[index].Stemperature(lines[2])

#Counting the number of lines in input CSV file
n_rows= len(s[0].time)

#intialising data struct for stream_aggregate values
stream_agg= stream()

#coping the time stamps from input file
stream_agg.time= s[0].time

#Uncomment to print time stamps
#print(stream_agg.time)

#calculating aggregate flow from stream files
for each in range(n_rows):
    fsum=0
    for item in s:
        fsum+=s[s.index(item)].flow[each]
    stream_agg.flow.append(round(fsum,2))

#Uncomment to aggregate flow values
#print(stream_agg.flow)

#calculating the Flow-weighted temperature
for each in range(n_rows):
    fwtsum=0
    flow_sum=0
    for item in s:
        fwt = s[s.index(item)].flow[each] * s[s.index(item)].temperature[each]
        flow_sum+=s[s.index(item)].flow[each]
        fwtsum+= fwt
    final= fwtsum/flow_sum
    stream_agg.temperature.append(round(final,2))

#Uncomment to print Flow-weighted temperature values
#print(stream_agg.temperature)

#uncomment to print headers of csv file
#print(fields)

#defining output file with path
filename= 'output/stream_aggregate.csv'
#Checking if path exists or not else create the path ./input/
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

#Writing values from the list stream_agg to output file stream_aggregate.csv
with open(filename, 'w') as Ncsv:
    Writer= csv.DictWriter(Ncsv,delimiter=',', lineterminator='\n', fieldnames=fields)
    #Writer.writerow(fields)
    Writer.writeheader()
    for n in range(n_rows):
        Writer.writerow({'datetime': stream_agg.time[n],'flow':stream_agg.flow[n],'temperature': stream_agg.temperature[n]})
