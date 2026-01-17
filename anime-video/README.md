# Anime Video Skill

动漫分镜视频生成 Skill，为 Claude Code 提供视频片段生成能力。

## 功能

- 基于分镜列表生成视频提示词
- 调用 Veo API 生成每个镜头的视频片段
- 支持多种镜头运动方式

## 使用方法

```bash
# 前置条件：先执行 /anime-character 生成定妆图
/anime-character

# 生成视频片段
/anime-video
```

## Veo API

使用 Google Veo 3.1 生成视频。

**时长限制**：仅支持 4、6、8 秒

## 镜头运动

| 中文 | 英文提示词 |
|------|------------|
| 固定 | static camera |
| 推进 | camera slowly zooms in |
| 拉远 | camera slowly zooms out |
| 左摇 | camera pans left |
| 右摇 | camera pans right |
| 跟随 | camera follows the character |

## 依赖

- Veo API 访问权限
- 需要先安装 `anime`、`anime-script`、`anime-storyboard`、`anime-character` skill

## 许可证

Apache License 2.0
