import numpy as np
import cv2
import time
import os
import sys
from grabscreen import grab_screen
from getkeys import key_check


def keys_one_hot(keys):
    #[AWSD]
    output = [0,0,0,0]

    if 'A' in keys:
        output[0] = 1
    elif 'W' in keys:
        output[1] = 1
    elif 'S' in keys:
        output[2] = 1
    else:
        output[3] = 1

    return output




filename = 'training-data-2k-3.npy'

if os.path.isfile(filename):
    print("File exists,loading...")
    training_data = list(np.load(filename))
else:
    print("Creating new file")
    training_data = []




def main():
    #k = 0

    for i in list(range(4))[::-1]:
            print(i+1)
            time.sleep(1)
    
    print("Entering sleep mode...")
    time.sleep(65)
    print("Exiting sleep mode")
    start_time = time.time()
    while True:
        #k = k+1
        
        screen = grab_screen(region=(0,40,800,640))
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
        screen = cv2.resize(screen,(224,224))
        keys = key_check()
        output = keys_one_hot(keys)
        training_data.append([screen,output])
        #print('Frame took {} seconds'.format(time.time()-last_time))
        print('Length:{}'.format(len(training_data)))
        #last_time = time.time()

        #cv2.imshow('window',screen)
        #cv2.imwrite('screengrabs\ss'+str(k)+'.png',screen)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
    
        if len(training_data)  == 2000:
            print(len(training_data))
            print("Capturing  frames took {} secs ".format(time.time()-start_time))
            np.save(filename,training_data)
            print("Data Saved")
            sys.exit()
            
        


main()
