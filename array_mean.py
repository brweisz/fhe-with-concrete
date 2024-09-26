from concrete import fhe
import numpy as np

numeros_permitidos = fhe.LookupTable([3,7,11])

@fhe.compiler({"array": "encrypted"})
def mean_of_array(array):
    return np.round(np.sum(array) / array.size).astype(np.int64)

inputset = [np.random.randint(0, 16, size=10) for _ in range(10)]
circuit = mean_of_array.compile(inputset)

sample = np.array([10,10,10,10,10,10,10,10,10,10])
expected_output = 10
actual_output = circuit.encrypt_run_decrypt(sample)

assert expected_output == actual_output
