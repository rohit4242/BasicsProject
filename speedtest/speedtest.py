# internat speed test with python
from speedtest import Speedtest

st=Speedtest()

print('your download speed is: ',st.download())
print('your upload speed is: ', st.upload())
