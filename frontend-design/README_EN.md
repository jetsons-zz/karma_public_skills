# Frontend Design Skill

> 🎨 Create distinctive, production-grade frontend interfaces with AI

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-violet.svg)](https://claude.ai)
[![Made with React](https://img.shields.io/badge/Made%20with-React-61dafb.svg)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178c6.svg)](https://typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.x-38bdf8.svg)](https://tailwindcss.com)

## 📖 Overview

AI-powered skill for building beautiful, production-ready web interfaces that avoid generic AI aesthetics. Generates creative, polished code for landing pages, dashboards, portfolios, and more.

This skill is specifically designed for [Claude Code](https://claude.ai) by Anthropic, enabling developers to create high-quality frontend applications through conversational AI assistance.

## ✨ Features

- 🎯 **Smart Defaults**: Works out of the box with minimal configuration
- 🎨 **20+ Project Types**: Landing pages, dashboards, portfolios, e-commerce, blogs, and more
- 🖼️ **Visual Reference Support**: Accepts URL, screenshot, hand-drawn sketch, or Figma/Sketch designs
- 📱 **Responsive Design**: Mobile-first approach with all standard breakpoints (sm, md, lg, xl, 2xl)
- ♿ **Accessibility First**: WCAG AA compliant, screen reader friendly, keyboard navigation
- 🚀 **Production Ready**: Vercel, Netlify, GitHub Pages, Docker deployment configs included
- 🎭 **Custom Design System**: Automatic design tokens, color palettes, typography scales, spacing systems
- 🧩 **Modern Stack**: React 18+, Vite 5.x, TypeScript 5.x, Tailwind CSS 3.x, shadcn/ui
- ⚡ **Fast Development**: Hot reload, TypeScript checking, ESLint, Prettier pre-configured
- 🎬 **Smooth Animations**: Transitions, micro-interactions, and advanced animations support

## 🚀 Quick Start

### Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/karma_public_skills.git
   cd karma_public_skills/frontend-design
   ```

2. **Copy to your project**:
   ```bash
   # Linux/Mac
   cp -r .claude /path/to/your/project/

   # Windows
   xcopy .claude C:\path\to\your\project\.claude\ /E /I
   ```

3. **Start using it** - Claude Code will automatically detect the skill:
   ```
   使用 frontend-design skill 创建一个 SaaS 产品的登陆页面
   ```

### Global Installation (All Projects)

**macOS/Linux**:
```bash
cp -r .claude/skills/frontend-design ~/.config/claude-code/skills/
```

**Windows**:
```powershell
xcopy .claude\skills\frontend-design %APPDATA%\claude-code\skills\frontend-design\ /E /I
```

### Alternative: Download ZIP

1. Download this repository as ZIP
2. Extract to your desired location
3. Copy the `frontend-design/.claude` folder to your project root

## 📚 Usage Examples

### Basic Usage

Create a project with minimal input:
```
Use frontend-design to build a portfolio website
```

### With URL Reference

Reference an existing website's style:
```
Create a landing page like https://stripe.com using frontend-design
```

### With Screenshot

Upload or provide a screenshot path:
```
Use frontend-design to recreate this design
[Upload screenshot.png or provide path: C:\Users\...\design.png]
```

### With Hand-drawn Sketch

Turn your sketches into real code:
```
I drew a quick sketch. Use frontend-design to make it real.
[Upload photo of your paper sketch]
```

### With Specific Requirements

Provide detailed specifications:
```
Use frontend-design to create a dashboard with:
- Sidebar navigation
- Data visualization charts
- User profile section
- Dark mode support
```

## 🎯 Supported Project Types

| Category | Project Types |
|----------|---------------|
| **Business** | Landing Pages, Company Websites, Pricing Pages, Service Showcase |
| **Creative** | Portfolio Sites, Photographer Portfolios, Resume Websites |
| **Data** | Dashboards, Admin Panels, Analytics Interfaces |
| **Content** | Blog Websites, Article Templates, Documentation Sites |
| **E-commerce** | Product Landing Pages, Store Homepages, Product Showcases |
| **Apps** | SaaS Product Pages, App Landing Pages, Mobile App Interfaces |
| **Education** | Course Landing Pages, School Websites |
| **Events** | Event Websites, Booking Pages |
| **Health** | Clinic Websites, Gym Websites |
| **Food** | Restaurant Websites, Food Delivery Interfaces |
| **Real Estate** | Property Websites, Real Estate Portals |
| **Community** | Forum Homepages, Community Sites |
| **Tools** | Calculator Pages, Multi-step Forms, Coming Soon Pages |

## 🛠️ Technology Stack

### Default Stack (Production-Ready)

| Component | Version | Purpose |
|-----------|---------|---------|
| **React** | 18+ | UI framework |
| **Vite** | 5.x | Build tool (fast, modern) |
| **TypeScript** | 5.x | Type safety and better DX |
| **Tailwind CSS** | 3.x | Utility-first styling (**stable version, NOT 4.x**) |
| **shadcn/ui** | Latest | Beautiful, accessible components |
| **Lucide React** | Latest | Professional icon library |
| **PostCSS** | 8.4+ | CSS post-processing |
| **Autoprefixer** | 10.4+ | Browser compatibility |

**Important Version Notes:**
- **Tailwind CSS**: Using stable 3.x version for production reliability (NOT 4.x alpha/beta)
- All dependencies use stable, well-tested versions
- This stack is production-ready, well-documented, and beginner-friendly

### Alternative Stack Support

Ask Claude to use alternative technologies:
- **Frameworks**: Next.js, Vue 3, Svelte, Angular, Solid.js
- **Styling**: Bootstrap, Material-UI, Chakra UI, Ant Design, CSS-in-JS (styled-components, emotion)
- **State**: Zustand, Redux, MobX, Jotai, Recoil
- **Forms**: React Hook Form, Formik
- **Animation**: Framer Motion, GSAP, React Spring
- **3D**: Three.js, React Three Fiber

## 📖 How It Works

The skill follows a four-phase workflow:

### Phase 1: Understanding (1-2 minutes)
- Analyzes your requirements
- Processes design references (URL/screenshot/sketch)
- Identifies target audience and project type
- Uses smart defaults, asks questions only when necessary

### Phase 2: Project Setup (2-3 minutes)
- Creates Vite + React + TypeScript project structure
- Installs and configures Tailwind CSS 3.x (stable)
- Sets up shadcn/ui with your preferred theme
- Establishes standard folder structure

### Phase 3: Component Generation (5-10 minutes)
- Builds layout components (Header, Footer, Sidebar)
- Implements page sections (Hero, Features, Testimonials, etc.)
- Creates UI components (Button, Card, Form, etc.)
- Writes utility functions and custom hooks

### Phase 4: Styling & Optimization (3-5 minutes)
- Applies responsive design patterns
- Adds animations and transitions
- Sets up typography and spacing systems
- Applies color themes and design tokens

**Total Time**: 15-20 minutes for a complete, production-ready project

## 🎨 Design Features

### Design System Components
- **Color Systems**: Primary, secondary, accent, neutral, and semantic colors with full palettes
- **Typography Scale**: Harmonious font sizes, weights, and line heights
- **Spacing System**: 4px base grid for consistent spacing
- **Shadow Library**: Elevation system with multiple shadow levels
- **Border Radius**: Consistent corner radius tokens
- **Animation Presets**: Duration and easing function tokens

### Built-in Features
- ✅ Responsive breakpoints (sm:640px, md:768px, lg:1024px, xl:1280px, 2xl:1536px)
- ✅ Dark mode support (optional)
- ✅ Touch-friendly interactions (44px minimum touch targets)
- ✅ Accessible forms with validation
- ✅ Loading states and skeletons
- ✅ Error handling and fallbacks
- ✅ SEO-friendly markup
- ✅ Performance optimizations

## 📦 What You Get

Every generated project includes:

### Code & Configuration
- ✅ Complete, production-ready source code
- ✅ TypeScript type definitions
- ✅ Vite build configuration
- ✅ Tailwind CSS configuration
- ✅ PostCSS and Autoprefixer setup
- ✅ ESLint and Prettier configs (optional)

### Documentation
- ✅ Comprehensive code comments
- ✅ Customization guide
- ✅ Component usage examples
- ✅ Design token reference

### Deployment
- ✅ Vercel deployment config (`vercel.json`)
- ✅ Netlify deployment config (`netlify.toml`)
- ✅ GitHub Pages build script
- ✅ Dockerfile for containerization

### Dependencies
- ✅ Complete `package.json` with all dependencies
- ✅ Lock file for reproducible builds
- ✅ Development and production scripts

## 🚀 Development Commands

After project generation, use these commands:

```bash
# Install dependencies
npm install

# Start development server (http://localhost:5173)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Type checking
npm run type-check

# Linting (if configured)
npm run lint
npm run lint:fix

# Formatting (if configured)
npm run format

# Add shadcn/ui components
npx shadcn-ui@latest add [component-name]
```

## 📸 Visual Reference Analysis

The skill can analyze and extract design elements from various reference types:

### Supported Reference Types
1. **🌐 URL Analysis** - Extract HTML/CSS, compute styles, identify patterns
2. **🎨 Color Extraction** - Get exact hex codes from rendered elements
3. **📝 Font Detection** - Identify font families and suggest alternatives
4. **📏 Spacing Measurement** - Calculate precise padding/margin/gap values
5. **📱 Responsive Detection** - Identify breakpoints and mobile layouts
6. **🎬 Animation Analysis** - Extract transition timings and easing functions

### How It Works
- Uses WebFetch for URL analysis
- Uses Playwright for computed style extraction (if available)
- Falls back to manual analysis for screenshots and sketches
- Generates design tokens based on extracted elements

## 🎓 Learning Resources

Built-in links and documentation:
- [React Official Docs](https://react.dev)
- [Vite Documentation](https://vitejs.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [shadcn/ui Components](https://ui.shadcn.com)
- [TypeScript Handbook](https://typescriptlang.org)
- [Lucide Icons](https://lucide.dev)

## 🔧 Advanced Features (Optional)

Ask Claude to add:
- 🔐 User authentication (login, signup, password reset)
- 🗄️ Database integration (Supabase, Firebase, MongoDB)
- 📊 State management (Zustand, Redux, Context API)
- 📝 Form handling (React Hook Form + Zod validation)
- 📈 Analytics (Google Analytics, Plausible, Mixpanel)
- 🔍 SEO optimization (meta tags, Open Graph, sitemap)
- 🌍 Internationalization (i18n, multi-language support)
- 🧪 Testing framework (Vitest, React Testing Library, Playwright)
- 🎬 Advanced animations (Framer Motion, GSAP)
- 🎮 3D effects (Three.js, React Three Fiber)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue with detailed reproduction steps
2. **Suggest Features**: Share your ideas for improvements
3. **Submit PRs**: Fork, create a branch, make changes, and submit a pull request
4. **Improve Documentation**: Help make the docs clearer and more comprehensive
5. **Share Examples**: Contribute example projects or templates

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 🐛 Troubleshooting

### Common Issues

**Issue**: Tailwind CSS not working
- **Solution**: Ensure Tailwind CSS 3.x is installed (run `npm list tailwindcss`)
- **Solution**: Check `tailwind.config.js` content paths are correct

**Issue**: shadcn/ui components not found
- **Solution**: Run `npx shadcn-ui@latest init` to initialize
- **Solution**: Add individual components with `npx shadcn-ui@latest add [component]`

**Issue**: TypeScript errors
- **Solution**: Run `npm run type-check` to see all errors
- **Solution**: Ensure all dependencies are installed

**Issue**: Build fails
- **Solution**: Check Node.js version (requires 18+)
- **Solution**: Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`

## 📄 License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

### What This Means
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Patent use allowed
- ✅ Private use allowed
- ⚠️ Trademark use NOT granted
- ⚠️ Liability and warranty NOT provided

## 🙏 Acknowledgments

This skill is built with and for amazing open-source projects:

- **[Claude Code](https://claude.ai)** by Anthropic - The AI assistant platform
- **[shadcn/ui](https://ui.shadcn.com)** by shadcn - Beautiful component library
- **[React](https://react.dev)** by Meta - UI framework
- **[Vite](https://vitejs.dev)** by Evan You - Build tool
- **[Tailwind CSS](https://tailwindcss.com)** by Tailwind Labs - Utility-first CSS
- **[TypeScript](https://typescriptlang.org)** by Microsoft - Type safety
- **[Lucide](https://lucide.dev)** - Icon library

Special thanks to the open-source community for making these tools available!

## 📞 Support & Community

Need help or want to connect?

- 📖 **Documentation**: [SKILL.md](.claude/skills/frontend-design/SKILL.md) - Comprehensive skill documentation
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/YOUR_USERNAME/frontend-design-skill/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/frontend-design-skill/discussions)
- 🎯 **Feature Requests**: Open an issue with the "enhancement" label
- 📧 **Contact**: [Your email or contact method]

## 📊 Project Status

- ✅ **Stable**: Core functionality is production-ready
- 🔄 **Active Development**: Regular updates and improvements
- 📝 **Well Documented**: Comprehensive guides and examples
- 🧪 **Tested**: Used in real-world projects
- 🌍 **Open Source**: Community-driven development

## 🗺️ Roadmap

Future enhancements planned:
- [ ] Multi-platform support (Cursor, Windsurf, etc.)
- [ ] Example project gallery
- [ ] CLI tool for standalone usage
- [ ] Design system templates
- [ ] Component library presets
- [ ] Integration with design tools (Figma API)
- [ ] AI-powered design suggestions
- [ ] Performance optimization templates

## 📈 Stats

- 📁 **20+ Project Types** supported
- 🎨 **100+ Component Variants** available
- 🚀 **15-20 minute** average project creation time
- ⚡ **Zero config** required to get started
- 📚 **2400+ lines** of comprehensive documentation

---

<div align="center">

**Made with ❤️ for developers who care about design**

[⭐ Star this repo](https://github.com/YOUR_USERNAME/frontend-design-skill) • [🐛 Report Bug](https://github.com/YOUR_USERNAME/frontend-design-skill/issues) • [💡 Request Feature](https://github.com/YOUR_USERNAME/frontend-design-skill/issues)

</div>
