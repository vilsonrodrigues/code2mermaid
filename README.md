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
[![](https://mermaid.ink/img/pako:eNqdVO1u2jAUfRXLCNEiUsUhkMTT-qOl_NuvVpu0ZZqcxC4WxkaOUWHAg3Rv0qfqK8wJScPXJDT_8r33nJNr3ZO7hqnKKMTQcZxYGm4ExeDbhAsKhFJzkHHyrMkslmW93V7HElSHS24w2EsUp2MmdEY7GHQSktNO71z1K9GcJILmnVP6XPMZ0at7JZQuVFoP0UPwEJwIVbgnujQN1i3Pv7B3SmdUN-j7s2DBJW0w4_DO86ITUE5TJbODPiMU9aP70wdTbfgBkDHWOQRtm7C6btvtWDKhXtIJ0QY8jWxa2jn9yjLGBkni_wDd7hR8BsjtdsHP4ypwnNtdhoWJO0CJXyPq-OrKCryUY56CW-BblevrY1AhsxnRVFM7SjDdVNUhSwkKog90FdctTYGD9puq66XamEsigKb5Qphaz3VpgsKmxSou9OzkpHl_e52-v_3ZaR5J3ljNwqeb4-cWXgWPZmVdFstUkDwfUQaKqXHDVdEE40LgFhtQlNJebrSaUtzq9_vV3XnhmZlgb778dE7g_-hsIdPDz7PQjYKL-eUvWTFJlkbJxUzrwxlvvjsej_3R6GL2nNgdQK3GhfSGfWTMjDJiR39Y_fBb8byjUj3p88TKKntV2IMz-1TCM7vTyuUSw3LpxBDbawWMYSy3FkoWRj2uZAqx0Qvag1otnicQMyJyGy3mGTF0tNuANWRO5Hel9kOI13AJMfIGN2EUBCHyg0HoRcNhD64gHtqsH6DQ9UIX-QPX3_bg71IA3fRdzwtCD_U9fxiWBGrdpfSX3UouN_P2LyY_wKs?type=png)](https://mermaid.live/edit#pako:eNqdVO1u2jAUfRXLCNEiUsUhkMTT-qOl_NuvVpu0ZZqcxC4WxkaOUWHAg3Rv0qfqK8wJScPXJDT_8r33nJNr3ZO7hqnKKMTQcZxYGm4ExeDbhAsKhFJzkHHyrMkslmW93V7HElSHS24w2EsUp2MmdEY7GHQSktNO71z1K9GcJILmnVP6XPMZ0at7JZQuVFoP0UPwEJwIVbgnujQN1i3Pv7B3SmdUN-j7s2DBJW0w4_DO86ITUE5TJbODPiMU9aP70wdTbfgBkDHWOQRtm7C6btvtWDKhXtIJ0QY8jWxa2jn9yjLGBkni_wDd7hR8BsjtdsHP4ypwnNtdhoWJO0CJXyPq-OrKCryUY56CW-BblevrY1AhsxnRVFM7SjDdVNUhSwkKog90FdctTYGD9puq66XamEsigKb5Qphaz3VpgsKmxSou9OzkpHl_e52-v_3ZaR5J3ljNwqeb4-cWXgWPZmVdFstUkDwfUQaKqXHDVdEE40LgFhtQlNJebrSaUtzq9_vV3XnhmZlgb778dE7g_-hsIdPDz7PQjYKL-eUvWTFJlkbJxUzrwxlvvjsej_3R6GL2nNgdQK3GhfSGfWTMjDJiR39Y_fBb8byjUj3p88TKKntV2IMz-1TCM7vTyuUSw3LpxBDbawWMYSy3FkoWRj2uZAqx0Qvag1otnicQMyJyGy3mGTF0tNuANWRO5Hel9kOI13AJMfIGN2EUBCHyg0HoRcNhD64gHtqsH6DQ9UIX-QPX3_bg71IA3fRdzwtCD_U9fxiWBGrdpfSX3UouN_P2LyY_wKs)

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
    #> Check thresholds
    if x > 10:         
        #> good case
        print("Greater than 10")  
    elif x < 5: 
        #> ok case
        print("Less than 5")
    else: 
        #> bad case
        print("Between 5 and 10")
    x = x + 1
    #> for loop
    for i in range(10):
        print(i)    
        i += 1
    z = x + 1
    #> While loop
    while z < 10:
        z += 1
    #> Final result
    return z
"""
mermaid_diagram = code_to_mermaid(
    code, 
    "Complete Flowchart", 
    remove_self=True
)
```

[![](https://mermaid.ink/img/pako:eNqdV2tu20YQvsqChiBHkQw-xGcbA_FD_ZMAhW20QMMgWJFDa2FqVyCpWLYjoNdoD1Ig1-kFcoUOKe5SpCjAKPWHw_m-2W9ndmdXL1okYtACbTKZhLxgRQoBuRTLVQoFkFkqHqMFzYqQV_7B4CXkpH4YZ0VA9j6Uz7BYwBKGARnOaQ7DcZ_3N5oxOk8hHx7SVxlb0uzpUqQiK6OcXPvX7rV7EKjG3cGmaLB69RzDXogshqxBX_aCU8ahwcy8C9P0D0A5RILHLZ2-4Vv-5eGEIStYC5gkybAN2jZm_bodDEKeyOSTuwv8zLFOX8DTwfPN6BMZjTbkHSGo46vx4_tfmx_f_x6NyOcukEwm599max6RiKbpt53TdFzbAseVYGmf74LOznKRFEu6UXE_d5FV2MsFRA-kWGSQL0Qa53V0sKae4US-klLbL6j5CiKWM8FR6rbrL2PuvlBjGscA5nHEnCZzI_aT4whbN3XT9XSJkDFfShksIRtyTgy91LHtQqrJ3QsRY85yqGdlmJFjU9OSYGmXlcAFxgtM1r9__vNLBhRrjlmhHOPjl05hJK9R6k8Tk-oRlQg5t0oppJXWn4ndkioxlVTxsC_U1n3PS3QlVNodoR8gz3cq7UORknNcpExvLTKHljzpreTNaSuRphWZhp2AWlK13dF3AcUjAKojlMe9mZTE4yKlLXfLhrwlxn4ICah0JiIjqRCrWqdvz51pZE8VtrZPTzFaiWXYAUlG-T2gYkPfqXvzpovfW5KuMzX0eVOZ2t6fOetWosY0UXTQfTdy1MKWdhmFkbfv2jOU3obveDa4CVWbX9ol_7kvSRJQJen3BUthP024UizQp3M1YG1XaXqs0M-4fKut1iRHovZqF3sxNhYVR9o7Wd1pSe-uvTFOU4JdaJ0WcrdiMzAdQ_UgaZ9-Go0yKNYZJ8_Y1lBPJ0tnGK93EXSG7eCaLIQ8X8_vM7pakF_f37z_eH13fXMb8phlEBXY-ciHm5CvaEaXX_RSzWYnA3gc8obQ5EU28jLyYEBuiyc8OEMepTTPryApD4CYlYExBQlL0-AkscGIYJwXmXiA4MSyrPp98sjiYhGYq81PfQH-Hz3Bs6U9fOJhMl_NL5MomTSO_Pmrmdhml6wZdzabTa-uXs2uSgBlq34dvWF3DtgYEooLr-1V52STng5dHlh79Wsj1GmkEG2_Okh6BagD4ghbdfheturfR9iq9fayVVft98q-WFa-M6xsdr1EtUl7vapL9XNlvzkcVO3pXqJsHGq1KXe9h5uFhB5trC0RR1mMN-rqahtq1ZU31AJ8rUcItZBvEUrXhbh94pEWFNkaxlom1vcLLUgoHqdjbb2K8SZxxSg2k6WErCj_Q4h9UwtetI0WmNaZYdm641mm67q679tj7UkLJrZ_5hqu4_rodXT8bcfacxXBPHN023B913MczzRMf6wB1lpkH3d_CKr_Bdv_AIfy4yA?type=png)](https://mermaid.live/edit#pako:eNqdV2tu20YQvsqChiBHkQw-xGcbA_FD_ZMAhW20QMMgWJFDa2FqVyCpWLYjoNdoD1Ig1-kFcoUOKe5SpCjAKPWHw_m-2W9ndmdXL1okYtACbTKZhLxgRQoBuRTLVQoFkFkqHqMFzYqQV_7B4CXkpH4YZ0VA9j6Uz7BYwBKGARnOaQ7DcZ_3N5oxOk8hHx7SVxlb0uzpUqQiK6OcXPvX7rV7EKjG3cGmaLB69RzDXogshqxBX_aCU8ahwcy8C9P0D0A5RILHLZ2-4Vv-5eGEIStYC5gkybAN2jZm_bodDEKeyOSTuwv8zLFOX8DTwfPN6BMZjTbkHSGo46vx4_tfmx_f_x6NyOcukEwm599max6RiKbpt53TdFzbAseVYGmf74LOznKRFEu6UXE_d5FV2MsFRA-kWGSQL0Qa53V0sKae4US-klLbL6j5CiKWM8FR6rbrL2PuvlBjGscA5nHEnCZzI_aT4whbN3XT9XSJkDFfShksIRtyTgy91LHtQqrJ3QsRY85yqGdlmJFjU9OSYGmXlcAFxgtM1r9__vNLBhRrjlmhHOPjl05hJK9R6k8Tk-oRlQg5t0oppJXWn4ndkioxlVTxsC_U1n3PS3QlVNodoR8gz3cq7UORknNcpExvLTKHljzpreTNaSuRphWZhp2AWlK13dF3AcUjAKojlMe9mZTE4yKlLXfLhrwlxn4ICah0JiIjqRCrWqdvz51pZE8VtrZPTzFaiWXYAUlG-T2gYkPfqXvzpovfW5KuMzX0eVOZ2t6fOetWosY0UXTQfTdy1MKWdhmFkbfv2jOU3obveDa4CVWbX9ol_7kvSRJQJen3BUthP024UizQp3M1YG1XaXqs0M-4fKut1iRHovZqF3sxNhYVR9o7Wd1pSe-uvTFOU4JdaJ0WcrdiMzAdQ_UgaZ9-Go0yKNYZJ8_Y1lBPJ0tnGK93EXSG7eCaLIQ8X8_vM7pakF_f37z_eH13fXMb8phlEBXY-ciHm5CvaEaXX_RSzWYnA3gc8obQ5EU28jLyYEBuiyc8OEMepTTPryApD4CYlYExBQlL0-AkscGIYJwXmXiA4MSyrPp98sjiYhGYq81PfQH-Hz3Bs6U9fOJhMl_NL5MomTSO_Pmrmdhml6wZdzabTa-uXs2uSgBlq34dvWF3DtgYEooLr-1V52STng5dHlh79Wsj1GmkEG2_Okh6BagD4ghbdfheturfR9iq9fayVVft98q-WFa-M6xsdr1EtUl7vapL9XNlvzkcVO3pXqJsHGq1KXe9h5uFhB5trC0RR1mMN-rqahtq1ZU31AJ8rUcItZBvEUrXhbh94pEWFNkaxlom1vcLLUgoHqdjbb2K8SZxxSg2k6WErCj_Q4h9UwtetI0WmNaZYdm641mm67q679tj7UkLJrZ_5hqu4_rodXT8bcfacxXBPHN023B913MczzRMf6wB1lpkH3d_CKr_Bdv_AIfy4yA)

7. Long expressions

After `0.3.0` release **code2mermaid** offers supports to long expressions. Previously long expressions were truncated by Mermaid if the len was greater than 24 characters.

``` python
code = """
x = 1
while msg.outputs.user != "ok":
    msg = self.agent_super(msg)
"""
mermaid_diagram = code_to_mermaid(code)
```

[![](https://mermaid.ink/img/pako:eNqdlE-O2jAUxq_iGqHMIIhInJA_LbMYGHZdzaiLNtXIJA5YY-zIcQQUIfUa7UEqzXV6gblCHSANASqhehH5-f2-z37JizcwFgmBIWy3NxEHh0E5VSE4WiiHoeZkQYwQGFOcE6N7KfsJS4qnjOTGuTyTdIHleiSYkKVL6yF48B68M6MD90RWqmb7u_Ev9l7IhMiaHl2EGeWkZib-vW0HZ1BOYsGTxjkDK0DB6LxgIhVtgGmaGk1oW4eH6bbdjnjKxDKeY6nA01gvc_0JngfI9qxkan0Bnc4KDIHV6YCvp0nQ693tVxDq2xhZcUVU8c2N1i_nlBGwyGemKFRWqNwsciI_TOXduyH4_f2XeNEP7X97eyqvN_B95KG-41VEFZfn085gWNrlhKUmnhGunvMiI_Lt9YfOvb3-3B8-4u02eFRr3RARjxnO8zFJQfmCqaKCYwZSyljYSl1ixaSbKyleSNhCCB3mvSVN1Dy0s9X7Swb_J08LHje3T_1-4F2tZ0JklRIncTC9WqlbZkHrfSeTiTMeX63OsMQLoj2ulNfqkyZKSIoLpprZvx1QltdMVZ_-SAi7cKGLwTTRd8fuT4_g7gaIYKinBzCCEd9qFBdKPK55DEMlC9KFUhSzOQxTzHIdFVmCFRlTPNP1VUiG-WchjkMYbuAKhnbfNW03cFzX9z0fuZbXhWsYOoHpW8hzrcCxdCn-wNl24bedQ9_0HaRJF9mDgWu7tlYQ3UBCftzffbsrcPsHu-SOLA?type=png)](https://mermaid.live/edit#pako:eNqdlE-O2jAUxq_iGqHMIIhInJA_LbMYGHZdzaiLNtXIJA5YY-zIcQQUIfUa7UEqzXV6gblCHSANASqhehH5-f2-z37JizcwFgmBIWy3NxEHh0E5VSE4WiiHoeZkQYwQGFOcE6N7KfsJS4qnjOTGuTyTdIHleiSYkKVL6yF48B68M6MD90RWqmb7u_Ev9l7IhMiaHl2EGeWkZib-vW0HZ1BOYsGTxjkDK0DB6LxgIhVtgGmaGk1oW4eH6bbdjnjKxDKeY6nA01gvc_0JngfI9qxkan0Bnc4KDIHV6YCvp0nQ693tVxDq2xhZcUVU8c2N1i_nlBGwyGemKFRWqNwsciI_TOXduyH4_f2XeNEP7X97eyqvN_B95KG-41VEFZfn085gWNrlhKUmnhGunvMiI_Lt9YfOvb3-3B8-4u02eFRr3RARjxnO8zFJQfmCqaKCYwZSyljYSl1ixaSbKyleSNhCCB3mvSVN1Dy0s9X7Swb_J08LHje3T_1-4F2tZ0JklRIncTC9WqlbZkHrfSeTiTMeX63OsMQLoj2ulNfqkyZKSIoLpprZvx1QltdMVZ_-SAi7cKGLwTTRd8fuT4_g7gaIYKinBzCCEd9qFBdKPK55DEMlC9KFUhSzOQxTzHIdFVmCFRlTPNP1VUiG-WchjkMYbuAKhnbfNW03cFzX9z0fuZbXhWsYOoHpW8hzrcCxdCn-wNl24bedQ9_0HaRJF9mDgWu7tlYQ3UBCftzffbsrcPsHu-SOLA)

### Change the style

**code2mermaid** uses a pre-defined color palette. But through the `_node_style` parameter you can change it.

To check the default style:

``` python
from code2mermaid.style import node_style
print(node_style)
```

## Acknowledgments

**code2mermaid** was developed using 3.5 Sonnet. Thanks to Anthropic for making it available free via Claude.