
#################################
# get disk usage per dir
##############################


import os
import time

class DiskUsage(object) :
    filepath = "/home/fwere"

    def getFreeSpace(self):
        filepath = self.filepath
        stinfo = os.statvfs(filepath)
        print("directory information for file depicted above is:= {}".format(stinfo))
        #filepath = self.filepath
        st = os.statvfs(filepath + "/")
        du = st.f_bavail * st.f_frsize

        du2 = stinfo.f_bavail * stinfo.f_frsize
        print("Disk for directory usage is: => {}".format(du2))
        print("DaIndexing SetUp()")
        print("Another capture of Disk usage: => {}".format(du))
        return du2

if __name__ == "__main__":
    dsk = DiskUsage()
    dsk.getFreeSpace()

