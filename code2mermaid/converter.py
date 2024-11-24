from typing import Dict, Optional
from .core import (
    Node, 
    count_indent, 
    detect_node_type,   
    generate_node_id,
    parse_annotation,
    parse_function_parameters,     
    parse_label,    
    sanitize_code,
)
from .style import node_style

def code_to_mermaid(
    code: str, 
    title: Optional[str] = None,
    orientation: Optional[str] = "TD",
    remove_self: Optional[bool] = False,
    _node_style: Optional[Dict[str, str]] = node_style,
) -> str:
    """ Code converter for Mermaid chartflows
      
          Possible FlowChart orientations are:

    TB - Top to bottom
    TD - Top-down/ same as top to bottom
    BT - Bottom to top
    RL - Right to left
    LR - Left to right
    """    
    lines = code.split('\n')
    mermaid = ""
    if title:
        mermaid += f"---\ntitle: {title}\n---\n"
    # theme
    theme = """%%{
        init: {
            'theme': 'base',
            'themeVariables': {
            'primaryColor': '#E9E7E7',
            'primaryTextColor': '#000000',
            'primaryBorderColor': '#C0000',
            'lineColor': '#F8B229',
            'secondaryColor': '#91939C',
            'tertiaryColor': '#fff'
            }
        }
    }%%\n"""
    mermaid += theme
    mermaid += f"flowchart {orientation}\n"

    nodes: Dict[str, Node] = {}
    last_node_at_level: Dict[int, str] = {}
    branch_ends: Dict[str, Optional[str]] = {"if": None, "elif": None, "else": None}
    current_branch_type: Optional[str] = None
    
    previous_node_id = None
    pending_label = None

    # Variables for conditional nodes
    current_conditional = None
    last_condition_node = None
    
    # Variables for loop control
    current_loop = None
    loop_first_node = None
    loop_last_node = None

    # Variables for function control and parameters
    function_params = None
    first_node_after_def = None

    for line in lines:
        if not line.strip():
            continue

        indent = count_indent(line)
        code_part = line.split('#')[0].rstrip()
        if not code_part.strip():
            label = parse_label(line)
            if label:
                pending_label = label
            continue

        sanitized_code = sanitize_code(code_part.lstrip(), remove_self)
        node_type = detect_node_type(sanitized_code)
        node_id = generate_node_id()

        # Special handling for function definition
        if node_type == "function":
            function_params = parse_function_parameters(code_part)
            continue  # Pula a criação do nó da função
        
        # If we are right after a function definition, mark this node
        if function_params is not None and first_node_after_def is None:
            first_node_after_def = node_id

        node = Node(sanitized_code, node_id, node_type)
        node.indent_level = indent

        annotation = parse_annotation(line)
        if annotation:
            node.label = annotation

        if pending_label and previous_node_id:
            nodes[previous_node_id].label = pending_label
            pending_label = None

        # Logic for loops
        if node_type == "loop":
            current_loop = node_id
            loop_first_node = None
            loop_last_node = None
        elif current_loop and indent > nodes[current_loop].indent_level:
            if loop_first_node is None:
                loop_first_node = node_id
            loop_last_node = node_id
        elif current_loop and indent <= nodes[current_loop].indent_level:
            # Add connection from last loop node back to loop
            if loop_last_node:
                nodes[loop_last_node].next_node = current_loop
            current_loop = None
            loop_first_node = None
            loop_last_node = None

        # Logic for conditionals
        if node_type == "condition":
            if sanitized_code.startswith('if '):
                current_conditional = generate_node_id()
                conditional_node = Node("Decision", current_conditional, "conditional")
                conditional_node.indent_level = indent
                nodes[current_conditional] = conditional_node

                if previous_node_id:
                    nodes[previous_node_id].next_node = current_conditional

                conditional_node.children.append(node_id)
                node.parent_node = current_conditional
                current_branch_type = "if"
                last_condition_node = node_id

            elif sanitized_code.startswith('elif '):
                if current_conditional:
                    nodes[current_conditional].children.append(node_id)
                    node.parent_node = current_conditional
                    node.is_elif_else = True
                    current_branch_type = "elif"
                    last_condition_node = node_id

            elif sanitized_code.startswith('else'):
                if current_conditional:
                    nodes[current_conditional].children.append(node_id)
                    node.parent_node = current_conditional
                    node.is_elif_else = True
                    current_branch_type = "else"
                    last_condition_node = node_id

        # Connect inner nodes of conditional blocks
        elif current_conditional and indent > nodes[current_conditional].indent_level:
            if last_condition_node:
                # Connect the condition node to its inner node
                nodes[last_condition_node].inner_node = node_id
                branch_ends[current_branch_type] = node_id

        # Exit from conditional block
        elif current_conditional and indent <= nodes[current_conditional].indent_level:
            # Connect all branch_ends to the next node
            for branch_end in branch_ends.values():
                if branch_end:
                    nodes[branch_end].next_node = node_id
            current_conditional = None
            last_condition_node = None
            branch_ends = {"if": None, "elif": None, "else": None}
            current_branch_type = None

        # Normal connection outside conditionals
        elif previous_node_id and not nodes[previous_node_id].is_elif_else:
            nodes[previous_node_id].next_node = node_id

        nodes[node_id] = node
        last_node_at_level[indent] = node_id
        previous_node_id = node_id

    for node_id, node in nodes.items():
        # Node style based-on type
        if node.type == "conditional":
            mermaid += f" {node_id}{{ **{node.code}** }}\n"
        elif node.type == "condition":
            mermaid += f" {node_id}{{{{ **{node.code[:-1]}** }}}}\n"
        elif node.type == "loop":
            mermaid += f" {node_id}(( **{node.code[:-1]}** ))\n"
        elif node.type == "terminal":
            mermaid += f" {node_id}([**{node.code}**])\n"
        elif node.type == "functional":
            mermaid += f" {node_id}>**{node.code}**]\n"            
        else:
            mermaid += f" {node_id}[ **{node.code}** ]\n"
        
        # Add connections 
        if isinstance(node.next_node, str):
            if node.label:
                mermaid += f" {node_id} -->|{node.label}| {node.next_node}\n"
            else:
                mermaid += f" {node_id} --> {node.next_node}\n"
                if node.type == "loop":
                    mermaid += f"{node.next_node} -->|loop| {node_id}\n"
        
        # Add connections for children
        for child in node.children:
            if node.label:
                mermaid += f" {node_id} -->|{node.label}| {child}\n"
            else:
                mermaid += f" {node_id} --> {child}\n"

        # Add connections to internal nodes
        if node.inner_node:
            if node.label:
                mermaid += f" {node_id} -->|{node.label}| {node.inner_node}\n"
            else:
                mermaid += f" {node_id} --> {node.inner_node}\n"


    # Add parameter subgraph if function exists
    if function_params and first_node_after_def:
        mermaid += "\nsubgraph PARAMETERS\n"
        mermaid += "direction LR\n"
        
        # Create nodes for each parameter
        param_nodes = []
        for i, param in enumerate(function_params):
            param_node_id = f"param_{i}"
            param_nodes.append(param_node_id)
            mermaid += f"{param_node_id}([**{param}**])\n"
        
        # Connect parameters with invisible connections
        for i in range(len(param_nodes) - 1):
            mermaid += f"{param_nodes[i]} ~~~~ {param_nodes[i + 1]}\n"
        
        mermaid += "end\n"
        # Connect subgraph to first node of function
        mermaid += f"PARAMETERS --> {first_node_after_def}\n"

    # Add styles
    mermaid += "\n%% Styles\n"
    mermaid += f"classDef conditional fill:{_node_style['conditional']},stroke:#333,stroke-width:2px;\n"
    mermaid += f"classDef condition fill:{_node_style['condition']},stroke:#333,stroke-width:2px;\n"
    mermaid += f"classDef functional fill:{_node_style['functional']},stroke:#333,stroke-width:2px;\n"
    mermaid += f"classDef loop fill:{_node_style['loop']},stroke:#333,stroke-width:2px;\n"
    mermaid += f"classDef terminal fill:{_node_style['terminal']},stroke:#333,stroke-width:2px;\n"
    mermaid += f"classDef parameter fill:{_node_style['parameter']},stroke:#333,stroke-width:px;\n"

    # Apply styles in nodes
    for node_id, node in nodes.items():
        mermaid += f"class {node_id} {node.type};\n"

    if function_params:
        # Apply styles in parameters
        for i in range(len(function_params)):
            mermaid += f"class param_{i} parameter;\n"

    return mermaid