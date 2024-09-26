from concrete import fhe
import numpy as np

numeros_permitidos = fhe.LookupTable([3,7,11])

@fhe.compiler({"array": "encrypted"})
def sum_of_array(array):
    return np.sum(array)

inputset = [np.random.randint(0, 16, size=10) for _ in range(10)]
circuit = sum_of_array.compile(inputset)

sample = np.array([10,10,10,10,10,10,10,10,10,10])
expected_output = 100
actual_output = circuit.encrypt_run_decrypt(sample)

assert expected_output == actual_output
