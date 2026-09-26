import os
import zipfile

def extract_pptx_images(pptx_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with zipfile.ZipFile(pptx_path, 'r') as z:
        image_count = 0
        for filename in z.namelist():
            if filename.startswith('ppt/media/'):
                ext = os.path.splitext(filename)[1]
                target_path = os.path.join(output_dir, f"asset_{image_count}{ext}")
                with open(target_path, 'wb') as f:
                    f.write(z.read(filename))
                print(f"Extracted: {target_path}")
                image_count += 1

if __name__ == '__main__':
    extract_pptx_images(
        'input/Cypress_AYSO_154_Player_Evaluation_Slideshow_Draft.pptx',
        'extracted_assets'
    )