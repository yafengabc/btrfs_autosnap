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
    fi=open('/boot/grub/grub.cfg')
    for i in fi:
        if i!=autostring:
            grub_header+=i
        else:
            break
    fi.close()
    fi=open('/boot/grub/grub.cfg')
    for i in fi:
        if i.find('Arch Linux')!=-1:
            begin=1
        if begin==1:
            def_entry+=i
            if i.strip()=='}':
                break
    fi.close()

def get_cmd():
    device=root=''
    try:
        device,root=sys.argv[1].split('.')
    except Exception:
        print("::please input the params")
    return device,root

def manage_snap(device,root):
    global grub_header
    sub_vols=os.listdir('/mnt')
    snap_vols=[i for i in sub_vols if i.find(root+'_')!=-1]
    snap_vols.reverse()
    while len(snap_vols)>5:
        os.system('btrfs subvol delete /mnt/'+snap_vols.pop())
    get_grub_header()
    for i in snap_vols:
        bootstring=autostring
        tmp=def_entry.replace('Arch Linux','Arch Linux '+root)
        bootstring+=tmp.replace(root,i)
        grub_header+=bootstring
    fi=open('/boot/grub/grub.cfg','w')
    fi.write(grub_header)
    fi.close()
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
