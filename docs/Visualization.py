'''
Function:
	Visualization the test results while training
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import re
import matplotlib.pyplot as plt


f = open('train.log', 'r')
contents = f.read()
results = re.findall(r'loss is (.*?)\.\.\.', contents)
batches = []
losses = []
for idx, result in enumerate(results):
	batches.append(idx)
	losses.append(float(result))
plt.title('Loss vary according to batch of train')
plt.xlabel('batch')
plt.ylabel('loss')
plt.plot(batches, losses, 'b')
plt.savefig('vis.jpg')
plt.show()