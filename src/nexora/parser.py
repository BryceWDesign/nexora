# src/nexora/parser.py

"""
Nexora Parser Module
---------------------
This module will parse .nex source files into an abstract syntax tree (AST).
The parser is language-agnostic and modular. Future versions may support plugins.

This is the initial scaffold. Actual parsing rules will be built once
the grammar specification is finalized.
"""

from dataclasses import dataclass
from typing import List, Union, Optional


@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int


@dataclass
class ASTNode:
    type: str
    value: Union[str, List['ASTNode']]
    children: Optional[List['ASTNode']] = None


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0

    def parse(self) -> ASTNode:
        """
        Entry point to parse the token list and return the root AST node.
        For now, returns a placeholder node.
        """
        return ASTNode(type="Program", value="Nexora program", children=[])

    def _current_token(self) -> Optional[Token]:
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def _advance(self):
        self.position += 1

