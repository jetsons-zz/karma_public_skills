# Anime Storyboard Skill

动漫分镜生成 Skill，为 Claude Code 提供详细分镜创作能力。

## 功能

- 根据剧本生成详细分镜列表
- 包含场景、画面、对白、时长、镜头信息
- 支持多种镜头类型和运动方式

## 使用方法

```bash
# 前置条件：先执行 /anime-script 生成剧本
/anime-script

# 生成分镜
/anime-storyboard
```

## 镜头类型

| 类型 | 说明 |
|------|------|
| 特写 | 面部或物体细节 |
| 中景 | 上半身或局部场景 |
| 全景 | 完整场景 |
| 远景 | 环境建立 |

## 镜头运动

- 固定、推、拉、摇、升降、跟

## 依赖

需要先安装 `anime` 和 `anime-script` skill。

## 许可证

Apache License 2.0
