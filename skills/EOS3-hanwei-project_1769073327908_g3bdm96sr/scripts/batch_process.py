#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
from pathlib import Path
from analyze_image import analyze_image
import time

def batch_process(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    supported_formats = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
    image_files = [f for f in input_path.iterdir() if f.suffix.lower() in supported_formats]
    
    total = len(image_files)
    print(f'找到 {total} 张图片，开始批量处理...')
    
    results = []
    success_count = 0
    
    for idx, img_file in enumerate(image_files, 1):
        print(f'[{idx}/{total}] 处理: {img_file.name}')
        try:
            result = analyze_image(str(img_file))
            output_file = output_path / f'{img_file.stem}.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            results.append({'file': img_file.name, 'status': 'success', 'output': str(output_file)})
            success_count += 1
            print(f'  -> 成功，输出: {output_file.name}')
            time.sleep(1)
        except Exception as e:
            results.append({'file': img_file.name, 'status': 'failed', 'error': str(e)})
            print(f'  -> 失败: {str(e)}')
    
    summary = {'total': total, 'success': success_count, 'failed': total - success_count, 'results': results}
    summary_file = output_path / '_summary.json'
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f'\n批量处理完成！成功: {success_count}/{total}，汇总报告: {summary_file}')
    return summary

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('用法: python batch_process.py <输入文件夹> <输出文件夹>')
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    batch_process(input_dir, output_dir)