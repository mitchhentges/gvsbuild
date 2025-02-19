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
from gvsbuild.utils.base_expanders import GitRepo
from gvsbuild.utils.base_project import project_add


@project_add
class Emeus(GitRepo, Meson):
    def __init__(self):
        Meson.__init__(
            self,
            "emeus",
            repository="https://github.com/ebassi/emeus",
            repo_url="https://github.com/ebassi/emeus.git",
            fetch_submodules=False,
            tag="master",
            dependencies=["ninja", "meson", "pkgconf", "gtk3"],
            patches=["00_win_no_script.patch"],
        )
        if self.opts.enable_gi:
            self.add_dependency("gobject-introspection")
            enable_gi = "true"
        else:
            enable_gi = "false"

        self.add_param("-Ddocs=false")
        self.add_param(f"-Dintrospection={enable_gi}")

    def build(self):
        Meson.build(self, make_tests=True)
        self.install(r".\COPYING.txt share\doc\emeus")
