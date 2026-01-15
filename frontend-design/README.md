# Frontend Design Skill

> 🎨 使用 AI 创建独特的、生产级别的前端界面

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-violet.svg)](https://claude.ai)
[![Made with React](https://img.shields.io/badge/Made%20with-React-61dafb.svg)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178c6.svg)](https://typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.x-38bdf8.svg)](https://tailwindcss.com)

**[English](README_EN.md) | 简体中文**

## 📖 概述

这是一个为 Claude Code 设计的 AI 技能，用于构建精美的、生产就绪的 Web 界面，避免千篇一律的 AI 美学。可以生成创意十足、精致优雅的登陆页面、仪表板、投资组合网站等代码。

本 Skill 专为 Anthropic 的 [Claude Code](https://claude.ai) 设计，让开发者能够通过对话式 AI 辅助创建高质量的前端应用。

## ✨ 功能特性

- 🎯 **智能默认配置**: 开箱即用，无需复杂配置
- 🎨 **20+ 项目类型**: 登陆页面、仪表板、投资组合、电商、博客等
- 🖼️ **视觉参考支持**: 支持 URL、截图、手绘草图或 Figma/Sketch 设计稿
- 📱 **响应式设计**: 移动优先，支持所有标准断点 (sm, md, lg, xl, 2xl)
- ♿ **无障碍优先**: 符合 WCAG AA 标准，支持屏幕阅读器和键盘导航
- 🚀 **生产就绪**: 包含 Vercel、Netlify、GitHub Pages、Docker 部署配置
- 🎭 **自定义设计系统**: 自动生成设计令牌、调色板、排版比例、间距系统
- 🧩 **现代技术栈**: React 18+, Vite 5.x, TypeScript 5.x, Tailwind CSS 3.x, shadcn/ui
- ⚡ **快速开发**: 热重载、TypeScript 检查、ESLint、Prettier 预配置
- 🎬 **流畅动画**: 过渡效果、微交互和高级动画支持

## 🚀 快速开始

### 安装

1. **克隆仓库**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/karma_public_skills.git
   cd karma_public_skills/frontend-design
   ```

2. **复制到你的项目**:
   ```bash
   # Linux/Mac
   cp -r .claude /path/to/your/project/

   # Windows
   xcopy .claude C:\path\to\your\project\.claude\ /E /I
   ```

3. **开始使用** - Claude Code 会自动检测到这个 skill:
   ```
   使用 frontend-design skill 创建一个 SaaS 产品的登陆页面
   ```

### 全局安装（所有项目可用）

**macOS/Linux**:
```bash
cp -r .claude/skills/frontend-design ~/.config/claude-code/skills/
```

**Windows**:
```powershell
xcopy .claude\skills\frontend-design %APPDATA%\claude-code\skills\frontend-design\ /E /I
```

### 备选方案：下载 ZIP

1. 下载本仓库的 ZIP 文件
2. 解压到你想要的位置
3. 复制 `frontend-design/.claude` 文件夹到你的项目根目录

## 📚 使用示例

### 基础用法

创建一个项目，只需最少的输入：
```
使用 frontend-design 创建一个投资组合网站
```

### 使用 URL 参考

参考现有网站的风格：
```
创建一个类似 https://stripe.com 的登陆页面，使用 frontend-design
```

### 使用截图

上传或提供截图路径：
```
使用 frontend-design 重现这个设计
[上传 screenshot.png 或提供路径: C:\Users\...\design.png]
```

### 使用手绘草图

将你的草图变成真实代码：
```
我画了一个草图。使用 frontend-design 把它实现出来。
[上传你的纸质草图照片]
```

### 提供具体需求

提供详细的规格说明：
```
使用 frontend-design 创建一个仪表板，包括：
- 侧边栏导航
- 数据可视化图表
- 用户资料区域
- 暗色模式支持
```

## 🎯 支持的项目类型

| 类别 | 项目类型 |
|----------|---------------|
| **商业** | 登陆页面、公司网站、定价页面、服务展示 |
| **创意** | 投资组合网站、摄影作品集、简历网站 |
| **数据** | 仪表板、管理面板、数据分析界面 |
| **内容** | 博客网站、文章模板、文档站点 |
| **电商** | 产品登陆页、商店首页、产品展示 |
| **应用** | SaaS 产品页、应用登陆页、移动应用界面 |
| **教育** | 课程登陆页、学校网站 |
| **活动** | 活动网站、预订页面 |
| **健康** | 诊所网站、健身房网站 |
| **餐饮** | 餐厅网站、外卖界面 |
| **房地产** | 房产网站、房地产门户 |
| **社区** | 论坛首页、社区网站 |
| **工具** | 计算器页面、多步骤表单、即将推出页面 |

## 🛠️ 技术栈

### 默认技术栈（生产就绪）

| 组件 | 版本 | 用途 |
|-----------|---------|---------|
| **React** | 18+ | UI 框架 |
| **Vite** | 5.x | 构建工具（快速、现代化） |
| **TypeScript** | 5.x | 类型安全和更好的开发体验 |
| **Tailwind CSS** | 3.x | 功能优先的样式框架（**稳定版本，非 4.x**） |
| **shadcn/ui** | Latest | 精美、可访问的组件库 |
| **Lucide React** | Latest | 专业图标库 |
| **PostCSS** | 8.4+ | CSS 后处理 |
| **Autoprefixer** | 10.4+ | 浏览器兼容性 |

**重要版本说明:**
- **Tailwind CSS**: 使用稳定的 3.x 版本以确保生产可靠性（非 4.x alpha/beta）
- 所有依赖都使用稳定、经过充分测试的版本
- 这套技术栈适合生产环境、文档完善、对初学者友好

### 支持的替代技术栈

可以要求 Claude 使用其他技术：
- **框架**: Next.js, Vue 3, Svelte, Angular, Solid.js
- **样式**: Bootstrap, Material-UI, Chakra UI, Ant Design, CSS-in-JS (styled-components, emotion)
- **状态管理**: Zustand, Redux, MobX, Jotai, Recoil
- **表单**: React Hook Form, Formik
- **动画**: Framer Motion, GSAP, React Spring
- **3D**: Three.js, React Three Fiber

## 📖 工作原理

该 Skill 遵循四个阶段的工作流程：

### 阶段 1: 理解（1-2 分钟）
- 分析你的需求
- 处理设计参考（URL/截图/草图）
- 识别目标受众和项目类型
- 使用智能默认值，只在必要时提问

### 阶段 2: 项目设置（2-3 分钟）
- 创建 Vite + React + TypeScript 项目结构
- 安装和配置 Tailwind CSS 3.x（稳定版）
- 设置 shadcn/ui 及你偏好的主题
- 建立标准文件夹结构

### 阶段 3: 组件生成（5-10 分钟）
- 构建布局组件（Header、Footer、Sidebar）
- 实现页面区块（Hero、Features、Testimonials 等）
- 创建 UI 组件（Button、Card、Form 等）
- 编写工具函数和自定义 hooks

### 阶段 4: 样式和优化（3-5 分钟）
- 应用响应式设计模式
- 添加动画和过渡效果
- 设置排版和间距系统
- 应用颜色主题和设计令牌

**总时长**: 15-20 分钟完成一个完整的、生产就绪的项目

## 🎨 设计功能

### 设计系统组件
- **颜色系统**: 主色、辅助色、强调色、中性色和语义色，包含完整调色板
- **排版比例**: 和谐的字体大小、字重和行高
- **间距系统**: 基于 4px 的网格，保证间距一致性
- **阴影库**: 多层次阴影的高度系统
- **圆角半径**: 一致的圆角令牌
- **动画预设**: 持续时间和缓动函数令牌

### 内置功能
- ✅ 响应式断点 (sm:640px, md:768px, lg:1024px, xl:1280px, 2xl:1536px)
- ✅ 暗色模式支持（可选）
- ✅ 触摸友好的交互（44px 最小触摸目标）
- ✅ 带验证的无障碍表单
- ✅ 加载状态和骨架屏
- ✅ 错误处理和降级方案
- ✅ SEO 友好的标记
- ✅ 性能优化

## 📦 你将得到什么

每个生成的项目都包括：

### 代码和配置
- ✅ 完整的、生产就绪的源代码
- ✅ TypeScript 类型定义
- ✅ Vite 构建配置
- ✅ Tailwind CSS 配置
- ✅ PostCSS 和 Autoprefixer 设置
- ✅ ESLint 和 Prettier 配置（可选）

### 文档
- ✅ 全面的代码注释
- ✅ 自定义指南
- ✅ 组件使用示例
- ✅ 设计令牌参考

### 部署
- ✅ Vercel 部署配置 (`vercel.json`)
- ✅ Netlify 部署配置 (`netlify.toml`)
- ✅ GitHub Pages 构建脚本
- ✅ Docker 容器化配置

### 依赖
- ✅ 包含所有依赖的完整 `package.json`
- ✅ 用于可重现构建的锁定文件
- ✅ 开发和生产脚本

## 🚀 开发命令

项目生成后，使用这些命令：

```bash
# 安装依赖
npm install

# 启动开发服务器 (http://localhost:5173)
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview

# 类型检查
npm run type-check

# 代码检查（如果配置了）
npm run lint
npm run lint:fix

# 代码格式化（如果配置了）
npm run format

# 添加 shadcn/ui 组件
npx shadcn-ui@latest add [component-name]
```

## 📸 视觉参考分析

该 Skill 可以分析并从各种参考类型中提取设计元素：

### 支持的参考类型
1. **🌐 URL 分析** - 提取 HTML/CSS，计算样式，识别模式
2. **🎨 颜色提取** - 从渲染元素获取精确的十六进制代码
3. **📝 字体检测** - 识别字体系列并建议替代方案
4. **📏 间距测量** - 计算精确的 padding/margin/gap 值
5. **📱 响应式检测** - 识别断点和移动端布局
6. **🎬 动画分析** - 提取过渡时间和缓动函数

### 工作原理
- 使用 WebFetch 进行 URL 分析
- 使用 Playwright 提取计算样式（如果可用）
- 对截图和草图降级到手动分析
- 基于提取的元素生成设计令牌

## 🎓 学习资源

内置链接和文档：
- [React 官方文档](https://react.dev)
- [Vite 文档](https://vitejs.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [shadcn/ui 组件](https://ui.shadcn.com)
- [TypeScript 手册](https://typescriptlang.org)
- [Lucide 图标](https://lucide.dev)

## 🔧 高级功能（可选）

可以要求 Claude 添加：
- 🔐 用户认证（登录、注册、密码重置）
- 🗄️ 数据库集成（Supabase、Firebase、MongoDB）
- 📊 状态管理（Zustand、Redux、Context API）
- 📝 表单处理（React Hook Form + Zod 验证）
- 📈 数据分析（Google Analytics、Plausible、Mixpanel）
- 🔍 SEO 优化（meta 标签、Open Graph、站点地图）
- 🌍 国际化（i18n、多语言支持）
- 🧪 测试框架（Vitest、React Testing Library、Playwright）
- 🎬 高级动画（Framer Motion、GSAP）
- 🎮 3D 效果（Three.js、React Three Fiber）

## 🤝 贡献

欢迎贡献！以下是你可以帮助的方式：

1. **报告 Bug**: 提交 Issue 并详细描述重现步骤
2. **建议功能**: 分享你对改进的想法
3. **提交 PR**: Fork、创建分支、修改、提交 Pull Request
4. **改进文档**: 帮助让文档更清晰、更全面
5. **分享示例**: 贡献示例项目或模板

## 🐛 故障排除

### 常见问题

**问题**: Tailwind CSS 不工作
- **解决方案**: 确保安装了 Tailwind CSS 3.x（运行 `npm list tailwindcss`）
- **解决方案**: 检查 `tailwind.config.js` 的 content 路径是否正确

**问题**: 找不到 shadcn/ui 组件
- **解决方案**: 运行 `npx shadcn-ui@latest init` 进行初始化
- **解决方案**: 使用 `npx shadcn-ui@latest add [component]` 添加单个组件

**问题**: TypeScript 错误
- **解决方案**: 运行 `npm run type-check` 查看所有错误
- **解决方案**: 确保安装了所有依赖

**问题**: 构建失败
- **解决方案**: 检查 Node.js 版本（需要 18+）
- **解决方案**: 删除 `node_modules` 并重新安装: `rm -rf node_modules && npm install`

## 📄 许可证

本项目采用 **Apache License 2.0** 许可证 - 详见 [LICENSE](.claude/skills/frontend-design/LICENSE.txt) 文件。

### 这意味着什么
- ✅ 允许商业使用
- ✅ 允许修改
- ✅ 允许分发
- ✅ 允许专利使用
- ✅ 允许私人使用
- ⚠️ 不授予商标使用权
- ⚠️ 不提供责任和保证

## 🙏 致谢

本 Skill 基于并为以下出色的开源项目构建：

- **[Claude Code](https://claude.ai)** by Anthropic - AI 助手平台
- **[shadcn/ui](https://ui.shadcn.com)** by shadcn - 精美的组件库
- **[React](https://react.dev)** by Meta - UI 框架
- **[Vite](https://vitejs.dev)** by Evan You - 构建工具
- **[Tailwind CSS](https://tailwindcss.com)** by Tailwind Labs - 功能优先的 CSS
- **[TypeScript](https://typescriptlang.org)** by Microsoft - 类型安全
- **[Lucide](https://lucide.dev)** - 图标库

特别感谢开源社区让这些工具成为可能！

## 📞 支持与社区

需要帮助或想要交流？

- 📖 **文档**: 本 README 包含所有信息
- 🐛 **Bug 报告**: [GitHub Issues](https://github.com/YOUR_USERNAME/karma_public_skills/issues)
- 💬 **讨论**: [GitHub Discussions](https://github.com/YOUR_USERNAME/karma_public_skills/discussions)
- 🎯 **功能请求**: 提交 Issue 并添加 "enhancement" 标签

## 📊 项目状态

- ✅ **稳定**: 核心功能已可用于生产环境
- 🔄 **积极开发**: 定期更新和改进
- 📝 **文档完善**: 全面的指南和示例
- 🧪 **经过测试**: 在实际项目中使用
- 🌍 **开源**: 社区驱动的开发

## 🗺️ 路线图

计划的未来增强功能：
- [ ] 多平台支持（Cursor、Windsurf 等）
- [ ] 示例项目画廊
- [ ] 独立使用的 CLI 工具
- [ ] 设计系统模板
- [ ] 组件库预设
- [ ] 与设计工具集成（Figma API）
- [ ] AI 驱动的设计建议
- [ ] 性能优化模板

## 📈 统计数据

- 📁 支持 **20+ 项目类型**
- 🎨 提供 **100+ 组件变体**
- 🚀 平均项目创建时间 **15-20 分钟**
- ⚡ **零配置**即可开始使用
- 📚 超过 **2400 行**的全面文档

---

<div align="center">

**为注重设计的开发者打造**

[⭐ Star 本仓库](https://github.com/YOUR_USERNAME/karma_public_skills) • [🐛 报告 Bug](https://github.com/YOUR_USERNAME/karma_public_skills/issues) • [💡 功能建议](https://github.com/YOUR_USERNAME/karma_public_skills/issues)

</div>
