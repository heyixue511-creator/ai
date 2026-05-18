import os
import re
from pdfminer.high_level import extract_text
from pathlib import Path

def sanitize_filename(filename):
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filename = filename.replace('.pdf', '')
    return filename

def convert_pdf_to_markdown(pdf_path, output_dir):
    try:
        text = extract_text(pdf_path)
        
        markdown_content = f"# {sanitize_filename(os.path.basename(pdf_path))}\n\n{text}"
        
        output_filename = sanitize_filename(os.path.basename(pdf_path)) + '.md'
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✓ 已转换: {os.path.basename(pdf_path)}")
        return True
    except Exception as e:
        print(f"✗ 转换失败 {os.path.basename(pdf_path)}: {str(e)}")
        return False

def main():
    base_dir = r"c:\Users\lenovo\Desktop\人工智能辅助下当代艺术史文献计量分析方法研究"
    pdf_dir = base_dir
    output_dir = os.path.join(base_dir, "markdown文件")
    
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_files = list(Path(pdf_dir).glob("*.pdf"))
    
    if not pdf_files:
        print("未找到PDF文件")
        return
    
    print(f"找到 {len(pdf_files)} 个PDF文件，开始转换...\n")
    
    success_count = 0
    for pdf_file in pdf_files:
        if convert_pdf_to_markdown(str(pdf_file), output_dir):
            success_count += 1
    
    print(f"\n转换完成！成功: {success_count}/{len(pdf_files)}")

if __name__ == "__main__":
    main()
