# internat speed test with python
import speedtest
s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
res = s.results.dict()
print(res["download"], res["upload"], res["ping"])
