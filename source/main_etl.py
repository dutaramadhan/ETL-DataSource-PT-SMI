import transform
import load

title, result = transform.transform(r"D:\Kuliah\Kerja Praktik\Data Source\OneDrive_1_1-4-2024\UU_NO_31_1999.PDF")
print(title)
for index, res in enumerate(result):
  print(res, "\n---\n")