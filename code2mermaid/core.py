import re
from dataclasses import dataclass, field
from uuid import uuid4
from typing import List, Optional

@dataclass
class Node:
    code: str
    id: str
    type: str = "default"
    next_node: Optional[str] = None
    label: Optional[str] = None
    indent_level: int = 0
    children: List[str] = field(default_factory=list)
    else_node: Optional[str] = None
    parent_node: Optional[str] = None
    is_elif_else: bool = False
    inner_node: Optional[str] = None
    loop_start: Optional[str] = None

def parse_function_parameters(line: str) -> List[str]:
    """Extract function parameters from a function definition line."""
    match = re.search(r'def.*?\((.*?)\)', line)
    if not match:
        return []
    
    params = match.group(1).split(',')
    clean_params = []
    
    for param in params:
        # Remove whitespace and type hints
        param = param.split(':')[0].strip()
        # Skip 'self' parameter
        if param and param != 'self':
            clean_params.append(param)
            
    return clean_params

def count_indent(line: str) -> int:
    return len(line) - len(line.lstrip())

def sanitize_code(line: str, remove_self: bool) -> str:
    line = line.replace('(', '﹙')
    line = line.replace(')', '﹚')
    line = line.replace('[', '〔')
    line = line.replace(']', '〕')
    line = line.replace('"', '‶')
    line = line.replace("'", "‵")
    if remove_self:
        line = line.replace("self.", ' ')
    return line

def parse_label(line: str) -> Optional[str]:
    match = re.search(r'#>\s*(.*?)$', line)
    if match:
        return match.group(1).strip()
    return None

def parse_annotation(line: str) -> Optional[str]:
    match = re.search(r'#\s*\|(.*?)\|', line)
    if match:
        return match.group(1).strip()
    return None

def generate_node_id() -> str:
    return f"node_{str(uuid4())[:8]}"

def detect_node_type(code: str) -> str:
    code = code.strip()
    if code.startswith('def '):
        return "function"
    elif code.startswith(('if ', 'elif ', 'else')):
        return "condition"
    elif " F." in code:
        return "functional"
    elif code.startswith(('for ', 'while ')):
        return "loop"
    elif code.startswith('return '):
        return "terminal"
    return "default"