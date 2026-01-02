from collections import ChainMap,Counter,defaultdict,OrderedDict,namedtuple,deque

# Counter - Counts the frequency of each element
data = [1, 2, 2, 3, 3, 3,4, 4, 4,5]
count = Counter(data)
print(count)
print(data[3])

# Default Dict - automatically assign a default value for missing key
d = defaultdict(int)
d["a"] += 1
print(d)

# Ordered Dict - Maintains the insertion order of keys
od = OrderedDict()
od["one"] = 1
od["two"] = 2
print(od)

# NamedTuple - Creates a tuple with named fields
Student = namedtuple("Student", ["name", "age", "marks"])
s1 = Student("CCCCC", 20, 75)
print(s1.name, s1.marks)

# Deque - fast insert/delete from both ends
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq)

# ChainMap - combines multiple dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

cm = ChainMap(d1, d2)
print(cm)
print(cm["a"])
print(cm["b"])
print(cm["c"])