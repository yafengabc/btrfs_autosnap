#!/usr/bin/env python
import sys
import os

#Get the command line argvs
def get_cmd():
    device=root=''
    try:
        device,root=sys.argv[1].split('.')
    except Exception:
        print("::please input the params")
    return device,root

def rollback(device,root):
    base='/mnt/'
    print("::Mounting the device")
    os.system('mount /dev/'+device+' '+base)
    sub_vols=os.listdir(base)
    snap_vols=[i for i in sub_vols if i.find(root+'_')!=-1]
    snap_vols.reverse()
    index=0
    print("::Please select one snapshot to rollback:")
    for i in snap_vols:
        print(str(index)+'.'+i)
        index+=1
    index=input("::Please input a number(default 0):")
    try:
        select=snap_vols[int(index)]
    except:
        select=snap_vols[0]
    print('::Warning! Will use',select," to recover ",root,"!!!")
    ask=input("::Please enter 'yes' to continue:")
    if ask=='yes':
        print('::Delete the subvol',root)
        os.system('btrfs subvol delete '+base+root+"/var/lib/machines")
        os.system('btrfs subvol delete '+base+root)
        print('::Rollback the snapshot')
        os.system('btrfs subvol snapshot '+base+select+' '+base+root)
        print("::Done...")
    else:
        print('::Do nothing! exit.')
    os.system('umount '+base)

if __name__=="__main__":
    device,snap_s=get_cmd()
    rollback(device,snap_s)
