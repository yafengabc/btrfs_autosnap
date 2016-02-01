# Maintainer: Yafeng <yafengabc@gmail.com>

pkgname=btrfs_autosnap
pkgver=0.0.1
pkgrel=1
pkgdesc="Auto snapshot the btrfs subvol"
url=""
arch=('any')
license=('GPLv3')
depends=('glibc' 'sh' 'python')
provides=('btrfs_autosnap')
source=('btrfs_autosnap.tar.gz')
sha1sums=('SKIP')

build() {
  cd "${srcdir}"
}


package() {
  #install scripts to /usr/bin
install -D "${srcdir}/${pkgname}/btrfs_autosnap.py" "${pkgdir}/usr/bin/btrfs_autosnap.py"
install -D "${srcdir}/${pkgname}/btrfs_rollback.py" "${pkgdir}/usr/bin/btrfs_rollback.py"
  # install systemd files
install -Dm644 "${srcdir}/${pkgname}/btrfs_autosnap@.service" "${pkgdir}/usr/lib/systemd/system/btrfs_autosnap@.service"
}

