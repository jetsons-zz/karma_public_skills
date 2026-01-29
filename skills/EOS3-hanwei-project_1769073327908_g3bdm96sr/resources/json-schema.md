# JSON输出结构规范

## 顶层结构

所有分析结果包含以下顶层字段：

- metadata: 基础元数据（文件信息、尺寸等）
- visual: 视觉特征描述
- artistic: 艺术风格分析
- technical: 技术参数
- semantic: 语义和情感分析

## 字段详细定义

### metadata（元数据）
- filename: 文件名
- format: 文件格式（PNG/JPG/WEBP等）
- dimensions: 尺寸对象 {width, height, aspectRatio}
- fileSize: 文件大小（字节）
- colorMode: 色彩模式（RGB/CMYK/Grayscale）

### visual（视觉特征）
- subject: 主体对象描述（中文）
- composition: 构图方式（中文）
- colorPalette: 主要色彩数组（中文色彩名称）
- lighting: 光影描述（中文）
- depth: 景深效果（中文）
- perspective: 视角描述（中文）

### artistic（艺术风格）
- style: 整体风格（中文）
- genre: 艺术流派（中文）
- technique: 技法特点（中文）
- influences: 风格影响（中文）

### technical（技术参数）
- quality: 渲染质量评估（中文）
- detail: 细节丰富度（中文）
- effects: 后期效果列表（中文）

### semantic（语义分析）
- mood: 情绪基调（中文）
- atmosphere: 氛围描述（中文）
- narrative: 叙事性（中文）
- symbolism: 象征意义（中文，可选）