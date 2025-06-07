def mergeSort(arr, arr2, arr3, arr4, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)

def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    L2 = [0] * n1
    L3 = [0] * n1
    L4 = [0] * n1
    R = [0] * n2
    R2 = [0] * n2
    R3 = [0] * n2
    R4 = [0] * n2
    
    for i in range(n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]
        
    for j in range(n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]
        
    i = j = 0
    k = l
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

filename = "data.dat"
fh = open(filename, 'r')
lines = fh.readlines()
first_line = lines.pop(0)

names = []
cc_nums = []
cc_types = []
expiry_dates = []

for line in lines:
    parts = line.strip().split(',')
    if len(parts) < 6:
        continue
        
    given_name = parts[0].strip()
    surname = parts[1].strip()
    cc_type = parts[2].strip()
    cc_number = parts[3].strip()
    exp_mo = parts[4].strip()
    exp_yr = parts[5].strip()
    
    name = f"{given_name} {surname}"
    names.append(name)
    cc_types.append(cc_type)
    cc_nums.append(cc_number)
    
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo
    expiry_date = int(exp_yr + exp_mo)
    expiry_dates.append(expiry_date)

fh.close()

mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates)-1)

output_file_name = "output.txt"
with open(output_file_name, "w") as output_file:
    for i in range(len(expiry_dates)):
        if expiry_dates[i] > 202506:  # June 2025 threshold
            break
            
        if expiry_dates[i] < 202406:  # Before June 2024
            status = "EXPIRED"
        else:  # June 2024 - June 2025
            status = "RENEW IMMEDIATELY"
            
        # Format expiry date as string for proper alignment
        expiry_str = str(expiry_dates[i])
        output_line = f"{names[i] + ':':<20} {cc_types[i]:<12} #{cc_nums[i]} {expiry_str} {status}"
        print(output_line)
        output_file.write(output_line + "\n")

print(f"\nOutput sent to {output_file_name}")
