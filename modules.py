# import math
import math as m
from module_example import pi as pi_example
import module_example

print(m.pi)
print(pi_example)

square_value = 3
print(module_example.square(square_value))

cubed_value = module_example.cube(3)
print(cubed_value)

print(help("modules"))

import pandas as pd

df = pd.DataFrame