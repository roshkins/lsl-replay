import pylsl
import pandas as pd
import time
from sys import argv

if __name__ == '__main__':
    sample_rate = 220 if len(argv) <= 2 else int(argv[2]) # times a second
    static_data = pd.read_csv(argv[1])
    static_data_column_count = len(static_data.columns)
    print(static_data)
    static_stream_info = pylsl.StreamInfo(name='static-lsl',
    nominal_srate=sample_rate, channel_count=static_data_column_count, type='EEG')
    static_stream = pylsl.StreamOutlet(static_stream_info)
    index = 0
    while index < len(static_data):
        values = static_data.loc[[index]].values
        print(values)
        static_stream.push_sample(values[0])
        index += 1
        time.sleep(1/sample_rate)
