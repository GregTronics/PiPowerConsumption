import time

import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()

GAIN = 1

logName = raw_input('Please enter a filename to log the data to: ')
logName = logName + '.txt'
sampleRate = raw_input('Please enter the sample rate (in milliseconds, 10 minimum): ')
fout = open(logName, 'w')
print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
# Main loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
        # Note you can also pass in an optional data_rate parameter that controls
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.
        #values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)
        # Each value will be a 12 or 16 bit signed integer value depending on the
        # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
    # Print the ADC values.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    
    fout.write(str(time.time()) + ',' + str(values[0]) + ',' + str(values[1]) + ',' + str(values[2]) + ',' + str(values[3]))
    fout.write('\n')
    
    # Pause for half a second.
    if(sampleRate > 10)
        time.sleep(sampleRate/100)

fout.close()
