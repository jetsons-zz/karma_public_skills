# Anime Character Skill

动漫角色定妆图生成 Skill，为 Claude Code 提供角色设计图生成能力。

## 功能

- 基于角色描述生成图像提示词
- 调用 Gemini CLI 生成 Character Design Sheet
- 支持多种动漫风格

## 使用方法

```bash
# 前置条件：先执行 /anime-storyboard 生成分镜
/anime-storyboard

# 生成角色定妆图
/anime-character
```

## 支持的风格

| 风格 | 英文关键词 |
|------|------------|
| 美式喜剧 | American comedy cartoon style |
| 日式动漫 | Japanese anime style |
| 蜡笔小新 | Crayon Shin-chan style |
| 火柴人 | stick figure |
| 像素风 | pixel art, 8-bit |

## 定妆图内容

- 多角度视图（正面、侧面、3/4）
- 多种表情
- 服装细节

## 依赖

- Gemini CLI（图像生成）
- 需要先安装 `anime`、`anime-script`、`anime-storyboard` skill

## 许可证

Apache License 2.0
