# code2mermaid

[![GitHub LICENSE](https://img.shields.io/github/license/ouhammmourachid/mermaid-py)](https://github.com/ouhammmourachid/mermaid-py/blob/main/LICENSE) [![Mounthly Download](https://img.shields.io/pypi/dm/mermaid-py)](https://pypistats.org/packages/mermaid-py) [![latest version](https://img.shields.io/pypi/v/mermaid-py.svg?style=flat)](https://pypi.org/project/mermaid-py/) [![supported python version](https://img.shields.io/pypi/pyversions/mermaid-py)](https://pypi.org/project/mermaid-py)


code2mermaid is a python-only library to help converter python code in [Mermaid](https://mermaid.js.org/) chartflows specifications. code2mermaid supports conditional and loops.

## Environment

> pip install code2mermaid

To visualize flowcharts you can use

#### Mermaid Live

* https://mermaid.live/

#### mermaid-py

> pip install mermaid-py

``` python
import mermaid as md
from mermaid.graph import Graph

def plot_mermaid(mermaid_diagram):
    graph = Graph(
        title='chartflow',
        script=mermaid_diagram,
    )    
    Mermaid(graph) # render the graph in notebook
```

## Getting Started

``` python
from code2mermaid import code_to_mermaid
```

Mermaid supports five types of orientation:

* TB - Top to bottom (default)
* TD - Top-down/ same as top to bottom
* BT - Bottom to top
* RL - Right to left
* LR - Left to right

code2mermaid add a new node in graph each line in code

Labels are supported using two forms of comments:

* #|my graph annotation|
* #> second form

This makes it possible to keep standard code comments and easily add annotations to the graph

There are 7 types of nodes supported, each of them has its own style:

* default - general code
* conditional - when a node of the if/elif/else type is detected it is inserted into the graph
* condition - the type of the condition, can be if, elif and else
* functional - nodes that contain an F., useful for examples using pytorch-like
* loop - node of the for/while type
* parameter - extracts the parameters of the function and transforms them into nodes. `self` parameters and type annotations are ignored
* terminal - nodes that start with `return` ideal to indicate the end of the graph

#### 1. First Chartflow

``` python
code = """
x = 1
x += 2
print(x)
"""
mermaid_diagram = code_to_mermaid(code)
```

[![](https://mermaid.ink/img/pako:eNqdlN1u2jAUx1_FMooisVA5CSnEU3dRPu521WoXW6bJcexizdiR46gwxINsb9Kn6ivMQNJAYRLaufLx-f2PP459NpDqgkEMPW-TKdCYUMJicDSxM98u2JL5GPg5qZgfXIp-IUaQXLLKP5eXRiyJWU-01GaXpTdLZ6PZ6CxRwz2yle1YtLd_sffaFMx09OQiLIViHTMf30dRegZVjGpVnOwzDdM4nZwfmBkrTkDOuX8KbTu3GW49L1Nc6me6IMaCx6mbVq4EP8KcJnwYjr6Bfn8F7kDY74Pv74NgMPh0mGGIJmOUs5Zo_YP8wx2IjvVttNMn0S0K84K2ROvv9O5WlX19-b16fflzyJIpzwMPdu0qmykqSVVNGQe7mxJWaEUk4EJK3OMJCykLKmv0T4Z7cRw348GzKOwCR-Xq46UE_yfntaKny_MxSkdX66XWZaskBU3zq5Wu9kvRrTufz4fT6dXqkhiyZC7HlfJO_e41FIyTWtrT6FutL0bbOh9FMwUDuHQnIqJwnWD_bzO4_88ZxG7YoBnM1NahpLb6Ya0oxNbULIBG108LiDmRlfPqsiCWTQV5codskZKor1ofuxBv4AriKBnfRBEaheM4QWGM4gCuIUbbAP7a8-gmbWw4RHHoiguZezLafD60rX332v4FA-x5zw?type=png)](https://mermaid.live/edit#pako:eNqdlN1u2jAUx1_FMooisVA5CSnEU3dRPu521WoXW6bJcexizdiR46gwxINsb9Kn6ivMQNJAYRLaufLx-f2PP459NpDqgkEMPW-TKdCYUMJicDSxM98u2JL5GPg5qZgfXIp-IUaQXLLKP5eXRiyJWU-01GaXpTdLZ6PZ6CxRwz2yle1YtLd_sffaFMx09OQiLIViHTMf30dRegZVjGpVnOwzDdM4nZwfmBkrTkDOuX8KbTu3GW49L1Nc6me6IMaCx6mbVq4EP8KcJnwYjr6Bfn8F7kDY74Pv74NgMPh0mGGIJmOUs5Zo_YP8wx2IjvVttNMn0S0K84K2ROvv9O5WlX19-b16fflzyJIpzwMPdu0qmykqSVVNGQe7mxJWaEUk4EJK3OMJCykLKmv0T4Z7cRw348GzKOwCR-Xq46UE_yfntaKny_MxSkdX66XWZaskBU3zq5Wu9kvRrTufz4fT6dXqkhiyZC7HlfJO_e41FIyTWtrT6FutL0bbOh9FMwUDuHQnIqJwnWD_bzO4_88ZxG7YoBnM1NahpLb6Ya0oxNbULIBG108LiDmRlfPqsiCWTQV5codskZKor1ofuxBv4AriKBnfRBEaheM4QWGM4gCuIUbbAP7a8-gmbWw4RHHoiguZezLafD60rX332v4FA-x5zw)


``` python

```

``` python

```