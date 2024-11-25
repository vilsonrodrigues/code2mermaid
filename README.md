# code2mermaid


[![GitHub LICENSE](https://img.shields.io/github/license/vilsonrodrigues/code2mermaid)](https://github.com/vilsonrodrigues/code2mermaid/blob/main/LICENSE) [![Mounthly Download](https://img.shields.io/pypi/dm/code2mermaid)](https://pypistats.org/packages/code2mermaid) [![latest version](https://img.shields.io/pypi/v/code2mermaid.svg?style=flat)](https://pypi.org/project/mermaid-py/) [![supported python version](https://img.shields.io/pypi/pyversions/code2mermaid)](https://pypi.org/project/code2mermaid)

**code2mermaid** is a python-only library to help convert Python code in [Mermaid](https://mermaid.js.org/) chartflows specifications. **code2mermaid** supports conditional and loops.

## Environment

Install the project

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

**code2mermaid** add a new node in graph each line in code

Labels are supported using two forms of comments:

* #> first form
* #|second form|

This makes it possible to keep standard code comments and easily add annotations to the graph. 

There are 7 types of nodes supported, each of them has its own style:

* default - general code
* conditional - when a node of the if/elif/else type is detected it is inserted into the graph
* condition - the type of the condition, can be if, elif and else
* functional - nodes that contain an F., useful for examples using pytorch-like
* loop - node of the for/while type
* parameter - extracts the parameters of the function and transforms them into nodes. `self` parameters and type annotations are ignored
* terminal - nodes that start with `return` ideal to indicate the end of the graph

Observation: add labels in loops or conditional nodes is not supported.

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

#### 2. Conditional Node

``` python
code = """
x = 1
if x == 1:
    print(x)
else:
    print("x is not equal to 1")
"""
mermaid_diagram = code_to_mermaid(code)
```

[![](https://mermaid.ink/img/pako:eNqdVNmK2zAU_RWhEAzBKV6S8VLah8ny1qcZ-tC6FNm-mog6UirLTNJg6G-0H1KY3-kPzC9UWbxlgVA96d57zl2kw93iRKSAQ9zvbyOOjodxpkLUcuyOoRawBCNERkxyMMxL0Y9EMhJnkBvn9JVkSyI3E5EJucvSmwUzb-adJTriHmGtGqy1P9ew90KmIBv05CI4YxwazNy_d5zgDJRDInja6TOwAzeYnA8MUrEOkFJqdEFlYx6vZb8fcZqJ52RBpEKPU-3m-gu-uikknm-Rz2gwWKN3yB4M0JfTIBoO3x88kIwsJ3ZHFaKyt5o-hYTlTHCdoTyNNxnieOzcjVLvOoK6I39se3GFqBjbXRFGkW7z0GdZnkKaJM6IEjv160Yrezen_j6uXl9-rV9ffrfHrQrvC0GWQ6dGFW2NYpO7wAncuouj3a7x9-efNWK5BigE3wuSISWQrb117Yj3--hBbbR8I55kJM-nQNFODkzp19QMyrIs7NEx2AmYuZLiG4Q913WP9-EzS9UidFbrt5cS_B-dFjzplqe-FXg38zMhVhWTpEkQ38zUAl-ypu58Ph9NpzezV0SSJegcN9Ib9onkU6CkyFQ3Wou19T1dRK3EGtGNVzq8nL_W2BV2pbAWG5t4qV-MsFSv0_3yi_B-KUY41NcjMMIRLzWUFEo8bHiCQyULMLEUxdMCh5RotZu4WKVEwZSRJ_2ItXdF-CchlhVFmzjc4jUOnbH_xnEsz_bdsWW7lmviDQ6t0sQ_9njbxKCnEPLDYdnvd375D2534-s?type=png)](https://mermaid.live/edit#pako:eNqdVNmK2zAU_RWhEAzBKV6S8VLah8ny1qcZ-tC6FNm-mog6UirLTNJg6G-0H1KY3-kPzC9UWbxlgVA96d57zl2kw93iRKSAQ9zvbyOOjodxpkLUcuyOoRawBCNERkxyMMxL0Y9EMhJnkBvn9JVkSyI3E5EJucvSmwUzb-adJTriHmGtGqy1P9ew90KmIBv05CI4YxwazNy_d5zgDJRDInja6TOwAzeYnA8MUrEOkFJqdEFlYx6vZb8fcZqJ52RBpEKPU-3m-gu-uikknm-Rz2gwWKN3yB4M0JfTIBoO3x88kIwsJ3ZHFaKyt5o-hYTlTHCdoTyNNxnieOzcjVLvOoK6I39se3GFqBjbXRFGkW7z0GdZnkKaJM6IEjv160Yrezen_j6uXl9-rV9ffrfHrQrvC0GWQ6dGFW2NYpO7wAncuouj3a7x9-efNWK5BigE3wuSISWQrb117Yj3--hBbbR8I55kJM-nQNFODkzp19QMyrIs7NEx2AmYuZLiG4Q913WP9-EzS9UidFbrt5cS_B-dFjzplqe-FXg38zMhVhWTpEkQ38zUAl-ypu58Ph9NpzezV0SSJegcN9Ib9onkU6CkyFQ3Wou19T1dRK3EGtGNVzq8nL_W2BV2pbAWG5t4qV-MsFSv0_3yi_B-KUY41NcjMMIRLzWUFEo8bHiCQyULMLEUxdMCh5RotZu4WKVEwZSRJ_2ItXdF-CchlhVFmzjc4jUOnbH_xnEsz_bdsWW7lmviDQ6t0sQ_9njbxKCnEPLDYdnvd375D2534-s)


#### 3. For Loop Nodes

We can insert titles in flowchart and labels in chart

``` python
code = """
x = 1
for i in range(x): 
    print(i)
x += 2
#> Final result
print(x)
"""
mermaid_diagram = code_to_mermaid(code, "For loop diagram")
```

[![](https://mermaid.ink/img/pako:eNqdVNuO2jAQ_RXLK8QuDYjcSOxq-7Bc3vZpV31os6pMYoPVYCPHaKEsH9L-yX7V_kKdkBACVEL1k2fmnJlx5mS2MJYJhRh2u91IaK5TisFEKpBKuQQJJzNFFpEooq3WNhKgPFxwjcGRIz9tPacL2sagPSUZbVuXol-J4mSa0qx9Tl8qviBqM5SpVHmWmzEaB-PgLFGJe6ZrXWP7xfkX9kGqhKoaPbwITrmgNWYSPjgOOgNlNJYiafSJbOSi4fmDqdK8AWSMtZugXW2W112rFQmWytd4TpQGzyPjFmZKP0ji2mhgs--g01mDe2B3OuDlNAi63S97z9RmKCaJVyEq-_bW8JmZMTdTBIqIGf14_73-eP9j8t3dncLrhHTgUOQwPxINMwe85Xp5u1y3wuVtm2kIbarxfbWXU0xdLPBcBzEvrBCVvX_8p3vgHPOraNHLhAuSAkWzVarLntz-NE6Ic-ipso97Wh96yrUOnvTGqDQScUqybEQZyKfONZd5csbTFN8wn9oxtTKt5E-Kb1zXLe_dV57oOXaW68-XEvwfna1E3CzPwj4KruYXv3TJJEmMplczjY4XvK47mUy80ehq9pKYHUJNjivpNftE2QllxIy0GT3INH9eM3QQ1UXiQTIXo5VAjqLQggvzIQhPzL4sVlcEi5UWQWyuJTCCkdgZKFlp-bQRMcRaragFlVzN5hAzkmbGWi0Toulov18ryJKIb1IemxBv4Rpix0e90PZD33f80A0827PgBmKv33MD3wuQ6wch8tBgZ8FfRYJ-D3m274TuIAxs3-uHtgWp0Z5Uj_t1X2z93V8-6eIJ?type=png)](https://mermaid.live/edit#pako:eNqdVNuO2jAQ_RXLK8QuDYjcSOxq-7Bc3vZpV31os6pMYoPVYCPHaKEsH9L-yX7V_kKdkBACVEL1k2fmnJlx5mS2MJYJhRh2u91IaK5TisFEKpBKuQQJJzNFFpEooq3WNhKgPFxwjcGRIz9tPacL2sagPSUZbVuXol-J4mSa0qx9Tl8qviBqM5SpVHmWmzEaB-PgLFGJe6ZrXWP7xfkX9kGqhKoaPbwITrmgNWYSPjgOOgNlNJYiafSJbOSi4fmDqdK8AWSMtZugXW2W112rFQmWytd4TpQGzyPjFmZKP0ji2mhgs--g01mDe2B3OuDlNAi63S97z9RmKCaJVyEq-_bW8JmZMTdTBIqIGf14_73-eP9j8t3dncLrhHTgUOQwPxINMwe85Xp5u1y3wuVtm2kIbarxfbWXU0xdLPBcBzEvrBCVvX_8p3vgHPOraNHLhAuSAkWzVarLntz-NE6Ic-ipso97Wh96yrUOnvTGqDQScUqybEQZyKfONZd5csbTFN8wn9oxtTKt5E-Kb1zXLe_dV57oOXaW68-XEvwfna1E3CzPwj4KruYXv3TJJEmMplczjY4XvK47mUy80ehq9pKYHUJNjivpNftE2QllxIy0GT3INH9eM3QQ1UXiQTIXo5VAjqLQggvzIQhPzL4sVlcEi5UWQWyuJTCCkdgZKFlp-bQRMcRaragFlVzN5hAzkmbGWi0Toulov18ryJKIb1IemxBv4Rpix0e90PZD33f80A0827PgBmKv33MD3wuQ6wch8tBgZ8FfRYJ-D3m274TuIAxs3-uHtgWp0Z5Uj_t1X2z93V8-6eIJ)

#### 3. While Nodes

``` python
code = """
k = 10
while k > 4: 
    #> Decrease k
    k = k -1
#> Final result
print(k)
"""
mermaid_diagram = code_to_mermaid(code, "While loop diagram")
```

[![](https://mermaid.ink/img/pako:eNqdVO1u2jAUfRXLFaJFSRXn257WHy3l33612qQt02QSp1gYGzlGLaM8SPcmfaq-wpyQQClMQvMv33vPObZ1j-8K5qpgkEDXdTNpuBGMgG8TLhgQSs1BwemDprNMNvVeb5VJ0C4uuSHgXaJefTNhM9YnoD-mFes7x6pfqeZ0LFjVP6TPNZ9RvbxRQula5ewW3ya3yYFQi7tnT2aH9Zr1L-y10gXTO_TNUbDgku0wo_Ta9_EBqGK5ksXePTHCAb45fDDThu8By7Ls74PWu7Ddrnu9TJZCPeYTqg24H9q0tH36hdM4TsIk_gEGgyn4DJA3GICfH6vAda82GUpDz_fitEN08fm5FXhs2jwFVyC0KhcXH0G1zPOQ5ZrZVoLp86Y6jhEqEC46dBd3V5oCF72_VFdv1EZcUgE0qxbCdHpeSqM4Rlt8G9d6tnPSvL2-TN9e_2w0aw-CO7O07slkLmhVDVkJ6m5ww1UtXnIhyFkZMZQzpzJaTRk5C4Kg3buPvDAT4s-fPh0T-D96uZD5_vFl6uHkZH7z1VomLXI8Pplp_TXju3NHo1E4HJ7MnlP7t5nVOJG-Y38wXMFKalu6X936qH7efmlriqPEzgLvqtCBM_tUygs7q5qhkcFmmGSQ2G0LzGAm1xZKF0bdLWUOidEL5kCtFg8TSEoqKhst5gU1bLiZbNvsnMrvSs06ig0hWcEnSPwIX6YoSqPIj9IgCVHowCUkoXcZJFGY4CBKUhzieO3A342Ad4lDFPkWizFKUBimDmTWXkp_2czaZuSu_wJ_1q6C?type=png)](https://mermaid.live/edit#pako:eNqdVO1u2jAUfRXLFaJFSRXn257WHy3l33612qQt02QSp1gYGzlGLaM8SPcmfaq-wpyQQClMQvMv33vPObZ1j-8K5qpgkEDXdTNpuBGMgG8TLhgQSs1BwemDprNMNvVeb5VJ0C4uuSHgXaJefTNhM9YnoD-mFes7x6pfqeZ0LFjVP6TPNZ9RvbxRQula5ewW3ya3yYFQi7tnT2aH9Zr1L-y10gXTO_TNUbDgku0wo_Ta9_EBqGK5ksXePTHCAb45fDDThu8By7Ls74PWu7Ddrnu9TJZCPeYTqg24H9q0tH36hdM4TsIk_gEGgyn4DJA3GICfH6vAda82GUpDz_fitEN08fm5FXhs2jwFVyC0KhcXH0G1zPOQ5ZrZVoLp86Y6jhEqEC46dBd3V5oCF72_VFdv1EZcUgE0qxbCdHpeSqM4Rlt8G9d6tnPSvL2-TN9e_2w0aw-CO7O07slkLmhVDVkJ6m5ww1UtXnIhyFkZMZQzpzJaTRk5C4Kg3buPvDAT4s-fPh0T-D96uZD5_vFl6uHkZH7z1VomLXI8Pplp_TXju3NHo1E4HJ7MnlP7t5nVOJG-Y38wXMFKalu6X936qH7efmlriqPEzgLvqtCBM_tUygs7q5qhkcFmmGSQ2G0LzGAm1xZKF0bdLWUOidEL5kCtFg8TSEoqKhst5gU1bLiZbNvsnMrvSs06ig0hWcEnSPwIX6YoSqPIj9IgCVHowCUkoXcZJFGY4CBKUhzieO3A342Ad4lDFPkWizFKUBimDmTWXkp_2czaZuSu_wJ_1q6C)

4. Function Nodes

``` python
code = """
def forward(self, x):
    x = self.conv1(x)
    x = self.conv2(x)
    x = self.conv3(x)    
    return x
"""
mermaid_diagram = code_to_mermaid(code, "Function diagram")
```
[![](https://mermaid.ink/img/pako:eNqdVO1u2jAUfRXLFWKLAspnE2fapLbAr1Wa2mo_VleVSexiLdjIcVYY4kG2N-lT9RVmQkJGySQ0__K995xz7fjkrmEqMwoTOBgMsNBc5zQBk1KkmksBMk6eFJljUVV7vTUWoF5ccJ2AvxLb1dczOqf9BPSnpKB9u6v6lShOpjkt-sf0heJzolZXMpdqq3I2RuNoHB0J1bg7utQt1qnWv7CXUmVUteirTnDOBW0xk_jS89ARqKCpFNnBOZGLfHR1fGGqND8AMsb6h6BNG9bbTa-HBcvlczojSoO7kUkL80qPbhbH1E-n98CyluAjKGjOhuYsP9zXl1_L15fflgUe3oLBYPBpl0mDcxoFkdcgmvhIzuuQa8Ct3DkLwoh4foNo4iM5v0OuAbdyzpSQ2PFYg2jid_eWpagulQBLy3p4jwUWRTk1vlzMwJeLm4vr8d345haLjCu6s-3nGywWxBj30dmyaxoVGRYtoe3cfKmtcq8HbvXKuBOLNCdFMaIMbF-bb4VJDhjP8-SMhdRNqV1oJb_T5Mz3_Xo_eOaZniXeYvmhS-D_6Kz-Hdv2LHZQdDI_l3LRMEmWounJTOPfOW_7TiaTYDQ6mV09ATUaJ9Jb9hsHZ5SRMteH1b0hO6t7f3VWG2_tL7gv17Zpz24q0IZzgyM8M3OyGlkYVqMMw8Rs6w4YYrExUFJqebsSKUy0KqkNlSyfZjBhJC9MVC4youloN1f32QUR36ScNxQTwmQNlzDxQjSM3TAOQy-M_ShwAxuuYBI4Qz8Kgwj5YRSjAJ1vbPizEnCGKHBDz2ARciM3CGIbUmM-qa53c74a95s_XunieQ?type=png)](https://mermaid.live/edit#pako:eNqdVO1u2jAUfRXLFWKLAspnE2fapLbAr1Wa2mo_VleVSexiLdjIcVYY4kG2N-lT9RVmQkJGySQ0__K995xz7fjkrmEqMwoTOBgMsNBc5zQBk1KkmksBMk6eFJljUVV7vTUWoF5ccJ2AvxLb1dczOqf9BPSnpKB9u6v6lShOpjkt-sf0heJzolZXMpdqq3I2RuNoHB0J1bg7utQt1qnWv7CXUmVUteirTnDOBW0xk_jS89ARqKCpFNnBOZGLfHR1fGGqND8AMsb6h6BNG9bbTa-HBcvlczojSoO7kUkL80qPbhbH1E-n98CyluAjKGjOhuYsP9zXl1_L15fflgUe3oLBYPBpl0mDcxoFkdcgmvhIzuuQa8Ct3DkLwoh4foNo4iM5v0OuAbdyzpSQ2PFYg2jid_eWpagulQBLy3p4jwUWRTk1vlzMwJeLm4vr8d345haLjCu6s-3nGywWxBj30dmyaxoVGRYtoe3cfKmtcq8HbvXKuBOLNCdFMaIMbF-bb4VJDhjP8-SMhdRNqV1oJb_T5Mz3_Xo_eOaZniXeYvmhS-D_6Kz-Hdv2LHZQdDI_l3LRMEmWounJTOPfOW_7TiaTYDQ6mV09ATUaJ9Jb9hsHZ5SRMteH1b0hO6t7f3VWG2_tL7gv17Zpz24q0IZzgyM8M3OyGlkYVqMMw8Rs6w4YYrExUFJqebsSKUy0KqkNlSyfZjBhJC9MVC4youloN1f32QUR36ScNxQTwmQNlzDxQjSM3TAOQy-M_ShwAxuuYBI4Qz8Kgwj5YRSjAJ1vbPizEnCGKHBDz2ARciM3CGIbUmM-qa53c74a95s_XunieQ)

You can suppress `self.` in nodes

``` python
code = """
def forward(self, x):
    x = self.conv1(x)
    x = self.conv2(x)
    #> Final conv
    x = self.conv3(x)    
    return x
"""
mermaid_diagram = code_to_mermaid(
    code, 
    "Function diagram without self", 
    remove_self=True
)
```

[![](https://mermaid.ink/img/pako:eNqdlN9O2zAYxV_FMqq6RSlq_pE40yYBba9AmgDtYhghN3aotdSuHGe0gz7I9iY8Fa8wJ00aSjOpmq9sf79zbDen3xNMJGUwhoPBAAvNdcZiMClEorkUgHLyoMgcPHI9k4UGOctSLCq013vCAtSDC65j8GajHH09Y3PWj0F_SnLWt7uq34jiZJqxvL8vXyg-J2p1LjOpSpejMRqH43DPqOZu2FK37LAa_2LPpKJMtfR5J5xxwVpmEp25LtqDcpZIQXfuiRzkofP9BzOl-Q6Ypml_F1q3y3q67vWwSDP5mMyI0uBmZLaF-WT3CUv8gJ2kt8CyluAzAOYeP53Xl9_L15c_lgXu3oNgMPiy2UEhJX7Ihg3RrHes3A6rBiytnidckKxCnzfVqc-cyAn9hm7WO7Zeh20Dtjd0kOtOI0oaoll_uLUsxXShBFha1t1HLLDIi6kJ6WIGvp5enV6Ob8ZX11hQrtgmwxdXWCyISfH9sFTXMiYoFq2gPbn5tUrnXg9c65VJJxZJRvJ8xNLyDZSXxubtKc-y-CgNmJMwO9dK_mDxked59XzwyKmexe5i-anL4P_kaf3fbI9PoyEKD9ZnUi4aJaEJmh6sNPmd8_bcyWTij0YHq6tPwIzHgfJW_S7FlKWkyPRudRvMzuo2X53VJlvbB27LdWzau5sKtOHccIRT0zSrloVh1cowjM20PgFDLNYGJYWW1yuRwFirgtlQyeJhBuOUZLlZFQtKNBttmmyDLIj4LuXbJYyf4BLGboCOIyeIgsANIi_0Hd-GKxj7w2MvDPwQeUEYIR-drG34qzIYHiPfCVzDIuSEju-HNmQme1Jdbnp-1frXfwEw_efG?type=png)](https://mermaid.live/edit#pako:eNqdlN9O2zAYxV_FMqq6RSlq_pE40yYBba9AmgDtYhghN3aotdSuHGe0gz7I9iY8Fa8wJ00aSjOpmq9sf79zbDen3xNMJGUwhoPBAAvNdcZiMClEorkUgHLyoMgcPHI9k4UGOctSLCq013vCAtSDC65j8GajHH09Y3PWj0F_SnLWt7uq34jiZJqxvL8vXyg-J2p1LjOpSpejMRqH43DPqOZu2FK37LAa_2LPpKJMtfR5J5xxwVpmEp25LtqDcpZIQXfuiRzkofP9BzOl-Q6Ypml_F1q3y3q67vWwSDP5mMyI0uBmZLaF-WT3CUv8gJ2kt8CyluAzAOYeP53Xl9_L15c_lgXu3oNgMPiy2UEhJX7Ihg3RrHes3A6rBiytnidckKxCnzfVqc-cyAn9hm7WO7Zeh20Dtjd0kOtOI0oaoll_uLUsxXShBFha1t1HLLDIi6kJ6WIGvp5enV6Ob8ZX11hQrtgmwxdXWCyISfH9sFTXMiYoFq2gPbn5tUrnXg9c65VJJxZJRvJ8xNLyDZSXxubtKc-y-CgNmJMwO9dK_mDxked59XzwyKmexe5i-anL4P_kaf3fbI9PoyEKD9ZnUi4aJaEJmh6sNPmd8_bcyWTij0YHq6tPwIzHgfJW_S7FlKWkyPRudRvMzuo2X53VJlvbB27LdWzau5sKtOHccIRT0zSrloVh1cowjM20PgFDLNYGJYWW1yuRwFirgtlQyeJhBuOUZLlZFQtKNBttmmyDLIj4LuXbJYyf4BLGboCOIyeIgsANIi_0Hd-GKxj7w2MvDPwQeUEYIR-drG34qzIYHiPfCVzDIuSEju-HNmQme1Jdbnp-1frXfwEw_efG)

5. Diagram orientation

``` python
code = """
def forward(self, x_tensor):
    x_tensor = F.tanh(x_tensor)   
    return x_tensor
"""
mermaid_diagram = code_to_mermaid(
    code, 
    "Diagram orientation", 
    orientation="LR",
)
```

[![](https://mermaid.ink/img/pako:eNqdVG2O2jAQvYrlFUobBRQIAeyqK-3y8asrVbDqjzYVMslksRrsyHG0UMRB2pvsqfYKdQIhZaES6vzyjN97ntgvs8WhjABT3Gw2A6G5ToCiEWdPiq2QVByEZppLEYgS0GhsA4EOwQXXFP1VKMLSS1iBRZG1YBlYzqXdL0xxtkggs87pqeIrpjZDmUhVqNyMybg_7p8JHXCPsNY11i3jX9h7qSJQNXp4EZxwATVmMrjvdMgZKINQiuikT9ImHhmefzAozU-AcRxbp6BdnR6Wu0YjEHEin8MlUxp9mpqyMA81b5MQugPWu7Xt9VyDyKRCH9GkpZlYvr78qmqvL79t-_tbEmo2b_cVEro-LMigQlT5u2-2rUDnSqBKyui8D8z7Z_nCmCJdos9307uH8eN4OgtExBWEhT_KFlNmXDN3C5FTNogoEDWv7qPqrDig0UAzvTGuCESYsCwbQYyKW-aFPktQzJOE3sQ-tENwMq3kD6A3nucd1s1nHukl7aTrD5cE_o8e5yI8PT4euKR_NT-RMq2YLArJ4mqm8c2K1-dOJpPuaHQ1u3wJMBpX0mv2G8fUF3AKqAxz7PO4fTBB3YLZwQ5eGRzjkZk05R8f4HISBJiaZQQxyxMd4EDsDJTlWs42IsRUqxwcrGT-tMQ0ZklmsjyNmIbDiDpWUya-SrmqKCbFdIvXmLoO3mDa7pGWT_xetzcgXr_d9gY7B_8sCW6L7KPresT3fL_jYDCekephPxnLAbn7A0XGofo?type=png)](https://mermaid.live/edit#pako:eNqdVG2O2jAQvYrlFUobBRQIAeyqK-3y8asrVbDqjzYVMslksRrsyHG0UMRB2pvsqfYKdQIhZaES6vzyjN97ntgvs8WhjABT3Gw2A6G5ToCiEWdPiq2QVByEZppLEYgS0GhsA4EOwQXXFP1VKMLSS1iBRZG1YBlYzqXdL0xxtkggs87pqeIrpjZDmUhVqNyMybg_7p8JHXCPsNY11i3jX9h7qSJQNXp4EZxwATVmMrjvdMgZKINQiuikT9ImHhmefzAozU-AcRxbp6BdnR6Wu0YjEHEin8MlUxp9mpqyMA81b5MQugPWu7Xt9VyDyKRCH9GkpZlYvr78qmqvL79t-_tbEmo2b_cVEro-LMigQlT5u2-2rUDnSqBKyui8D8z7Z_nCmCJdos9307uH8eN4OgtExBWEhT_KFlNmXDN3C5FTNogoEDWv7qPqrDig0UAzvTGuCESYsCwbQYyKW-aFPktQzJOE3sQ-tENwMq3kD6A3nucd1s1nHukl7aTrD5cE_o8e5yI8PT4euKR_NT-RMq2YLArJ4mqm8c2K1-dOJpPuaHQ1u3wJMBpX0mv2G8fUF3AKqAxz7PO4fTBB3YLZwQ5eGRzjkZk05R8f4HISBJiaZQQxyxMd4EDsDJTlWs42IsRUqxwcrGT-tMQ0ZklmsjyNmIbDiDpWUya-SrmqKCbFdIvXmLoO3mDa7pGWT_xetzcgXr_d9gY7B_8sCW6L7KPresT3fL_jYDCekephPxnLAbn7A0XGofo)

6. Full Diagram

``` python
code = """
def myfunc(self, x: Tensor):
    x = self.conv1(x)
    #> Func call
    x = F.softmax(x)    
    if x > 10:  #> Check threshold
        print("Greater than 10")  
    elif x < 5:
        print("Less than 5")
    else:
        print("Between 5 and 10")
    for i in range(10):
        print(i)    
        i += 1
    z = x + 1
    while z < 10:
        z += 1
    #> Final result
    return z
"""
mermaid_diagram = code_to_mermaid(
    code, 
    "Complete Flowchart", 
    "TB", 
    True
)
```

[![](https://mermaid.ink/img/pako:eNqdVu1u2zYUfRVCgeHUtQ19f3UN0MTx_rTAkAT7saooaOkyJiZTBiU3zoeBvcb2IAP6OnuBvsIoWaQsWR6C6Zeu7rmHR5fkIZ-1OEtAC7XJZBKxghYphOgqW61TKADN0-whXmJeRKzKDwbPEUP1QxktQnTwoXyGxRJWMAzRcIFzGI77sr9iTvEihXx4XL7mdIX541WWZrxkObsOrr1r74ioxt3BtmiwevWcwl5mPAHeoK96wSll0GDm_qVpBkegHOKMJS2dgRFYwdXxDwMvaAtICBm2QbsmrF93g0HEiGw-ursUn5mYp68x2LHrBM5nNBpt0XuEhI5vxo_vf25_fP9rNEJfukA0mVy8zDcsRjFO05d9EhJDT_TElGAZX-xJ59M8I8UKbxXvly6ypN1_cV0vxo6ZSISMn4XCGcQ0pxkTwnbdfMNgWpZh6gn5D4SduLHvLU4jLMsE28auREjO51IGJWiLLpChlzp2XUhD4vkLYsQklggZl80Wa4gVoh___PH3zxywmFZULDETpOJLp_eyrmH2A2KL1qkfkD9UyYO0EvgTctr6akzDonuBbbqWIxEy7uj7CHm-F-cca5M1p7XJVtbacmipktmmXvB5xsL1JULGHVWXUDwACE0Is6S3bbLwtDQZn58LbpJxRIUJIY7ZPYhBDH1P-OZNF38wxbobm4EOaqrq-FAs7U5njWlYFrrjJp6nVqyMSxaK3r5HxmG9zDb1sCCxY-u62lV1XNY_iQ24RW_bFBLQUDi-6RoGqLUq46o1D0uaAnoSS6pa801DJOpg9izXx7qjeGS8l9L9FZnduwplOEUc8k1a1MZiESI2pqfWgozPP49GHIoNZ-hJuInQ0-nMVPClWbZ-6U58Z9gOrulCxPLN4p7j9RL98uHmw6fru-ub24gllENcCAtCH28itsYcr77qpZrtXgYwYVxNQdMX6Z8l82CAbotHcV5FLE5xns-AlL6b0JJYtIDQNA3PiANGDOO84NnvEJ5ZllW_Tx5oUixDc71910fw_8qJsPT28MTXA-_V9WUTZSVO4mDx6kphfSvajDufz-3Z7NXV1RRAaZ-vK2-qO-daAgSLhdfOquOpaU8boE6Og_lrI9SxoBDtvDL3XgHKtE9UK_vtrVbmeqJaOWRvtXK7cm47oqWF9RaqbdjfU-k9vVnlKMeDql3b_6-1Naj1pNL1Lm2WyrtyE2pjbSWQmCbislrdGiOtuk1GWihe6zEiLWI7AcWbIrt9ZLEWFnwDY41nm_ulFhIszrOxtlkn4gSfUSwMYyUha8x-y7LDUAufta0WGpY99W3H8QIv0E3PN5yx9qiFEytwp2KpmHbgG5ZIBe5urD1VFMbUcxzD9kzD93TbNC13rIGY0Yx_2t-2q0v37l_ztq64?type=png)](https://mermaid.live/edit#pako:eNqdVu1u2zYUfRVCgeHUtQ19f3UN0MTx_rTAkAT7saooaOkyJiZTBiU3zoeBvcb2IAP6OnuBvsIoWaQsWR6C6Zeu7rmHR5fkIZ-1OEtAC7XJZBKxghYphOgqW61TKADN0-whXmJeRKzKDwbPEUP1QxktQnTwoXyGxRJWMAzRcIFzGI77sr9iTvEihXx4XL7mdIX541WWZrxkObsOrr1r74ioxt3BtmiwevWcwl5mPAHeoK96wSll0GDm_qVpBkegHOKMJS2dgRFYwdXxDwMvaAtICBm2QbsmrF93g0HEiGw-ursUn5mYp68x2LHrBM5nNBpt0XuEhI5vxo_vf25_fP9rNEJfukA0mVy8zDcsRjFO05d9EhJDT_TElGAZX-xJ59M8I8UKbxXvly6ypN1_cV0vxo6ZSISMn4XCGcQ0pxkTwnbdfMNgWpZh6gn5D4SduLHvLU4jLMsE28auREjO51IGJWiLLpChlzp2XUhD4vkLYsQklggZl80Wa4gVoh___PH3zxywmFZULDETpOJLp_eyrmH2A2KL1qkfkD9UyYO0EvgTctr6akzDonuBbbqWIxEy7uj7CHm-F-cca5M1p7XJVtbacmipktmmXvB5xsL1JULGHVWXUDwACE0Is6S3bbLwtDQZn58LbpJxRIUJIY7ZPYhBDH1P-OZNF38wxbobm4EOaqrq-FAs7U5njWlYFrrjJp6nVqyMSxaK3r5HxmG9zDb1sCCxY-u62lV1XNY_iQ24RW_bFBLQUDi-6RoGqLUq46o1D0uaAnoSS6pa801DJOpg9izXx7qjeGS8l9L9FZnduwplOEUc8k1a1MZiESI2pqfWgozPP49GHIoNZ-hJuInQ0-nMVPClWbZ-6U58Z9gOrulCxPLN4p7j9RL98uHmw6fru-ub24gllENcCAtCH28itsYcr77qpZrtXgYwYVxNQdMX6Z8l82CAbotHcV5FLE5xns-AlL6b0JJYtIDQNA3PiANGDOO84NnvEJ5ZllW_Tx5oUixDc71910fw_8qJsPT28MTXA-_V9WUTZSVO4mDx6kphfSvajDufz-3Z7NXV1RRAaZ-vK2-qO-daAgSLhdfOquOpaU8boE6Og_lrI9SxoBDtvDL3XgHKtE9UK_vtrVbmeqJaOWRvtXK7cm47oqWF9RaqbdjfU-k9vVnlKMeDql3b_6-1Naj1pNL1Lm2WyrtyE2pjbSWQmCbislrdGiOtuk1GWihe6zEiLWI7AcWbIrt9ZLEWFnwDY41nm_ulFhIszrOxtlkn4gSfUSwMYyUha8x-y7LDUAufta0WGpY99W3H8QIv0E3PN5yx9qiFEytwp2KpmHbgG5ZIBe5urD1VFMbUcxzD9kzD93TbNC13rIGY0Yx_2t-2q0v37l_ztq64)

### Change the style

**code2mermaid** use a color palette pre-defined. But through the `_node_style` parameter you can change it.

To check the default style:

``` python
from code2mermaid.style import node_style
print(node_style)
```

## Acknowledgments

**code2mermaid** was developed using 3.5 Sonnet. Thanks to Anthropic for making it available free via Claude.