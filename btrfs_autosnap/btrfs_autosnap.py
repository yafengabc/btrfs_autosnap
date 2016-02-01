#!/usr/bin/env python
import time
import sys
import os
autostring='####BEGIN AUTOSNAP####\n'
grub_header=''
def_entry=''
time_s=time.strftime("%Y%m%d_%H%M%S",time.localtime())

def get_grub_header():
    global grub_header
    global def_entry
    begin=0
    #Get the /boot/grub/grub.cfg content
    fi=open('/boot/grub/grub.cfg')
    for i in fi:
        if i!=autostring:
            grub_header+=i
        else:
            break
    fi.close()
    #get the Archlinux grub entry
    fi=open('/boot/grub/grub.cfg')
    for i in fi:
        if i.find('Arch Linux')!=-1:
            begin=1
        if begin==1:
            def_entry+=i
            if i.strip()=='}':
                break
    fi.close()

#check the subvol is rootfs?
def check_rootfs(root):
    pip=os.popen("mount |grep "+root)
    m_str=pip.readlines()
    if str(m_str).find(' / ')!=-1:
        return True
    else:
        return False

#Get the command line argvs
def get_cmd():
    device=root=''
    try:
        device,root=sys.argv[1].split('.')
    except Exception:
        print("::please input the params")
    return device,root

#manage the snapshot delete the old snapshot keep last 5 snapshot
def manage_snap(device,root):
    global grub_header
    sub_vols=os.listdir('/mnt')
    snap_vols=[i for i in sub_vols if i.find(root+'_')!=-1]
    snap_vols.reverse()
    while len(snap_vols)>5:
        os.system('btrfs subvol delete /mnt/'+snap_vols.pop())
    #add some boot entry for snapshot
    if check_rootfs(root):
        print("make grub enty")
        get_grub_header()
        for i in snap_vols:
            bootstring=autostring
            tmp=def_entry.replace('Arch Linux','Arch Linux '+root)
            bootstring+=tmp.replace(root,i)
            grub_header+=bootstring
        fi=open('/boot/grub/grub.cfg','w')
        fi.write(grub_header)
        fi.close()

#make a snapshot 
def make_snap(device,snap_s):
    print("::Mounting the root device")
    os.system("mount /dev/"+device+" /mnt")
    os.system("btrfs subvol snap /mnt/"+snap_s+" /mnt/"+snap_s+"_"+time_s)
    manage_snap(device,snap_s)
    print("::Unmount the root device")
    os.system("umount /mnt")


if __name__=="__main__":
    device,snap_s=get_cmd()
    make_snap(device,snap_s)
    print(check_rootfs(snap_s))
