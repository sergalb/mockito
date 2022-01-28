import os
import time
import statistics


def measureDockerRun(imageNumber):
    start = time.time()
    os.system("docker run  --rm " +
              "-v $(pwd):/data/project " +
              "-v $(pwd)/out:/data/results " +
              "-p 10001:10001 repo.labs.intellij.net/static-analyser/qodana:" + imageNumber
              )
    end = time.time()
    return end - start


def measureGc(gc):
    os.system("docker pull repo.labs.intellij.net/static-analyser/qodana:" + gc)
    times = []

    for i in range(15):

        times.append(measureDockerRun(gc))
    return times


parallelResults = measureGc("20868.2523")
g1Results = measureGc("20868.2521")
zResults = measureGc("20868.2526")
results = [
           ["G1", statistics.mean(g1Results), statistics.stdev(g1Results), g1Results],
           ["Parallel ", statistics.mean(parallelResults), statistics.stdev(parallelResults), parallelResults],
           ["Z", statistics.mean(zResults), statistics.stdev(zResults)],
           ]
print(results)
