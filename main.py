import os

line = "Do you come here often? I take this elevator 847 times a day and still needed floors 2 through 4 just to rehearse asking."

assert 1 <= len(line) <= 199
assert "\n" not in line and "\r" not in line

output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
output_dir = os.path.dirname(output_path)
if output_dir:
    os.makedirs(output_dir, exist_ok=True)

with open(output_path, "wb") as f:
    f.write(line.encode("utf-8"))

with open(output_path, "rb") as f:
    written = f.read()

assert written == line.encode("utf-8")
assert not written.endswith(b"\n")
