#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class PkgConf(Tarball, Meson):
    def __init__(self):
        Project.__init__(
            self,
            "pkgconf",
            prj_dir="pkgconf",
            version="1.9.3",
            archive_url="https://distfiles.dereferenced.org/pkgconf/pkgconf-{version}.tar.gz",
            hash="6d73ac21a9410f5cc636acf730f3a5bf46b28d1e18a239c89efc4b2c5548792f",
            dependencies=["ninja", "meson"],
            patches=["0001-libpkgconf-add-defines-to-unbreak-build-with-VS2013.patch"],
        )
        self.add_param("-Dtests=false")

    def build(self):
        Meson.build(self)
        self.install(r".\COPYING share\doc\pkgconf")

    def post_install(self):
        self.exec_cmd(
            r"copy %(gtk_dir)s\bin\pkgconf.exe %(gtk_dir)s\bin\pkg-config.exe"
        )
