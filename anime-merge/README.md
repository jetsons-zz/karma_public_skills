# Anime Merge Skill

动漫视频合成 Skill，为 Claude Code 提供最终视频合成能力。

## 功能

- 合并所有分镜视频片段
- 添加背景音乐（BGM）
- 添加字幕
- 导出最终视频

## 使用方法

```bash
# 前置条件：先执行 /anime-video 生成视频片段
/anime-video

# 合成最终视频
/anime-merge
```

## 导出参数

| 参数 | 竖版9:16 | 横版16:9 |
|------|----------|----------|
| 分辨率 | 1080x1920 | 1920x1080 |
| 帧率 | 24fps | 24fps |
| 编码 | H.264 | H.264 |
| 音频 | AAC 128kbps | AAC 128kbps |

## FFmpeg 功能

- 视频拼接
- 添加 BGM
- 添加字幕
- 淡入淡出
- 速度调整
- 添加水印

## 依赖

- FFmpeg
- 需要先完成整个动漫制作流程

## 许可证

Apache License 2.0
