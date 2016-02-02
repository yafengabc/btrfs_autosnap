# btrfs_autosnap 使用说明
##注意：现在仅限Archlinux使用，其他系统慎用

安装后，用systemctl enable btrfs_autosnap@device.root的方式来启动服务
例如，btrfs分区为/dev/sda2 想要自动快照的分区为rootfs，则命令为：
systemctl enable btrfs_autosnap@sda2.rootfs

每次重启，都会新建一个快照，并加入grub启动项，若想手动建立快照可以用
systemctl start btrfs_autosnap@sda2.rootfs
或者直接使用命令行：
btrfs_autosnap.py sda2.rootfs

##回滚方法：
1.先用一个快照启动；
2.运行
btrfs_rollback.py sda2.rootfs
根据提示操作恢复即可。
