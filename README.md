# btrfs_autosnap 使用说明

安装后，用systemctl enable btrfs_autosnap@device.root的方式来启动服务
例如，btrfs分区为/dev/sda2 想要自动快照的分区为rootfs，则命令为：
systemctl enable btrfs_autosnap@sda2.rootfs
