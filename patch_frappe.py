#!/usr/bin/env python3
import sys

file_path = '/home/chinhlt/frappe-bench/apps/frappe/frappe/__init__.py'

with open(file_path, 'r') as f:
    lines = f.readlines()

# Line 282 (index 281)
old_line = lines[281]
new_line = old_line.replace(
    'user=local.conf.db_name or db_name,',
    'user=local.conf.get("db_user") or local.conf.db_name or db_name,'
)

lines[281] = new_line

with open(file_path, 'w') as f:
    f.writelines(lines)

print('✅ Patched successfully!')
print(f'Old: {old_line.strip()}')
print(f'New: {new_line.strip()}')
