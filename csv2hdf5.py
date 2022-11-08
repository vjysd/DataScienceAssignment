import h5py
import numpy as np
import pandas as pd

# Read the CSV data and xml metadata
frame = pd.read_csv('data.csv')
xmlfh = open('metadata.xml', 'rb')

# Change the data columns that have datatype Object to String for easy conversion to hdf5
for typ, names in zip(frame.dtypes, frame.columns):
    print(typ, names)
    if typ == 'object':
        frame[names] = frame[names].astype('|S')

# Create an hdf5 file if doesn't exist
f = h5py.File('data.hdf5','a')

# create dataset array and add to hdf5
f['data_array'] = frame.to_records(index=False)
f.attrs['xml'] = xmlfh.read()

# close connection to file
f.close()