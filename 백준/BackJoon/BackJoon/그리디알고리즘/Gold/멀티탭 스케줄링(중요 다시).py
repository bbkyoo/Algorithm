# https://jokerldg.github.io/algorithm/2021/03/21/multitap.html

n, k = map(int, input().split())
multitap = list(map(int, input().split()))

plugs = []
count = 0

for i in range(k):
    if multitap[i] in plugs:
        continue

    if len(plugs) < n:
        plugs.append(multitap[i])
        continue

    multitap_idxs = []
    isTrue = True

    for j in range(n):
        if plugs[j] in multitap[i:]:
            multitap_idx = multitap[i:].index(plugs[j])
        else:
            multitap_idx = 101
            isTrue = False

        multitap_idxs.append(multitap_idx)

        if isTrue == False:
            break

    plug_out = multitap_idxs.index(max(multitap_idxs))
    del plugs[plug_out]
    plugs.append(multitap[i])
    count += 1

print(count)