#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import base64
from pathlib import Path
from PIL import Image
import anthropic
import os

def get_image_info(image_path):
    with Image.open(image_path) as img:
        return {
            'width': img.width,
            'height': img.height,
            'format': img.format,
            'mode': img.mode
        }

def encode_image(image_path):
    with open(image_path, 'rb') as f:
        return base64.standard_b64encode(f.read()).decode('utf-8')

def analyze_image(image_path, api_key=None):
    if not api_key:
        api_key = os.environ.get('ANTHROPIC_API_KEY')
    
    client = anthropic.Anthropic(api_key=api_key)
    
    img_info = get_image_info(image_path)
    img_data = encode_image(image_path)
    
    file_ext = Path(image_path).suffix.lower()
    media_type_map = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp', '.gif': 'image/gif'}
    media_type = media_type_map.get(file_ext, 'image/jpeg')
    
    prompt = '''请详细分析这张图片，并以JSON格式返回分析结果。JSON结构要求：
1. 所有键名使用英文
2. 所有描述性的值使用中文
3. 包含以下维度：
   - metadata: 基础信息（尺寸、格式等）
   - visual: 视觉特征（主体、构图、色彩、光影等）
   - artistic: 艺术风格（风格、流派、技法）
   - technical: 技术参数（质量、细节、效果）
   - semantic: 语义分析（情绪、氛围、叙事）

请直接返回JSON对象，不要包含任何其他文字。'''
    
    message = client.messages.create(
        model='claude-3-5-sonnet-20241022',
        max_tokens=2048,
        messages=[{
            'role': 'user',
            'content': [
                {'type': 'image', 'source': {'type': 'base64', 'media_type': media_type, 'data': img_data}},
                {'type': 'text', 'text': prompt}
            ]
        }]
    )
    
    result_text = message.content[0].text
    result_json = json.loads(result_text)
    
    result_json['metadata']['dimensions'] = {'width': img_info['width'], 'height': img_info['height'], 'aspectRatio': f"{img_info['width']}:{img_info['height']}"}
    result_json['metadata']['format'] = img_info['format']
    result_json['metadata']['colorMode'] = img_info['mode']
    
    return result_json

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法: python analyze_image.py <图片路径> [输出JSON路径]')
        sys.exit(1)
    
    image_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        result = analyze_image(image_path)
        json_str = json.dumps(result, ensure_ascii=False, indent=2)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(json_str)
            print(f'分析完成，结果已保存到: {output_path}')
        else:
            print(json_str)
    except Exception as e:
        print(f'错误: {str(e)}', file=sys.stderr)
        sys.exit(1)