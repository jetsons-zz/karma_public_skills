# Anime Generation Skill

基于 oiioii 工作流程的自动化动漫制作 Skill，为 Claude Code 提供完整的动漫制作能力。

## 功能特性

- **模块化命令**：每个制作阶段独立为一个命令
- **Human-in-the-Loop**：用户通过命令控制流程节奏
- **集成 Gemini CLI**：图像/视频生成能力
- **状态持久化**：项目进度跨会话保存

## 命令体系

| 命令 | 功能 | 说明 |
|------|------|------|
| `/anime` | 创建/加载项目 | 设置风格、时长、比例等参数 |
| `/anime-script` | 生成剧本 | 故事梗概、角色、分镜概述 |
| `/anime-storyboard` | 生成分镜 | 详细分镜列表 |
| `/anime-character` | 生成定妆图 | 角色设计图 |
| `/anime-video` | 生成视频 | 各镜头视频片段 |
| `/anime-merge` | 合成视频 | BGM + 字幕 + 最终输出 |

## 快速开始

```bash
# 创建新项目
/anime "一个25岁上班族为主角的搞笑动漫，30秒"

# 生成剧本
/anime-script

# 生成分镜
/anime-storyboard

# 生成角色定妆图
/anime-character

# 生成视频片段
/anime-video

# 合成最终视频
/anime-merge
```

## 支持的风格

| 风格 | 关键词 | 适用场景 |
|------|--------|----------|
| 火柴人 | stick figure | 简约搞笑 |
| 美式喜剧 | American comedy cartoon | 搞笑夸张 |
| 日式动漫 | Japanese anime style | 通用动漫 |
| 像素风 | pixel art, 8-bit | 复古游戏 |
| 水彩风 | watercolor painting | 唯美意境 |
| 赛博朋克 | cyberpunk, neon | 科幻未来 |

## 依赖

- Gemini CLI（图像/视频生成）
- FFmpeg（视频合成）

## 许可证

Apache License 2.0
