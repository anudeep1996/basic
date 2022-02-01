
source_file_list=['a','b','c','d']
processed_file_list=[]

try:
    processed_file_creation=open('processedlistfile.txt', 'x')
    processed_file_creation.close()
except:
    print('file already exists')


with open('processedlistfile.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        # add item to the list
        processed_file_list.append(currentPlace)

print(processed_file_list)
to_be_processes_list=list(set(source_file_list)-set(processed_file_list))

print(to_be_processes_list)

for i in to_be_processes_list:
    # process complete

    processed_file_list.append(i)

    # with open('process_list.txt', 'w') as f:
    #     f.write(str(processed_file_list))

    with open('processedlistfile.txt', 'w') as filehandle:
        for listitem in processed_file_list:
            filehandle.write('%s\n' % listitem)