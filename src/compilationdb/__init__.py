r"""Generate a `compile_commands.json` for Python C extension modules.

`JSON Compilation Database
<https://clang.llvm.org/docs/JSONCompilationDatabase.html>`_
(`compile_commands.json`) is a standardized format used by various
development tools (like clangd, clang-tidy, etc.) to understand how to
compile source files in a project. This package provides utilities to
generate such a database specifically for Python C extension modules.
"""

from typing import NotRequired, TypedDict


class CompilationCommandDict(TypedDict):
    """Represents a single compilation command in compilation databases.

    See `the format specification
    <https://clang.llvm.org/docs/JSONCompilationDatabase.html>`_
    for details.
    """

    directory: str
    """The working directory of the compilation."""

    file: str
    """The path to the source file being compiled.

    This must be either absolute or relative to the working directory
    specified in the :attr:`directory`.
    """

    arguments: NotRequired[list[str]]
    """The command line arguments used to compile the source file."""
