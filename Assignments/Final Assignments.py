"""
Author : Anson Tang
Student Number: 1003487
Revison date : 16 Jan 2025
Program : Credit Card Report
Description : Report of all credit cards in the customer database that have expired.

VARIABLE DICTIONARY :
    filename: str - Name of the input file (data.dat)
    f: file object - File handle for input file
    lines: list - List of all lines from input file
    names: list - List of customer full names (first + last)
    cc_nums: list - List of credit card numbers
    cc_types: list - List of credit card types (Visa/MasterCard)
    expiry_dates: list - List of expiry dates in YYYYMM format
    parts: list - Temporary storage for split line components
    given_name: str - Customer's first name
    surname: str - Customer's last name
    cc_type: str - Credit card type from record
    cc_number: str - Credit card number from record
    exp_mo: str - Expiry month string
    exp_yr: str - Expiry year string
    i: int - Loop index for processing records
    status: str - Card status (EXPIRED/RENEW IMMEDIATELY)
    name_display: str - Formatted name with colon
    expiry_str: str - String representation of expiry date
    out_line: str - Formatted output line
    out_file: file object - Output file handle
"""

def mergeSort(arr, arr2, arr3, arr4, l, r):
    """Sort arrays using merge sort algorithm"""
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)

def merge(arr, arr2, arr3, arr4, l, m, r):
    """Merge two sorted subarrays"""
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

# Main program
if __name__ == "__main__":
    # Open and read input file
    filename = "data.dat"
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Remove header line
    if lines:
        lines.pop(0)
    
    # Initialize data storage lists
    names = []
    cc_nums = []
    cc_types = []
    expiry_dates = []
    
    # Process each record line
    for line in lines:
        # Split line into components
        parts = line.strip().split(',')
        if len(parts) < 6:
            continue
            
        # Extract and clean fields
        given_name = parts[0].strip()
        surname = parts[1].strip()
        cc_type = parts[2].strip()
        cc_number = parts[3].strip()
        exp_mo = parts[4].strip()
        exp_yr = parts[5].strip()
        
        # Store formatted name
        names.append(f"{given_name} {surname}")
        
        # Store credit card details
        cc_types.append(cc_type)
        cc_nums.append(cc_number)
        
        # Format expiry date as YYYYMM integer
        if len(exp_mo) == 1:
            exp_mo = '0' + exp_mo
        expiry_dates.append(int(exp_yr + exp_mo))
    
    # Sort all data by expiry date
    if expiry_dates:
        mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates)-1)
    
    # Generate report with clean, minimal output
    with open("output.txt", "w") as out_file:
        for i in range(len(expiry_dates)):
            # Skip cards after June 2025
            if expiry_dates[i] > 202506:
                continue
                
            # Determine card status
            if expiry_dates[i] < 202406:  # Before June 2024
                status = "EXPIRED"
            else:  # June 2024 to June 2025
                status = "RENEW IMMEDIATELY"
            
            # Prepare formatted components
            name_display = names[i] + ':'
            expiry_str = str(expiry_dates[i])
            
            # Create output line matching assignment example
            out_line = f"{name_display:<20} {cc_types[i]:<12} #{cc_nums[i]} {expiry_str} {status}"
            
            # Write to file and print to console
            print(out_line)
            out_file.write(out_line + "\n")
    
    # Final confirmation
    print("\nReport generated successfully. Output saved to output.txt")
