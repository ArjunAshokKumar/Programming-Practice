class DoorMat(object):
    def createDoorMat(self, size):
        N = int(size.split()[0])
        M = int(size.split()[1])
        print(N)
        print(M)
        if M != 3*N:
            print("Invalid Input: M must be 3 times N.")
            return
        
        times1 = int(((N-1)/2)*3)
        times2 = 1
        print(times1)
        print(times2)

        for i in range(int(N/2)):
            pattern1 = '-'*times1
            pattern2 = '.|.'*times2
            print(pattern1,pattern2,pattern1)
            times1-=3
            times2+=2
        print('-'*(int((M-7)/2)), 'WELCOME', '-'*(int((M-7)/2)))
        for i in range(int(N/2)):
            times1+=3
            times2-=2
            pattern1 = '-'*times1
            pattern2 = '.|.'*times2
            print(pattern1,pattern2,pattern1)
            

dm_obj = DoorMat()
dm_obj.createDoorMat("11 33")