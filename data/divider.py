count = 0
thefile = open('train_set_x_cleaned.csv', 'rb')
while True:
    buffer = thefile.read(8192*1024)
    if not buffer:
        break
    count += buffer.count('\n')
print count
thefile.close( )

read_x = open('train_set_x_cleaned.csv','r')
read_y = open('train_set_y.csv')
writefile_train = open('train_set_0.8','w+')
writefile_test = open('test_set_0.2','w+')
whole_file = open('dataset_labeled','w+')
write_count = 0
while write_count<0.8 * count:
    linex = read_x.readline()
    liney = read_y.readline()
    writefile_train.writelines(liney.replace('\n','').split(',')[1] + ',' + linex.split(',')[1])
    whole_file.writelines(liney.replace('\n','').split(',')[1] + ',' + linex.split(',')[1])
    write_count += 1
while write_count <=count:
    linex = read_x.readline()
    liney = read_y.readline()
    writefile_test.writelines(liney.replace('\n', '').split(',')[1] + ',' + linex.split(',')[1])
    whole_file.writelines(liney.replace('\n', '').split(',')[1] + ',' + linex.split(',')[1])
    write_count += 1
    
read_x.close()
read_y.close()
whole_file.close()
writefile_test.close()
writefile_train.close()