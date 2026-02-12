pkgname = "fonts-inter"
pkgver = "4.1"
pkgrel = 1
pkgdesc = "Inter typeface family"
license = "OFL-1.1"
url = "https://rsms.me/inter"
source = f"https://github.com/rsms/inter/releases/download/v{pkgver}/Inter-{pkgver}.zip"
sha256 = "9883fdd4a49d4fb66bd8177ba6625ef9a64aa45899767dde3d36aa425756b11e"
options = ["empty"]


def install(self):
    self.install_file("*.ttf", "usr/share/fonts/inter", glob=True)
    self.install_file("extras/ttf/*.ttf", "usr/share/fonts/inter", glob=True)
    self.install_file("extras/otf/*.otf", "usr/share/fonts/inter", glob=True)
    self.install_file("*.ttc", "usr/share/fonts/inter", glob=True)
    self.install_license("LICENSE.txt")


@subpackage("fonts-inter-otf")
def _(self):
    self.subdesc = "OpenType (OTF): static fonts with cubic outlines; one file per style."
    self.depends = [self.parent, "!fonts-inter-ttf", "!fonts-inter-ttc"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/inter/*.otf"]


@subpackage("fonts-inter-ttf")
def _(self):
    self.subdesc = "TrueType (TTF): static fonts with quadratic outlines; one file per style."
    self.depends = [self.parent, "!fonts-inter-otf", "!fonts-inter-ttc"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/inter/*.ttf"]


@subpackage("fonts-inter-ttc")
def _(self):
    self.subdesc = "TrueType Collection (TTC): static fonts with quadratic outlines; single SFNT file containing all styles, eliminating redundancies. Well-suited for OS-level deployment, e.g. as a UI font."
    self.depends = [self.parent, "!fonts-inter-otf", "!fonts-inter-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/inter/*.ttc"]
