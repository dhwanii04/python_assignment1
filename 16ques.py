str1= "DhwaniSharma"

all_freq = {}
for i in str1:
    if i in all_freq:
        all_freq[i]+= 1
    else:
        all_freq[i]=1
print("count of all characters is :\n " +str(all_freq))
