# WeChat-Mini-Program Skill 使用说明

## 简介

WeChat-Mini-Program 是一个专门用于微信小程序开发的 Claude Code Skill，提供微信小程序开发规范、最佳实践和代码生成能力。

## 功能特性

- 遵循微信小程序官方开发规范
- 提供标准化的项目结构建议
- 生成符合规范的小程序代码
- 支持组件化、模块化开发指导
- 提供常见功能的实现方案
- 协助小程序项目部署和配置

## 安装配置

### 1. 安装 Skill

将 WeChat-Mini-Program skill 文件夹放到 Claude Code 的全局 skills 目录下：

**Windows 系统：**
```
C:\Users\你的用户名\.claude\skills\WeChat-Mini-Program\
```

**macOS/Linux 系统：**
```
~/.claude/skills/WeChat-Mini-Program/
```

### 2. 验证安装

重启 Claude Code 后，可以通过以下命令验证 skill 是否已安装：

```
/WeChat-Mini-Program
```

或直接在对话中询问：
```
我有哪些 skill
```

如果看到 `WeChat-Mini-Program` 出现在列表中，说明安装成功。

## 使用方法

### 方式一：显式调用

在 Claude Code 中输入：

```
/WeChat-Mini-Program
```

然后描述你的需求，例如：
- "创建一个新的小程序项目结构"
- "帮我实现商品列表页面"
- "生成底部导航配置"

### 方式二：自动触发

当你的对话内容涉及微信小程序开发时，Claude Code 会自动识别并使用此 skill。例如：

```
帮我创建一个微信小程序的登录页面
```

```
小程序的 TabBar 应该怎么配置？
```

## 适用场景

### 1. 项目初始化
- 创建标准化的小程序项目结构
- 生成配置文件（app.json, project.config.json 等）
- 搭建基础目录结构

### 2. 页面开发
- 生成页面文件（.wxml, .wxss, .js, .json）
- 实现常见页面功能（列表、详情、表单等）
- 添加页面导航和跳转

### 3. 组件开发
- 创建自定义组件
- 实现组件通信
- 组件样式隔离

### 4. API 集成
- 网络请求封装
- 数据缓存处理
- 用户授权流程

### 5. 功能实现
- 下拉刷新、上拉加载
- 图片上传预览
- 地理位置服务
- 支付功能集成
- 分享功能

### 6. 配置优化
- TabBar 配置
- 权限配置
- 性能优化建议

## 使用示例

### 示例 1：创建新页面

**输入：**
```
/WeChat-Mini-Program
帮我创建一个商品详情页，需要包含：
- 商品图片轮播
- 商品信息展示
- 加入购物车按钮
- 立即购买按钮
```

**Skill 会：**
- 生成页面的 .wxml 结构
- 生成对应的 .wxss 样式
- 生成 .js 逻辑代码
- 生成 .json 配置文件
- 提供代码说明和使用建议

### 示例 2：封装网络请求

**输入：**
```
/WeChat-Mini-Program
帮我封装一个通用的网络请求工具，需要支持：
- 自动显示加载提示
- 统一错误处理
- 请求拦截器
```

**Skill 会：**
- 生成 request.js 工具文件
- 提供使用示例
- 说明配置方法

### 示例 3：实现底部导航

**输入：**
```
/WeChat-Mini-Program
帮我配置底部导航，包含首页、分类、购物车、我的四个页面
```

**Skill 会：**
- 生成 app.json 中的 tabBar 配置
- 说明图标准备要求
- 提供完整配置代码

### 示例 4：组件开发

**输入：**
```
/WeChat-Mini-Program
创建一个商品卡片组件，支持：
- 显示商品图片、标题、价格
- 支持点击事件
- 可自定义样式
```

**Skill 会：**
- 生成组件的完整代码
- 说明组件的使用方法
- 提供属性和事件说明

## 开发规范

使用此 skill 生成的代码将遵循以下规范：

### 命名规范
- 文件名：kebab-case（小写短横线）
- 变量/函数：camelCase（小驼峰）
- 常量：UPPER_CASE（大写下划线）
- 组件：PascalCase（大驼峰）

### 目录结构
```
miniprogram/
├── api/                  # API 接口管理
├── components/          # 自定义组件
├── config/              # 配置文件
├── pages/               # 页面文件
├── utils/               # 工具函数
├── app.js               # 小程序入口
├── app.json             # 全局配置
├── app.wxss             # 全局样式
└── project.config.json  # 项目配置
```

### 代码风格
- 使用 ES6+ 语法
- 模块化开发
- 注释完整清晰
- 错误处理完善

## 最佳实践

### 1. 分层架构
- UI 层（pages/components）
- 业务逻辑层（api）
- 工具层（utils）
- 配置层（config）

### 2. 组件化开发
- 提取可复用组件
- 保持组件单一职责
- 使用组件通信机制

### 3. 性能优化
- 按需加载
- 图片懒加载
- 合理使用缓存
- 避免频繁 setData

### 4. 安全规范
- 敏感数据加密
- 接口鉴权
- 用户信息保护

## 常见问题

### Q1: Skill 不生效怎么办？
**A:**
1. 确认 skill 文件夹已正确放置在 `~/.claude/skills/` 目录下
2. 检查 skill 文件夹名称是否为 `WeChat-Mini-Program`
3. 重启 Claude Code
4. 使用命令 `我有哪些 skill` 验证是否识别

### Q2: 如何让生成的代码更符合我的项目风格？
**A:** 在提问时详细描述你的需求和项目规范，例如：
```
/WeChat-Mini-Program
使用 TypeScript 创建一个登录页面，采用 Composition API 风格
```

### Q3: 可以用这个 skill 调试小程序吗？
**A:** Skill 主要用于代码生成和开发指导，调试仍需在微信开发者工具中进行。

### Q4: 生成的代码可以直接使用吗？
**A:** 生成的代码遵循标准规范，但可能需要根据实际项目需求进行调整，特别是：
- API 接口地址
- 图片资源路径
- 业务逻辑细节

## 技术支持

### 相关资源
- [微信小程序官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/)
- [微信小程序设计指南](https://developers.weixin.qq.com/miniprogram/design/)
- [微信开放社区](https://developers.weixin.qq.com/community/develop/mixflow)

### 反馈建议
如果在使用过程中遇到问题或有改进建议，可以：
1. 在 Claude Code 中详细描述问题
2. 提供完整的错误信息
3. 说明期望的效果

## 版本信息

- Skill 版本：1.0.0
- 兼容 Claude Code 版本：最新版
- 支持的小程序基础库：2.0+

## 许可说明

本 Skill 遵循微信小程序开发规范，生成的代码可自由使用和修改。

---

**提示**：使用 `/WeChat-Mini-Program` 命令即可开始使用此 skill 进行小程序开发！
