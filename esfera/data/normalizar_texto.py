import numpy as np

data = np.loadtxt('/home/aye/Escritorio/hoy/krey/esfera/data/231640.txt')

text = pd.read_csv(data, header=None, error_bad_lines=False)

data_normalized = (data - data.min()) / (data.max() - data.min())
