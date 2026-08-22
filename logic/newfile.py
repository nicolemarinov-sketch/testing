file_path = r"C:\Users\nicol\Downloads\secret_message.png"  # שני לנתיב הקובץ שלך

with open(file_path, "rb") as f:
    data = f.read()

# מציאת המיקום של FF D9 (סוף תמונת ה-JPG)
eoi_index = data.find(b"\xff\xd9")

if eoi_index != -1:
    jpg_data = data[: eoi_index + 2]
    extra_data = data[eoi_index + 2 :]

    # 1. שמירת התמונה הנקייה בלבד (ללא התוספות הסודיות)
    with open("cleaned_image.jpg", "wb") as f_out:
        f_out.write(jpg_data)
    print("נוצרה תמונה נקייה: cleaned_image.jpg - נסי לפתוח אותה الآن!")

    # 2. בדיקה מה מוסתר אחרי סוף התמונה
    if extra_data:
        print("\n--- נמצא מידע מוסתר אחרי סוף התמונה! ---")
        try:
            print("טקסט מפוענח:", extra_data.decode("utf-8", errors="ignore"))
        except Exception:
            print("המידע המוסתר ב-Hex:", extra_data.hex())
    else:
        print("לא נמצא מידע נוסף בתוך הקובץ לאחר ה-FF D9.")
else:
    print("לא נמצה סימון FF D9 בקובץ.")