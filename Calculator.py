# استيراد المكتبات
import tkinter as tk  #مكتبه ثكينتر لتوفير الوجهات الرسوميه
import math  #لتوفير دوال رياضيه مثل اجذر التربيعي

def click(button_text):       #فنكشن اسمها كلك
    current = entry.get()     # السطر ده ياخذ النص الموجود حاليا ويحفظه في المتغير
    entry.delete(0, tk.END)                                                   #   الجزء ده عشان عند الضغط  رمز او رقم يتم اضافته لشاشه العرض
    entry.insert(0, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)                    # داله لو العمليه صحيحه تطلع الناتج لو العمليه غير صحيحه تطلع خطا
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "خطأ")

def square_root():
    try:
        value = float(entry.get())     # هنا جبنا فلوت عشان الجزر  بيبقي في جذور
        result = math.sqrt(value)      # داله من مكتبه math لحساب الجزر التربيعي
        entry.delete(0, tk.END)
        entry.insert(0, str(result))          # داله تقوم بحساب الجزر التربيعي تدخل علي  try لو حدث خطا ينتقل الي except
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "خطأ")

def percentage():
    try:
        value = float(entry.get())
        result = value / 100         # هنا بيقسم علي 100 عشان يجيب النسبه المىويه
        entry.delete(0, tk.END)
        entry.insert(0, str(result))             # داله تحسب الداله المىويه
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "خطأ")

# واجهة التطبيق
root = tk.Tk()
root.title(" calculator ")

entry = tk.Entry(root, width=20, font=("Arial", 25), borderwidth=2, relief="solid", justify='left') # سينشى خانه ادخال عدد الاحرف و نوع الخط و سمك الحواف وشكلها و الخط يبدا منين
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10) # المسافات بين الازرار

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for i, row in enumerate(buttons):      # انوميريت بتلف علي عناصر القاىمه
    for j, text in enumerate(row):                   # هنا هنعمل خلقه تلف علي كل صف
        if text == '=':
            btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), bg='green', command=calculate)  # بنربطها بالداله دي عشان يطلع ال result
        else:
            btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: click(t))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

# زر المسح
clear_btn = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), bg='red' , command=clear)
clear_btn.grid(row=5, column=0, padx=6, pady=6)

# زر الجذر التربيعي
sqrt_btn = tk.Button(root, text="√", width=5, height=2, font=("Arial", 14), bg='gray' , command=square_root)
sqrt_btn.grid(row=5, column=1, padx=6, pady=6)

# زر النسبة المئوية
percent_btn = tk.Button(root, text="%", width=5, height=2, font=("Arial", 14), bg='gray' , command=percentage)
percent_btn.grid(row=5, column=2, padx=6, pady=6)

# مكان إضافي لجعل الزر الأخير يملأ المساحة (اختياري)
empty_btn = tk.Label(root, width=5, height=2)
empty_btn.grid(row=5, column=3, padx=6, pady=6)

root.mainloop()    #بدا تشغيل التطبيق

print('congratulations')
