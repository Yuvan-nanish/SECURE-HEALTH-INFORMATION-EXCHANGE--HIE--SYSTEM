from tinyec import registry

# Access the registry to list available curves
curve_names = registry.get_curve_names()
print("Available curves:")
for curve_name in curve_names:
    print(curve_name)
