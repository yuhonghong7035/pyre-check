# Copyright (c) 2016-present, Facebook, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


class Error:
    ignore_error = False  # type: bool
    external_to_global_root = False  # type: bool

    def __init__(
        self, ignore_error: bool = False, external_to_global_root: bool = False, **error
    ) -> None:
        self.line = error["line"]
        self.column = error["column"]
        self.path = error["path"]
        self.code = error["code"]
        self.name = error["name"]
        self.description = error["description"]
        self.inference = error["inference"]
        self.ignore_error = ignore_error
        self.external_to_global_root = external_to_global_root

    def __repr__(self):
        return self.__key() + " " + self.description

    def __key(self):
        return self.path + ":" + str(self.line) + ":" + str(self.column)

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __lt__(self, other):
        return self.__key() < other.__key()

    def __hash__(self) -> int:
        return hash(self.__key())

    def is_ignored(self) -> bool:
        return self.ignore_error

    def is_external_to_global_root(self) -> bool:
        return self.external_to_global_root
