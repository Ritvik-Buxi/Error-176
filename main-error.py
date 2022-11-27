import speedtest
import numpy as np
import matplotlib.pyplot as plt
#import time
listDownloadSpeed = np.array([])
listUploadSpeed = np.array([])
for i in range(5):
    st = speedtest.Speedtest(secure=True)
    downloadSpeed = round(st.download()/1000000,2)
    uploadSpeed = round(st.upload()/1000000,2)
    np.append(listDownloadSpeed,(downloadSpeed))
    np.append(listUploadSpeed,(uploadSpeed))
    #time.sleep(60)
    print(listDownloadSpeed)
    print(listUploadSpeed)
    x = np.array([1,2,3,4,5])
    y = listDownloadSpeed
    plt.figure(figsize=(15,7))
    plt.plot(x, y)
    plt.show()
