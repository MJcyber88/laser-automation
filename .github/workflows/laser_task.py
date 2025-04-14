import os
import json

def simulate_laser_task(material, thickness, design, output):
    print(f"Processing laser task...")
    print(f"Material: {material}, Thickness: {thickness}, Design: {design}, Output: {output}")
    
    # จำลองการตัดและสลัก
    result = {
        "status": "success",
        "material": material,
        "thickness": thickness,
        "design": design,
        "output": output,
        "message": "Laser task completed"
    }
    
    # บันทึกผลลัพธ์
    with open(output, 'w') as f:
        json.dump(result, f, indent=2)
    return result

if __name__ == "__main__":
    # กำหนดค่า (เอา task_type ออก)
    task_inputs = {
        "material": "steel",         # ค่าที่คุณต้องการส่ง
        "thickness": 5,            # ค่าที่คุณต้องการส่ง
        "design": "logo.png",        # ค่าที่คุณต้องการส่ง
        "output": "finished_product" # ค่าที่คุณต้องการส่ง
    }
    branch_ref = "main"

    # เตรียม arguments สำหรับฟังก์ชัน (ปรับตามวิธีที่คุณเรียกฟังก์ชัน)
    # ตัวอย่าง ถ้าฟังก์ชันยังรับ task_type แต่เราไม่ต้องการให้ส่งเป็น input
    run_args = {
        "task_type": None, # ส่ง None หรือค่าที่ไม่ทำให้เงื่อนไข if task_type เป็นจริงในฟังก์ชัน
        "material": task_inputs["material"],
        "thickness": task_inputs["thickness"],
        "design": task_inputs["design"],
        "output": task_inputs["output"],
        "ref": branch_ref
    }
    result = run_laser_task_with_github_actions(**run_args) # เรียกฟังก์ชัน
    print("Dispatch Result:", result)
