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
    # ดึงอินพุตจากตัวแปรสภาพแวดล้อม (กำหนดโดย GitHub Actions)
    material = os.getenv("MATERIAL", "steel")
    thickness = float(os.getenv("THICKNESS", "5"))
    design = os.getenv("DESIGN", "logo.png")
    output = os.getenv("OUTPUT", "finished_product")
    
    result = simulate_laser_task(material, thickness, design, output)
    print("Task Result:", result)
