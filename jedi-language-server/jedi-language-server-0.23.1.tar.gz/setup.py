# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jedi_language_server']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0', 'jedi==0.18.0', 'pygls>=0.9.1,<0.10.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.8"': ['cached-property>=1.5.1']}

entry_points = \
{'console_scripts': ['jedi-language-server = jedi_language_server.cli:cli']}

setup_kwargs = {
    'name': 'jedi-language-server',
    'version': '0.23.1',
    'description': 'A language server for Jedi!',
    'long_description': '# jedi-language-server\n\n[![image-version](https://img.shields.io/pypi/v/jedi-language-server.svg)](https://python.org/pypi/jedi-language-server)\n[![image-license](https://img.shields.io/pypi/l/jedi-language-server.svg)](https://python.org/pypi/jedi-language-server)\n[![image-python-versions](https://img.shields.io/pypi/pyversions/jedi-language-server.svg)](https://python.org/pypi/jedi-language-server)\n\nA [Language Server](https://microsoft.github.io/language-server-protocol/) for the latest version(s) of [Jedi](https://jedi.readthedocs.io/en/latest/). If using Neovim/Vim, we recommend using with [coc-jedi](https://github.com/pappasam/coc-jedi).\n\n**Note:** this tool is actively used by its primary author. He\'s happy to review pull requests / respond to issues you may discover.\n\n## Installation\n\nFrom your command line (bash / zsh), run:\n\n```bash\npip install -U jedi-language-server\n```\n\n`-U` ensures that you\'re pulling the latest version from pypi.\n\nAlternatively, consider using [pipx](https://github.com/pipxproject/pipx) to keep jedi-language-server isolated from your other Python dependencies. Don\'t worry, jedi is smart enough to figure out which Virtual environment you\'re currently using!\n\n## Capabilities\n\njedi-language-server aims to support all of Jedi\'s capabilities and expose them through the Language Server Protocol. It currently supports the following Language Server capabilities:\n\n### Language Features\n\n- [completionItem/resolve](https://microsoft.github.io/language-server-protocol/specification#completionItem_resolve)\n- [textDocument/codeAction](https://microsoft.github.io/language-server-protocol/specification#textDocument_codeAction) (refactor.inline, refactor.extract)\n- [textDocument/completion](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_completion)\n- [textDocument/definition](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_definition)\n- [textDocument/documentHighlight](https://microsoft.github.io/language-server-protocol/specification#textDocument_documentHighlight)\n- [textDocument/documentSymbol](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_documentSymbol)\n- [textDocument/hover](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_hover)\n- [textDocument/publishDiagnostics](https://microsoft.github.io/language-server-protocol/specification#textDocument_publishDiagnostics)\n- [textDocument/references](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_references)\n- [textDocument/rename](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_rename)\n- [textDocument/signatureHelp](https://microsoft.github.io/language-server-protocol/specification#textDocument_signatureHelp)\n- [workspace/symbol](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#workspace_symbol)\n\n### Text Synchronization (for diagnostics)\n\n- [textDocument/didChange](https://microsoft.github.io/language-server-protocol/specification#textDocument_didChange)\n- [textDocument/didOpen](https://microsoft.github.io/language-server-protocol/specification#textDocument_didOpen)\n- [textDocument/didSave](https://microsoft.github.io/language-server-protocol/specification#textDocument_didSave)\n\n## Editor Setup\n\nThe following instructions show how to use jedi-language-server with your development tooling. The instructions assume you have already installed jedi-language-server.\n\n### Vim / Neovim\n\nUsers may choose 1 of the following options:\n\n- [coc.nvim](https://github.com/neoclide/coc.nvim) with [coc-jedi](https://github.com/pappasam/coc-jedi).\n- [ALE](https://github.com/dense-analysis/ale).\n- [Neovim\'s native LSP client](https://neovim.io/doc/user/lsp.html). See [here](https://github.com/neovim/nvim-lspconfig#jedi_language_server) for an example configuration.\n- [vim-lsp](https://github.com/prabirshrestha/vim-lsp).\n\nNote: this list is non-exhaustive. If you know of a great choice not included in this list, please submit a PR!\n\n### Emacs\n\nUsers may choose 1 of the following options:\n\n- [lsp-jedi](https://github.com/fredcamps/lsp-jedi).\n\nNote: this list is non-exhaustive. If you know of a great choice not included in this list, please submit a PR!\n\n### Command line (bash / zsh)\n\nAt your terminal prompt:\n\n```bash\njedi-language-server\n```\n\njedi-language-server currently works only over IO. This may change in the future.\n\n## Configuration\n\nWe recommend using [coc-jedi](https://github.com/pappasam/coc-jedi) and following its [configuration instructions](https://github.com/pappasam/coc-jedi#configuration).\n\nIf you are configuring manually, jedi-language-server supports the following [initializationOptions](https://microsoft.github.io/language-server-protocol/specification#initialize):\n\n```json\n...\n  "initializationOptions": {\n    "markupKindPreferred": null,\n    "jediSettings": {\n      "autoImportModules": []\n    },\n    "completion": {\n      "disableSnippets": false,\n      "resolveEagerly": false\n    },\n    "diagnostics": {\n      "enable": true,\n      "didOpen": true,\n      "didChange": true,\n      "didSave": true\n    },\n    "workspace": {\n      "extraPaths": []\n    }\n  }\n...\n```\n\nSee coc-jedi\'s [configuration instructions](https://github.com/pappasam/coc-jedi#configuration) for an explanation of the above configurations.\n\n## Additional Diagnostics\n\njedi-langugage-server provides diagnostics about syntax errors, powered by Jedi. If you would like additional diagnostics, we suggest using the powerful [diagnostic-language-server](https://github.com/iamcco/diagnostic-languageserver).\n\n## Code Formatting\n\nAgain, we recommend that you use [diagnostic-language-server](https://github.com/iamcco/diagnostic-languageserver). It also supports code formatting.\n\n## Local Development\n\nTo build and run this project from source:\n\n### Dependencies\n\nInstall the following tools manually:\n\n- [Poetry](https://github.com/sdispater/poetry#installation)\n- [GNU Make](https://www.gnu.org/software/make/)\n\n#### Recommended\n\n- [asdf](https://github.com/asdf-vm/asdf)\n\n### Get source code\n\n[Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) this repository and clone the fork to your development machine:\n\n```bash\ngit clone https://github.com/<YOUR-USERNAME>/jedi-language-server\ncd jedi-language-server\n```\n\n### Set up development environment\n\n```bash\nmake setup\n```\n\n### Run tests\n\n```bash\nmake test\n```\n\n## Inspiration\n\nPalantir\'s [python-language-server](https://github.com/palantir/python-language-server) inspired this project. Unlike python-language-server, jedi-language-server:\n\n- Uses [pygls](https://github.com/openlawlibrary/pygls) instead of creating its own low-level Language Server Protocol bindings\n- Supports one powerful 3rd party library: Jedi. By only supporting Jedi, we can focus on supporting all Jedi features without exposing ourselves to too many broken 3rd party dependencies (I\'m looking at you, [rope](https://github.com/python-rope/rope)).\n- Is supremely simple because of its scope constraints. Leave complexity to the Jedi [master](https://github.com/davidhalter). If the force is strong with you, please submit a PR!\n\n## Written by\n\nSamuel Roeca _samuel.roeca@gmail.com_\n',
    'author': 'Sam Roeca',
    'author_email': 'samuel.roeca@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pappasam/jedi-language-server',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
