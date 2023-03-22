import random
from collections import Counter
import matplotlib.pyplot as plt

#making the decision matrix
dec_matrix = [[0.01, 3, 800],
              [8, 1.25, 400],
              [15, 0.9, 80],
              [150,0.5,0.1]]

#making the normalised decision matrix
norm_matrix = [[0.36, 1, 0.003],
              [0.1, 0.09, 1],
               [1, 0.2, 0.04]]
rat1 = 0
rat2 = 0
rat3 = 0
rat4 = 0

cr1_w = []
cr2_w = []
cr3_w = []
cr11_w = []
cr21_w = []
cr31_w = []
cr12_w = []
cr22_w = []
cr32_w = []

for i in range(10000):
    w = [random.randint(1,10), random.randint(1,10), random.randint(1,10)]
    w_sum = w[0]+ w[1]+ w[2] #+ w[3]
    RAT_score_1 = ((w[0]/w_sum)*norm_matrix[0][0]) + ((w[1]/w_sum)*norm_matrix[0][1]) + ((w[2]/w_sum)*norm_matrix[0][2])
    RAT_score_2 = ((w[0]/w_sum)*norm_matrix[1][0]) + ((w[1]/w_sum)*norm_matrix[1][1]) + ((w[2]/w_sum)*norm_matrix[1][2])
    RAT_score_3 = ((w[0]/w_sum)*norm_matrix[2][0]) + ((w[1]/w_sum)*norm_matrix[2][1]) + ((w[2]/w_sum)*norm_matrix[2][2])

    rat_array = [RAT_score_1, RAT_score_2, RAT_score_3]
    selection = max(rat_array)
    if RAT_score_1 == selection:
        rat1 += 1
        cr1_w.append(w[0])
        cr11_w.append(w[1])
        cr12_w.append(w[2])

    if RAT_score_2 == selection:
        rat3 += 1
        cr2_w.append(w[0])
        cr21_w.append(w[1])
        cr22_w.append(w[2])

    if RAT_score_3 == selection:
        rat4 += 1
        cr3_w.append(w[0])
        cr31_w.append(w[1])
        cr32_w.append(w[2])

#counting the duplicated in the array
cr1_w.sort()
cr2_w.sort()
cr3_w.sort()
cr11_w.sort()
cr12_w.sort()
cr21_w.sort()
cr22_w.sort()
cr31_w.sort()
cr32_w.sort()

counts1 = dict(Counter(cr1_w))
counts2 = dict(Counter(cr2_w))
counts3 = dict(Counter(cr3_w))

counts4 = dict(Counter(cr11_w)) #w2
counts5 = dict(Counter(cr12_w)) #w3
counts6 = dict(Counter(cr21_w)) #w2
counts7 = dict(Counter(cr22_w)) #w3
counts8 = dict(Counter(cr31_w)) #w2
counts9 = dict(Counter(cr32_w)) #w3

dupes1 = {key:value for key, value in counts1.items() if value > 0}
dupes2 = {key:value for key, value in counts2.items() if value > 0}
dupes3 = {key:value for key, value in counts3.items() if value > -1}
dupes4 = {key:value for key, value in counts4.items() if value > -1}
dupes5 = {key:value for key, value in counts5.items() if value > -1}
dupes6 = {key:value for key, value in counts6.items() if value > -1}
dupes7 = {key:value for key, value in counts7.items() if value > -1}
dupes8 = {key:value for key, value in counts8.items() if value > -1}
dupes9 = {key:value for key, value in counts9.items() if value > -1}

#adding a 1 to dupes 7
dupes7_up = {'1' : 0}
dupes7 = {**dupes7_up, **dupes7}
#adding a 9 and a 10 to dupes 8
dupes8_up = {'9' : 0, '10' : 0}
dupes8.update((dupes8_up))





print("RAT 1 (WLAN): " + str(rat1))
print("RAT 2 (4G): " + str(rat3))
print("RAT 3 (5G): " + str(rat4))

#plotting bar chart
X = ['WLAN', '4G', '5G']
n = 10
#r = np.arange(n)
r = [1,2,3,4,5,6,7,8,9,10]
r2 = []
r3 = []
width = 0.25
for i in range(len(r)):
    r2.append(r[i] + width)
    r3.append(r[i] - width)

names_r1 = list(dupes1.keys())
values_r1 = list(dupes1.values())

names_r2 = list(dupes2.keys())
values_r2 = list(dupes2.values())

dupes3_up = {'1':0}
dupes3 = {**dupes3_up, **dupes3}

names_r3 = list(dupes3.keys())
values_r3 = list(dupes3.values())

a = values_r1
b = values_r2
c = values_r3

d = list(dupes4.values())
e = list(dupes6.values())
f = list(dupes8.values())

g = list(dupes5.values())
h = list(dupes7.values())
i = list(dupes8.values())

fontsize = 10
plt.subplot(1,3,1)
plt.bar(r, a, color = 'b', width = width, edgecolor = 'black', label = 'WLAN')
plt.bar(r2, b, color = 'g', width = width, edgecolor = 'black', label = '4G')
plt.bar(r3, c, color = 'r', width = width, edgecolor = 'black', label = '5G')
plt.title("Rat Selection Rate Relative To Weights Assigned to Download Speed (Mbps)", fontdict={'fontsize':fontsize})
plt.xlabel("Weight")
plt.ylabel("RAT selection amount")
plt.legend()

plt.subplot(1,3,2)
plt.bar(r, d, color = 'b', width = width, edgecolor = 'black', label = 'WLAN')
plt.bar(r2, e, color = 'g', width = width, edgecolor = 'black', label = '4G')
plt.bar(r3, f, color = 'r', width = width, edgecolor = 'black', label = '5G')
plt.title("Rat Selection Rate Relative To Weights Assigned to Cost per Mb", fontdict={'fontsize':fontsize})
plt.xlabel("Weight")
plt.ylabel("RAT selection amount")
plt.legend()

plt.subplot(1,3,3)
plt.bar(r, g, color = 'b', width = width, edgecolor = 'black', label = 'WLAN')
plt.bar(r2, h, color = 'g', width = width, edgecolor = 'black', label = '4G')
plt.bar(r3, i, color = 'r', width = width, edgecolor = 'black', label = '5G')
plt.title("Rat Selection Rate Relative To Weights Assigned to Coverage Range (Km)", fontdict={'fontsize':fontsize})
plt.xlabel("Weight")
plt.ylabel("RAT selection amount")
plt.legend()
plt.show()

