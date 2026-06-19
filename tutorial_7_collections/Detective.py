cctv_entiries = [
    "rahul",
    "neha",
    "amit",
    "suresh",
    "dinesh",
    "rahul",
    "neha",
    "himesh",
    "amit",
    "suresh",
    "dinesh",
    "rahul",
    "neha",
    "amit",
    "suresh",
    "dinesh",
    "rahul",
    "neha",
    "amit"
]
cctv_entiries.append("amit")
cctv_entiries.append("suresh")
cctv_entiries.append("dinesh")

print(cctv_entiries)

print("Total",len(cctv_entiries),"entries found.")

# conver list into set
unique_entries = set(cctv_entiries)
print(unique_entries)
print("Total",len(unique_entries),"suspects found.")


crime_time = (12, 35)
print("Original cirime time:",crime_time)

# time[1] = 22
# print("Modified time:",crime_time)

print(f"Crime was done at: {crime_time[0]}H:{crime_time[1]}M")


# who accessed at what time -> gate, refrigerator, swap id card


# 'rahul', 'neha', 'himesh', 'suresh', 'amit', 'dinesh'
# time should be key, name should be value -> correct 

gate_log ={"rahul": (2, 20), "neha": (1, 10)}
# gate_log['rahul'] = (2, 20)
# gate_log['neha'] = (1, 10)
gate_log['himesh'] = (12, 35)
gate_log['suresh'] = (12, 30)
gate_log['amit'] = (1, 55)
gate_log['dinesh'] = (12, 45)

# gate_log['rahul'][0] = 1
# print(gate_log['rahul'])

print("=================")
for key in gate_log:
    # print(f"Name: {key}, Entry_Time: {gate_log[key]}")
    entry_time = gate_log[key]
    if(entry_time[0]==crime_time[0] and entry_time[1]==crime_time[1]):
        print(key,"is guilty")
    # else:
    #     print(key,"is not guilty")