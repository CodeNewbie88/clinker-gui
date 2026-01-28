# Clinker GUI - 基因簇比对可视化工具

<div align="center">

![Version](https://img.shields.io/badge/version-1.3-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

**一个为 [clinker](https://github.com/gamcil/clinker) 命令行工具设计的现代化 Windows GUI 界面**

让不熟悉命令行的生物信息学研究人员也能轻松使用基因簇比对分析

[功能特性](#-功能特性) • [快速开始](#-快速开始) • [完整安装](#-完整安装教程) • [使用指南](#-使用指南) • [常见问题](#-常见问题)

</div>

---

## 📖 目录

- [功能特性](#-功能特性)
- [快速开始](#-快速开始)
- [完整安装教程](#-完整安装教程)
  - [步骤 1：安装 Python](#步骤-1安装-python)
  - [步骤 2：安装 Clinker](#步骤-2安装-clinker-工具)
  - [步骤 3：安装 GUI 依赖](#步骤-3安装-gui-依赖)
- [使用指南](#-使用指南)
  - [启动程序](#启动程序)
  - [添加文件](#添加文件)
  - [配置参数](#配置参数)
  - [运行分析](#运行分析)
- [高级功能](#-高级功能)
- [打包成独立程序](#-打包成独立程序)
- [更新日志](#-更新日志)
- [常见问题](#-常见问题)
- [技术支持](#-技术支持)

---

## ✨ 功能特性

### 核心功能

- 🎨 **现代化界面** - 基于 CustomTkinter，支持深色模式，界面美观专业
- 🖱️ **文件拖拽** - 支持直接拖拽文件到窗口，无需点击浏览
- ⚙️ **参数配置** - 图形化配置所有 clinker 参数，无需记忆命令行语法
- 📊 **实时日志** - 显示运行过程和详细日志，不会界面卡死
- 🚀 **异步执行** - 后台运行分析，GUI 保持响应
- 🌐 **路径兼容** - 完美处理 Windows 路径空格和中文编码问题

### 用户体验优化 (v1.2 - v1.3)

- 📜 **滚动条支持** - 窗口可自由缩放，内容通过滚动条访问
- 👻 **无控制台窗口** - 运行时不弹出黑色命令行窗口，更专业
- 💾 **智能日志** - 区分 INFO 和 ERROR，不误报错误信息
- 🎯 **一键打开** - 分析完成后可直接在浏览器中打开结果

---

## 🚀 快速开始

**如果您已经安装了 Python 和 Clinker**，只需 3 步：

```bash
# 1. 进入项目目录
cd c:\Users\Lenovo\Desktop\clinker

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动程序
python clinker_gui.py
```

或者**双击** `ClinkerGUI.bat` 文件直接启动！

---

## 📦 完整安装教程

**完全零基础？跟着这个教程一步步来！**

### 步骤 1：安装 Python

#### 1.1 下载 Python

访问 Python 官网下载：https://www.python.org/downloads/

- 推荐版本：Python 3.9 或更高（支持 3.7+）
- 选择 **Windows installer (64-bit)** 下载

#### 1.2 安装 Python

1. 双击下载的安装程序（如 `python-3.9.X-amd64.exe`）
2. ⚠️ **重要**：勾选 **"Add Python to PATH"** 选项
3. 点击 **"Install Now"** 开始安装
4. 等待安装完成，点击 **"Close"**

#### 1.3 验证安装

打开命令提示符（按 `Win + R`，输入 `cmd`，按回车），输入：

```bash
python --version
```

如果显示类似 `Python 3.9.X`，说明安装成功！

如果提示"不是内部或外部命令"，请：
- 重新安装 Python，确保勾选 "Add Python to PATH"
- 或手动添加 Python 到系统环境变量

---

### 步骤 2：安装 Clinker 工具

Clinker 是实际执行基因簇比对的命令行工具，有两种安装方式：

#### 方法 A：使用 npm 安装（推荐）

**前置条件**：需要先安装 Node.js

1. **下载 Node.js**
   - 访问：https://nodejs.org/
   - 下载 LTS 版本（长期支持版）
   - 安装时保持默认选项

2. **安装 Clinker**
   ```bash
   npm install -g clinker
   ```

3. **验证安装**
   ```bash
   clinker --version
   ```

#### 方法 B：使用 pip 安装

```bash
pip install clinker-py
```

验证安装：
```bash
clinker --version
```

**说明**：
- 方法 A（npm）安装的是 JavaScript 版本，更新更快
- 方法 B（pip）安装的是 Python 版本，无需额外安装 Node.js
- **两种方法都可以**，本 GUI 程序兼容两者

---

### 步骤 3：安装 GUI 依赖

#### 3.1 进入项目目录

```bash
cd c:\Users\Lenovo\Desktop\clinker
```

或者在文件资源管理器中：
1. 打开 `c:\Users\Lenovo\Desktop\clinker` 文件夹
2. 在地址栏中输入 `cmd`，按回车

#### 3.2 安装依赖包

**方法 1：使用 requirements.txt（推荐）**

```bash
pip install -r requirements.txt
```

**方法 2：手动安装**

```bash
pip install customtkinter tkinterdnd2
```

#### 3.3 验证安装

```bash
python -c "import customtkinter; import tkinterdnd2; print('依赖安装成功!')"
```

如果显示 "依赖安装成功!"，就可以启动程序了！

---

## 📖 使用指南

### 启动程序

**方法 1：双击启动（最简单）**

双击文件夹中的 `ClinkerGUI.bat` 文件

**方法 2：命令行启动**

```bash
cd c:\Users\Lenovo\Desktop\clinker
python clinker_gui.py
```

程序启动后会显示主窗口：

```
┌─────────────────────────────────────────────────────────┐
│    Clinker GUI - 基因簇比对可视化工具                   │
├──────────────────────┬──────────────────────────────────┤
│ 📁 输入文件          │ 🚀 执行控制                      │
│ [拖拽区域]           │ [▶️ 开始分析]                    │
│ [📂 浏览文件]        │                                  │
│                      │ 📋 运行日志                      │
│ 已选文件列表:        │ ┌──────────────────────────────┐ │
│ 1. file1.gbk         │ │ 欢迎使用 Clinker GUI！       │ │
│ 2. file2.gbk         │ │ 请添加 .gbk 或 .gb 格式...   │ │
│                      │ │                              │ │
│ ⚙️ 参数配置          │ │                              │ │
│ Identity: [━━━] 0.30 │ │                              │ │
│ 输出文件名: [____]   │ │                              │ │
│ 输出目录: [____] 📁  │ │                              │ │
│                      │ │                              │ │
│ ▶ 高级选项           │ │                              │ │
└──────────────────────┴──────────────────────────────────┘
```

---

### 添加文件

#### 方法 1：拖拽文件（推荐）

1. 在文件资源管理器中找到您的基因组文件（`.gbk`, `.gb`, `.gff3`）
2. 选中一个或多个文件
3. 直接拖拽到 GUI 窗口的"拖拽区域"
4. 文件会自动添加到列表

#### 方法 2：浏览文件

1. 点击 **"📂 浏览文件"** 按钮
2. 在弹出的对话框中选择文件
3. 支持按住 `Ctrl` 键多选
4. 点击"打开"确认

#### 管理文件列表

- **删除最后一个文件**：点击 **"❌ 删除选中"** 按钮
- **清空所有文件**：点击 **"🗑️ 清空列表"** 按钮

**支持的文件格式**：
- `.gbk` / `.gb` - GenBank 格式（最常用）
- `.gff3` - GFF3 格式（需要同名的 FASTA 文件）

---

### 配置参数

#### 基础参数

**1. 序列一致性 (Identity)**
- 滑动条范围：0.0 - 1.0
- 默认值：0.30
- 说明：最小序列一致性阈值，只显示相似度高于此值的基因链接
- 建议：
  - `0.3` - 宽松，显示更多链接
  - `0.5` - 中等，平衡
  - `0.7+` - 严格，只显示高度相似的基因

**2. 输出文件名**
- 默认格式：`clinker_result_YYYYMMDD_HHMM.html`
- 可自定义，会自动添加 `.html` 扩展名
- 示例：输入 `my_result` → 生成 `my_result.html`

**3. 输出目录**
- 默认：第一个输入文件所在的目录
- 点击 📁 按钮可自定义保存位置

#### 高级选项

点击 **"▶ 高级选项"** 展开更多配置：

| 选项 | 说明 | 默认 |
|------|------|------|
| 不对齐聚类 | 跳过序列对齐步骤，仅生成可视化 | ❌ 不勾选 |
| 按文件顺序显示 | 按输入文件顺序排列，而非相似度 | ❌ 不勾选 |
| 隐藏链接标题 | 简化可视化界面，隐藏列标题 | ❌ 不勾选 |
| 隐藏对齐标题 | 隐藏聚类名称标题 | ❌ 不勾选 |
| 覆盖已有文件 | 允许覆盖同名结果文件 | ✅ 勾选 |

---

### 运行分析

#### 开始分析

1. 确认已添加至少 2 个文件
2. 检查参数配置是否正确
3. 点击 **"▶️ 开始分析"** 按钮

#### 运行中

- 按钮变为 **"⏳ 运行中..."** 并禁用
- 出现进度条动画
- 日志区域实时显示运行信息：
  ```
  ============================================================
  🚀 开始执行 Clinker 分析...
  命令: clinker file1.gbk file2.gbk -i 0.3 -p result.html -f
  ============================================================
  
  [09:00:00] INFO - Starting clinker
  [09:00:00] INFO - Parsing files:
  [09:00:00] INFO -   file1.gbk
  [09:00:00] INFO -   file2.gbk
  [09:00:03] INFO - Starting cluster alignments
  [09:00:05] INFO - Building clustermap.js visualisation
  [09:00:05] INFO - Writing to: result.html
  [09:00:05] INFO - Done!
  
  ============================================================
  ✅ 分析完成！
  结果文件: C:\path\to\result.html
  ============================================================
  ```

#### 完成后

1. 弹出完成提示框
2. 询问是否立即打开结果
   - 点击 **"是"** - 在默认浏览器中打开结果 HTML
   - 点击 **"否"** - 稍后手动打开
3. 或点击 **"📊 打开结果"** 按钮随时打开

---

## 🎯 高级功能

### 窗口滚动支持 (v1.2)

**问题**：窗口太小时部分组件被隐藏

**解决**：左侧面板支持滚动
- 窗口可自由缩小到任意大小
- 内容超出时自动显示滚动条
- 通过滚动条访问所有被隐藏的内容

**操作**：
- 鼠标滚轮：在左侧面板上滚动
- 拖拽滚动条：直接拖拽右侧滚动条
- 触摸屏：滑动手势

### 无控制台窗口 (v1.3)

**优化前**：点击"开始分析"会弹出黑色命令行窗口

**优化后**：✅ 运行时不弹出任何额外窗口
- 所有输出在 GUI 日志区域显示
- 界面更专业、更简洁
- 避免用户误操作

**技术实现**：
```python
# Windows 平台自动隐藏控制台窗口
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE
creationflags = 0x08000000  # CREATE_NO_WINDOW
```

### 智能日志显示 (v1.1)

**优化前**：clinker 的 INFO 日志被误标记为"错误"

**优化后**：✅ 智能判断真正的错误
- INFO 日志正常显示
- 只有真正的错误才标记为"⚠️ 错误信息"
- 检测关键词：ERROR, Traceback, Exception, FAILED

---

## 📦 打包成独立程序

如果您想分发给没有 Python 环境的同事，可以打包成 `.exe` 文件。

### 安装 PyInstaller

```bash
pip install pyinstaller
```

### 打包命令

**方法 1：目录模式（推荐，兼容性最好）**

```bash
pyinstaller --windowed --name "ClinkerGUI" --hidden-import tkinterdnd2 --hidden-import tkinterdnd2.tkdnd clinker_gui.py
```

打包完成后：
- 可执行文件位于：`dist\ClinkerGUI\ClinkerGUI.exe`
- 将整个 `dist\ClinkerGUI\` 文件夹压缩发送

**方法 2：单文件模式（需要注意路径）**

```powershell
pyinstaller --onefile --windowed --name "ClinkerGUI" --hidden-import tkinterdnd2 --hidden-import tkinterdnd2.tkdnd --add-data "C:\Python39\Lib\site-packages\tkinterdnd2\tkdnd;tkdnd" clinker_gui.py
```

⚠️ **注意**：将 `C:\Python39` 替换为您的 Python 实际安装路径

### 分发说明

1. 将打包后的文件夹/文件发送给同事
2. **重要**：接收者电脑上仍需安装 clinker
   ```bash
   npm install -g clinker
   # 或
   pip install clinker-py
   ```
3. 双击 `ClinkerGUI.exe` 即可运行

### 常见问题

**Q: 打包后提示缺少 tkdnd 文件？**
A: 使用目录模式（方法 1）打包，兼容性更好

**Q: Windows Defender 误报病毒？**
A: PyInstaller 打包的程序常见现象，添加到信任列表即可

**Q: 打包后程序无法启动？**
A: 
1. 检查是否安装了所有依赖
2. 尝试在命令行中运行查看错误信息
3. 使用目录模式而非单文件模式

---

## 🔄 更新日志

### v1.3 (2026-01-28) - 当前版本

**新增**：
- ✅ 隐藏控制台窗口：运行时不弹出黑色 cmd 窗口
- ✅ 改善用户体验：更专业、更简洁

**技术实现**：
- 使用 `subprocess.STARTUPINFO` 和 `CREATE_NO_WINDOW` 标志
- 平台检测：仅在 Windows 上应用

### v1.2 (2026-01-28)

**新增**：
- ✅ 滚动条支持：左侧面板可滚动
- ✅ 窗口自由缩放：无最小尺寸限制
- ✅ 响应式布局：内容通过滚动条访问

**技术实现**：
- 使用 `CTkScrollableFrame` 替代普通框架

### v1.1 (2026-01-28)

**修复**：
- ✅ 日志误报错误：智能区分 INFO 和 ERROR
- ✅ bat 启动优化：cmd 窗口自动隐藏

### v1.0 (2026-01-28)

**初始发布**：
- ✅ 基础 GUI 功能
- ✅ 文件拖拽支持
- ✅ 参数配置面板
- ✅ 实时日志显示
- ✅ 异步执行

---

## ❓ 常见问题

### 安装相关

**Q1: pip 安装依赖时报错？**

A: 尝试以下解决方案：
```bash
# 1. 更新 pip
python -m pip install --upgrade pip

# 2. 使用国内镜像源（更快）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 3. 单独安装每个包
pip install customtkinter
pip install tkinterdnd2
```

**Q2: 提示 "未找到 clinker 命令"？**

A: 
1. 确认 clinker 已安装：`clinker --version`
2. 如未安装，运行：
   - npm 方式：`npm install -g clinker`
   - pip 方式：`pip install clinker-py`
3. 重启命令行窗口和 GUI 程序

**Q3: Python 安装后仍提示"不是内部或外部命令"？**

A: 
1. 重新安装 Python，确保勾选 "Add Python to PATH"
2. 或手动添加到环境变量：
   - 右键"此电脑" → 属性 → 高级系统设置
   - 环境变量 → 系统变量 → Path
   - 添加 Python 安装路径（如 `C:\Python39\`）

### 使用相关

**Q4: 路径包含中文或空格时出错？**

A: 本程序已自动处理此问题
- 使用绝对路径
- 强制 UTF-8 编码（`PYTHONUTF8=1`）
- 如仍有问题，请查看日志详细信息

**Q5: GFF3 文件无法识别？**

A: GFF3 文件需要配套的 FASTA 文件
- 确保同目录下有对应的 FASTA 文件
- 文件名必须相同（如 `cluster1.gff3` 和 `cluster1.fa`）
- 支持的 FASTA 扩展名：`.fa`, `.fsa`, `.fna`, `.fasta`, `.faa`

**Q6: 运行时界面卡死？**

A: 程序已采用异步执行，正常情况不会卡死
- 检查 clinker 是否正常运行
- 查看日志区域了解详细信息
- 如遇卡死，请重启程序并检查输入文件

**Q7: 分析失败，没有生成结果？**

A: 检查以下几点：
1. 确认输入文件格式正确（`.gbk`, `.gb`, `.gff3`）
2. 查看日志区域的错误信息
3. 确认 clinker 已正确安装
4. 尝试在命令行中手动运行 clinker 测试

**Q8: 窗口太小，看不到所有内容？**

A: ✅ v1.2 已解决
- 左侧面板支持滚动
- 鼠标滚轮或拖拽滚动条查看被隐藏的内容
- 窗口可自由缩放

**Q9: 运行时弹出黑色窗口？**

A: ✅ v1.3 已解决
- 程序已自动隐藏控制台窗口
- 如仍出现，请确认使用的是最新版本

### 打包相关

**Q10: PyInstaller 打包后运行出错？**

A: 
1. 使用目录模式打包（推荐）
2. 确保 `--hidden-import` 参数正确
3. 检查是否包含了 tkdnd 文件
4. 在命令行运行查看详细错误

**Q11: 打包后的 .exe 被杀毒软件拦截？**

A: 
- 这是 PyInstaller 打包程序的常见问题
- 将程序添加到杀毒软件的白名单
- 或使用代码签名证书签名（适用于正式发布）

---

## 💻 技术细节

### 技术栈

- **Python**: 3.7+
- **GUI 框架**: CustomTkinter 5.2+
- **拖拽支持**: tkinterdnd2 0.4+
- **进程管理**: subprocess（标准库）
- **线程处理**: threading（标准库）

### 特殊处理

**编码问题**：
```python
os.environ["PYTHONUTF8"] = "1"  # 强制 UTF-8
```

**路径处理**：
```python
cmd.extend(self.file_paths)  # 列表传递，避免字符串拼接
```

**异步执行**：
```python
threading.Thread(target=self._execute_clinker, daemon=True).start()
```

**隐藏控制台**（Windows）：
```python
if sys.platform == 'win32':
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.wShowWindow = subprocess.SW_HIDE
    creationflags = 0x08000000  # CREATE_NO_WINDOW
```

### 项目结构

```
clinker/
├── clinker_gui.py              # 主程序（单文件）
├── requirements.txt            # Python 依赖
├── ClinkerGUI.bat         # Windows 启动脚本
├── README.md                   # 本文档
├── Bug修复报告.md              # Bug 修复历史
└── 开发报告.md                 # 开发技术总结
```

---

## 📧 技术支持

### 获取帮助

- **问题反馈**：提交 Issue 或联系开发者
- **功能建议**：欢迎提出改进想法
- **技术交流**：分享使用经验

### 参考资料

- [Clinker GitHub](https://github.com/gamcil/clinker) - 原始命令行工具
- [CustomTkinter 文档](https://github.com/TomSchimansky/CustomTkinter) - GUI 框架
- [Python subprocess 文档](https://docs.python.org/3/library/subprocess.html) - 进程管理

---

## 📄 许可证

本项目采用 MIT 许可证。

---

## 🙏 致谢

- **[clinker](https://github.com/gamcil/clinker)** - 优秀的基因簇比对工具
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - 现代化 GUI 框架
- **[tkinterdnd2](https://github.com/pmgagne/tkinterdnd2)** - 文件拖拽支持

---

<div align="center">

**开发者**: Antigravity AI Assistant  
**版本**: v1.3  
**最后更新**: 2026-01-28

**⭐ 如果这个项目对您有帮助，请给一个 Star！**

</div>
